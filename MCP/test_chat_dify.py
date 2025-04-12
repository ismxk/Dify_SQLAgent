import requests
import json

# Dify API配置
DIFY_API_KEY = xxx
DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"
#DIFY_API_URL = "https://api.dify.ai/v1/completion-messages"

def test_dify_api():
    """测试Dify API的访问"""
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": "",
        "query": "xxx",
        "user": "test_user",
        "response_mode": "streaming"
    }
    
    try:
        print("正在发送请求到Dify API...")
        response = requests.post(DIFY_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        print("API响应:")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
        # 从响应中获取answer字段的内容
        answer = result.get("answer", "无法获取回答")
            
        print("\nDify回答:")
        print(answer)
        
    except Exception as e:
        print(f"请求Dify API时出错: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"错误详情: {e.response.text}")

if __name__ == "__main__":
    test_dify_api() 


# 使用curl调用agent的api：
# C:\Users\maxk>curl -X POST "https://api.dify.ai/v1/chat-messages" -H "Authorization: Bearer xxx" -H "Content-Type: application/json" -d "{\"inputs\": \"\",\"query\": \"xxx\",\"user\": \"test_user\",\"response_mode\": \"streaming\"}"
