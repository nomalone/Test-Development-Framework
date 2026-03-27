import uuid
from seldom.request import HttpRequest
import json
from config.config import Config
from config.mylogger import my_log


class APIClient(HttpRequest):
    def __init__(self, host):
        """
        初始化API客户端
        """
        self.llm_url = Config().LLM_URL
        self.authorization = Config().LLM_Authorization

        self.headers = {
            "Authorization": f"Bearer {self.authorization}",
            "Content-Type": "application/json",
            "Host": f"{host}.cn"
        }
        self.model = Config().LLM_MODEL

    def _parse_sse_stream(self, response):
        """解析SSE流式响应，返回完整响应文本"""
        full_response = ""
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8').strip()
                if line_str.startswith("data:"):
                    line_str = line_str[5:].strip()

                if line_str == "[DONE]":
                    break

                try:
                    json_data = json.loads(line_str)
                    if "choices" in json_data and len(json_data["choices"]) > 0:
                        delta = json_data["choices"][0].get("delta", {})
                        content_data = delta.get("content", "")
                        if content_data:
                            full_response += content_data
                except json.JSONDecodeError:
                    my_log.error(f"无法解析原始的流式响应: {line_str}")
                    # 流式监测到敏感数据时，可能截断滑动窗口导致响应不是完整json，尝试通过data分割提取
                    parts = line_str.split("data:")
                    if len(parts) > 1:
                        try:
                            choices_data = parts[1]
                            json_data = json.loads(choices_data)
                            if "choices" in json_data and len(json_data["choices"]) > 0:
                                delta = json_data["choices"][0].get("delta", {})
                                content_data = delta.get("content", "")
                                if content_data:
                                    full_response += content_data
                        except json.JSONDecodeError:
                            my_log.error(f"无法解析截取后的流式响应: {choices_data}")
        return full_response

    def no_stream_chat_completion(self, content):
        """回源：非流式输出,返回响应数据"""
        uu_id = str(uuid.uuid4())
        payload = {}

        try:
            r = self.post(url=self.llm_url, headers=self.headers, json=payload)
            r.raise_for_status()  # 检查请求是否成功
            content_type = r.headers.get("Content-Type", "")
            full_response = r.json()["choices"][0]["message"]["content"]
            return content_type, full_response, uu_id
        except Exception as e:
            my_log.error(f"非流式请求发生错误: {e}")
            raise

    def file_chat(self, file_data, model=None):
        """
        文件请求
        """
        uu_id = str(uuid.uuid4())
        if not model:
            model = self.model

        file_type = file_data[1]
        if file_type in ["png", "jpg", "bmp", "tiff", "gif"]:
            payload = {}
        else:
            payload = {}


        r = self.post(url=self.llm_url, headers=self.headers, json=payload)
        if r.status_code == 200:
            content_type = r.headers.get("Content-Type", "")
            full_response = r.json()["choices"][0]["message"]["content"]
            return content_type, full_response, uu_id
        elif r.status_code == 400:
            return [uu_id]
        else:
            return None

    def chat_code(self, content, model=None, cookie=None, referer=None, agent=None, forwarded=None, uri=None, token=None):
        """回源：非流式输出,返回响应数据"""
        uu_id = str(uuid.uuid4())
        if not model:
            model = self.model
        payload = {}
        headers = self.headers.copy()
        if cookie:
            headers["Cookie"] = cookie
        if referer:
            headers["Referer"] = referer
        if agent:
            headers["User-Agent"] = agent
        if forwarded:
            headers["X-Forwarded-For"] = forwarded
        if token:
            headers["Authorization"] = f"Bearer {token}"
        if uri:
            uri = self.llm_url + uri
        else:
            uri = self.llm_url
        r = self.post(url=uri, headers=headers, json=payload)
        if r.status_code == 200:
            content_type = r.headers.get("Content-Type", "")
            full_response = r.json()["choices"][0]["message"]["content"]
            return content_type, full_response, uu_id
        elif r.status_code == 403 or r.status_code == 401:
            content_type = r.headers.get("Content-Type", "")
            full_response = r.text
            return content_type, full_response, uu_id
        else:
            pass

    def stream_chat_completion(self, content, model=None, agent=None, uri=None, redline=False):

        if not model:
            model = self.model
        if redline:
            uu_id = ''
        else:
            uu_id = str(uuid.uuid4())

        # 判断content是字符串还是列表，是列表，则用例是监测上下文，需特殊处理传参
        if type(content) == list:
            content[-1]["content"] = uu_id + content[-1]["content"]

            payload = { }
        else:
            payload = { }


        headers = self.headers.copy()
        if agent:
            headers["User-Agent"] = agent

        if uri:
            url = self.llm_url + uri
        else:
            url = self.llm_url

        try:
            r = self.post(url=url, headers=headers, json=payload)
            r.raise_for_status()
            content_type = r.headers.get("Content-Type", "")
            full_response = self._parse_sse_stream(r)
            return content_type, full_response, uu_id

        except Exception as e:
            my_log.error(f"流式请求发生错误: {e}")
            raise


    def stream_check_content(self, content, flag=False):
        """流式输出,监测上下文"""
        uu_id = str(uuid.uuid4())
        content[-1]["content"] = uu_id + content[-1]["content"]

        payload = {}
        try:
            r = self.post(url=self.llm_url, headers=self.headers, json=payload)
            r.raise_for_status()
            content_type = r.headers.get("Content-Type", "")
            full_response = self._parse_sse_stream(r)
            return content_type, full_response, uu_id

        except Exception as e:
            my_log.error(f"流式请求发生错误: {e}")
            raise

    def v1_check(self, api_route_id, content, agent=None, uri=None, bm=False):
        """api check检测"""
        if bm:
            uu_id = ''
        else:
            uu_id = str(uuid.uuid4())
        payload = {"messages": [{"content": uu_id+content}]}
        base_url = f"{Config().LLM_CHECK_URL}/{api_route_id[4:]}/v1/check"
        headers = self.headers.copy()
        headers["Authorization"] = f"Bearer {Config().LLM_CHECK_Authorization}"
        headers["Host"] = f"{Config().api_check_domain}.com"

        if agent:
            headers["User-Agent"] = agent

        if uri:
            url = base_url + uri
        else:
            url = base_url

        try:
            r = self.post(url=url, headers=headers, json=payload)
            r.raise_for_status()  # 检查请求是否成功
            full_response = r.json()
            return full_response, uu_id
        except Exception as e:
            my_log.error(f"v1 check请求发生错误: {e}")
            raise