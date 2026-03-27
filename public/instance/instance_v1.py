import requests
from seldom.request import HttpRequest
from seldom.utils import cache

from config.config import Config
from public.login import Login


class Instance(HttpRequest):

    def __init__(self, cookie):
        self.cookie = cookie
        self.headers = {'Cookie': self.cookie}
        self.url = Config().URL

    def set_api_check(self, api_check_id, api_route_id, flag=True):
        """
        api-check 安全配置:
        flag=True: 开启安全配置, 默认开启安全配置
        flag=False: 关闭安全配置"""
        if flag:
            data = {
            "pluginConfigs": [
                {
                    "configurations": {
                        "strategySwitch": [],
                        "enable": True,
                        "enableObserve": True
                    },
                    "createdAt": "2026-01-23T12:03:41.065Z",
                    "internal": False,
                    "pluginName": "ks-waf",
                    "pluginVersion": "1.0.0",
                    "scope": "ROUTE",
                    "target": f"ai-route-{api_route_id}.internal",
                    "targets": {
                        "ROUTE": f"ai-route-{api_route_id}.internal"
                    },
                    "type": "enhanceManage",
                    "updatedAt": "2026-01-23T12:03:41.065Z"
                },
                {
                    "configurations": {
                        "keyword": {
                            "checkContext": False,
                            "checkRequest": True,
                            "checkResponse": True,
                            "keywordFilter": [
                                {
                                    "category": "fandong",
                                    "useBuiltin": True,
                                    "action": "detect",
                                    "useCustom": False
                                },
                                {
                                    "category": "shehei",
                                    "useBuiltin": True,
                                    "action": "detect",
                                    "useCustom": False
                                },
                                {
                                    "category": "shehuang",
                                    "useBuiltin": True,
                                    "action": "detect",
                                    "useCustom": False
                                },
                                {
                                    "category": "baokong",
                                    "useBuiltin": True,
                                    "action": "detect",
                                    "useCustom": False
                                },
                                {
                                    "category": "bocai",
                                    "useBuiltin": True,
                                    "action": "detect",
                                    "useCustom": False
                                },
                                {
                                    "category": "minsheng",
                                    "useBuiltin": True,
                                    "action": "detect",
                                    "useCustom": False
                                },
                                {
                                    "category": "zhengzhi",
                                    "useBuiltin": True,
                                    "action": "detect",
                                    "useCustom": False
                                },
                                {
                                    "category": "qita",
                                    "useBuiltin": True,
                                    "action": "detect",
                                    "useCustom": False
                                }
                            ]
                        },
                        "maskingData": {
                            "maskingDataFilter": [
                                {
                                    "category": "idcard",
                                    "action": "detect"
                                },
                                {
                                    "category": "mobile",
                                    "action": "detect"
                                },
                                {
                                    "category": "bankcard",
                                    "action": "detect"
                                },
                                {
                                    "category": "email",
                                    "action": "detect"
                                }
                            ],
                            "systemKeywordAction": "detect"
                        },
                        "enable": False
                    },
                    "createdAt": "2026-01-23T11:53:45.103Z",
                    "enabled": True,
                    "internal": False,
                    "pluginName": "ks-keyword-guard",
                    "pluginVersion": "1.0.0",
                    "scope": "ROUTE",
                    "target": f"ai-route-{api_route_id}.internal",
                    "targets": {
                        "ROUTE": f"ai-route-{api_route_id}.internal"
                    },
                    "updatedAt": "2026-01-23T12:03:43.176Z",
                    "version": None,
                    "type": "enhanceManage"
                },
                {
                    "configurations": {
                        "modelFilter": [
                            {
                                "label": "政治敏感",
                                "action": "detect",
                                "mode": "strict"
                            },
                            {
                                "label": "暴力恐怖",
                                "action": "detect",
                                "mode": "strict"
                            },
                            {
                                "label": "色情低俗",
                                "action": "detect",
                                "mode": "strict"
                            },
                            {
                                "label": "歧视谩骂",
                                "action": "detect",
                                "mode": "strict"
                            },
                            {
                                "label": "不良价值观",
                                "action": "detect",
                                "mode": "strict"
                            }
                        ],
                        "checkRequest": True,
                        "checkResponse": True,
                        "enable": False
                    },
                    "createdAt": "2026-01-23T11:53:45.034Z",
                    "enabled": True,
                    "internal": False,
                    "pluginName": "ks-model-guard",
                    "pluginVersion": "1.0.0",
                    "scope": "ROUTE",
                    "target": f"ai-route-{api_route_id}.internal",
                    "targets": {
                        "ROUTE": f"ai-route-{api_route_id}.internal"
                    },
                    "updatedAt": "2026-01-23T12:03:44.474Z",
                    "version": None,
                    "type": "enhanceManage"
                },
                {
                    "configurations": {
                        "promptConfig": [
                            {
                                "category": "prompt_injection",
                                "action": "detect",
                                "strategySwitch": []
                            },
                            {
                                "category": "jailbreak",
                                "action": "detect",
                                "strategySwitch": []
                            }
                        ],
                        "enable": False
                    },
                    "createdAt": "2026-01-23T11:53:44.975Z",
                    "enabled": True,
                    "internal": False,
                    "pluginName": "ks-prompt-guard",
                    "pluginVersion": "1.0.0",
                    "scope": "ROUTE",
                    "target": f"ai-route-{api_route_id}.internal",
                    "targets": {
                        "ROUTE": f"ai-route-{api_route_id}.internal"
                    },
                    "updatedAt": "2026-01-23T12:03:45.788Z",
                    "type": "enhanceManage"
                },
                {
                    "configurations": {
                        "checkRequest": True,
                        "checkResponse": True,
                        "enable": True,
                        "includedFileTypes": [
                            "html",
                            "rtf",
                            "txt",
                            "pdf",
                            "doc",
                            "docx",
                            "xls",
                            "xlsx",
                            "ppt",
                            "pptx",
                            "ofd",
                            "wps",
                            "et",
                            "dps",
                            "wps_ooxml",
                            "png",
                            "jpg",
                            "bmp",
                            "tiff",
                            "gif",
                            "zip",
                            "rar",
                            "7z",
                            "gz",
                            "bz2",
                            "tar",
                            "iso",
                            "unknown"
                        ]
                    },
                    "createdAt": "2026-01-23T11:53:43.550Z",
                    "enabled": True,
                    "internal": False,
                    "pluginName": "ks-bm-guard",
                    "pluginVersion": "1.0.0",
                    "scope": "ROUTE",
                    "target": f"ai-route-{api_route_id}.internal",
                    "targets": {
                        "ROUTE": f"ai-route-{api_route_id}.internal"
                    },
                    "type": "enhanceManage",
                    "updatedAt": "2026-01-23T12:03:47.080Z"
                }
            ]
        }
        else:
            data = {
                "pluginConfigs": [
                    {
                        "configurations": {
                            "strategySwitch": [],
                            "enable": False,
                            "enableObserve": False
                        },
                        "createdAt": "2026-02-04T10:27:28.201Z",
                        "internal": False,
                        "pluginName": "ks-waf",
                        "pluginVersion": "1.0.0",
                        "scope": "ROUTE",
                        "target": f"ai-route-{api_route_id}.internal",
                        "targets": {
                            "ROUTE": f"ai-route-{api_route_id}.internal"
                        },
                        "type": "enhanceManage",
                        "updatedAt": "2026-02-12T03:05:31.467Z"
                    },
                    {
                        "configurations": {
                            "keyword": {
                                "checkContext": False,
                                "checkRequest": True,
                                "checkResponse": True,
                                "keywordFilter": [
                                    {
                                        "category": "fandong",
                                        "useBuiltin": True,
                                        "action": "off",
                                        "useCustom": False
                                    },
                                    {
                                        "category": "shehei",
                                        "useBuiltin": True,
                                        "action": "off",
                                        "useCustom": False
                                    },
                                    {
                                        "category": "shehuang",
                                        "useBuiltin": True,
                                        "action": "off",
                                        "useCustom": False
                                    },
                                    {
                                        "category": "baokong",
                                        "useBuiltin": True,
                                        "action": "off",
                                        "useCustom": False
                                    },
                                    {
                                        "category": "bocai",
                                        "useBuiltin": True,
                                        "action": "off",
                                        "useCustom": False
                                    },
                                    {
                                        "category": "minsheng",
                                        "useBuiltin": True,
                                        "action": "off",
                                        "useCustom": False
                                    },
                                    {
                                        "category": "zhengzhi",
                                        "useBuiltin": True,
                                        "action": "off",
                                        "useCustom": False
                                    },
                                    {
                                        "category": "qita",
                                        "useBuiltin": True,
                                        "action": "off",
                                        "useCustom": False
                                    }
                                ]
                            },
                            "maskingData": {
                                "maskingDataFilter": [
                                    {
                                        "category": "idcard",
                                        "action": "off"
                                    },
                                    {
                                        "category": "mobile",
                                        "action": "off"
                                    },
                                    {
                                        "category": "bankcard",
                                        "action": "off"
                                    },
                                    {
                                        "category": "email",
                                        "action": "off"
                                    }
                                ],
                                "systemKeywordAction": "off"
                            },
                            "enable": False
                        },
                        "createdAt": "2026-02-04T10:27:26.360Z",
                        "enabled": True,
                        "internal": False,
                        "pluginName": "ks-keyword-guard",
                        "pluginVersion": "1.0.0",
                        "scope": "ROUTE",
                        "target": f"ai-route-{api_route_id}.internal",
                        "targets": {
                            "ROUTE": f"ai-route-{api_route_id}.internal"
                        },
                        "updatedAt": "2026-02-12T03:05:32.189Z",
                        "version": None,
                        "type": "enhanceManage"
                    },
                    {
                        "configurations": {
                            "modelFilter": [
                                {
                                    "label": "政治敏感",
                                    "action": "off",
                                    "mode": "strict"
                                },
                                {
                                    "label": "暴力恐怖",
                                    "action": "off",
                                    "mode": "strict"
                                },
                                {
                                    "label": "色情低俗",
                                    "action": "off",
                                    "mode": "strict"
                                },
                                {
                                    "label": "歧视谩骂",
                                    "action": "off",
                                    "mode": "strict"
                                },
                                {
                                    "label": "不良价值观",
                                    "action": "off",
                                    "mode": "strict"
                                }
                            ],
                            "checkRequest": True,
                            "checkResponse": True,
                            "enable": False
                        },
                        "createdAt": "2026-02-04T10:27:26.358Z",
                        "enabled": True,
                        "internal": False,
                        "pluginName": "ks-model-guard",
                        "pluginVersion": "1.0.0",
                        "scope": "ROUTE",
                        "target": f"ai-route-{api_route_id}.internal",
                        "targets": {
                            "ROUTE": f"ai-route-{api_route_id}.internal"
                        },
                        "updatedAt": "2026-02-12T03:05:32.888Z",
                        "version": None,
                        "type": "enhanceManage"
                    },
                    {
                        "configurations": {
                            "promptConfig": [
                                {
                                    "category": "prompt_injection",
                                    "action": "detect",
                                    "strategySwitch": [
                                        "prompt_leakage",
                                        "prompt_override",
                                        "structural_obfuscation",
                                        "token_smuggling",
                                        "common_injection_words",
                                        "template_injection"
                                    ]
                                },
                                {
                                    "category": "jailbreak",
                                    "action": "detect",
                                    "strategySwitch": [
                                        "role_playing",
                                        "jailbreak_frameworks",
                                        "virtual_scenarios",
                                        "ethical_bypass",
                                        "common_jailbreak_words",
                                        "dichotomous_prompting",
                                        "llm_guidance",
                                        "obfuscated_tasks"
                                    ]
                                }
                            ],
                            "enable": False
                        },
                        "createdAt": "2026-02-04T10:27:26.393Z",
                        "enabled": True,
                        "internal": False,
                        "pluginName": "ks-prompt-guard",
                        "pluginVersion": "1.0.0",
                        "scope": "ROUTE",
                        "target": f"ai-route-{api_route_id}.internal",
                        "targets": {
                            "ROUTE": f"ai-route-{api_route_id}.internal"
                        },
                        "updatedAt": "2026-02-12T03:05:33.577Z",
                        "type": "enhanceManage"
                    },
                    {
                        "configurations": {
                            "checkRequest": True,
                            "checkResponse": True,
                            "enable": False,
                            "includedFileTypes": []
                        },
                        "createdAt": "2026-02-04T10:27:25.705Z",
                        "enabled": True,
                        "internal": False,
                        "pluginName": "ks-bm-guard",
                        "pluginVersion": "1.0.0",
                        "scope": "ROUTE",
                        "target": f"ai-route-{api_route_id}.internal",
                        "targets": {
                            "ROUTE": f"ai-route-{api_route_id}.internal"
                        },
                        "type": "enhanceManage",
                        "updatedAt": "2026-02-12T03:05:34.271Z"
                    }
                ]
            }
        url = f"{self.url}/api/apiKey/updatePluginConfigs?_id={api_check_id}"
        try:
            r = self.put(url, headers=self.headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            raise Exception("插件配置发生错误: %s" % e)

    def search_api_check(self):
        """通过实例名称查询API keys"""
        url = f"{self.url}/api/apiKey"
        params = {
            "page": 1,
            "pageSize": 1000
        }
        r = self.get(url, headers=self.headers, params=params, verify=False)
        if r.status_code == 401:
            cache.clear("cookie")
            new_cookie = Login().login()
            r = self.get(url, headers={'Cookie': new_cookie}, params=params, verify=False)
            r.raise_for_status()  # 检查请求是否成功
        v1_list = r.json()['data']['list']
        for i in v1_list:
            if Config.api_check_name == i["name"]:
                api_check_id = i["_id"]
                api_route_id = i["route_id"]
                return api_check_id, api_route_id
        return None, None


