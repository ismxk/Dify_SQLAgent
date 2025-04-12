import subprocess

# Dify API配置
DIFY_API_KEY = xxx
DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"

def test_dify_api(prompt: str) -> str:
    """使用curl发送请求"""
    # 构造 curl 命令
    curl_command = [
        "curl", "-X", "POST", DIFY_API_URL,
        "-H", f"Authorization: Bearer {DIFY_API_KEY}",
        "-H", "Content-Type: application/json",
        "-d", f'{{"inputs": "", "query": "{prompt}", "user": "test_user", "response_mode": "streaming"}}'
    ]
    
    try:
        # 使用 subprocess 运行 curl 命令
        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        
        # 打印命令输出
        print("API响应:")
        print(result.stdout)
        print("成功输出响应")
        
    except subprocess.CalledProcessError as e:
        print(f"请求 Dify API 时出错: {str(e)}")
        print(f"错误输出: {e.stderr}")

if __name__ == "__main__":
    test_dify_api("xxx")
