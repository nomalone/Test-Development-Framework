
import socket


def get_local_ip():
    try:
        # 连接到外部服务器（不实际发送数据）
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as e:
        return f"获取失败：{str(e)}"


if __name__ == "__main__":
    ip = get_local_ip()
    print(f"对外通信的本地IP：{ip}")
