#!/usr/bin/env python3
"""
Simple OpenRouter integration test using requests library
"""

import requests
import json

# OpenRouter Configuration
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def test_horizon_beta():
    """Test Horizon Beta via OpenRouter using requests"""
    print("🚀 Testing Horizon Beta via OpenRouter...")
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "openrouter/horizon-beta",
        "messages": [
            {"role": "system", "content": "You are Horizon Beta, an elite assistant."},
            {"role": "user", "content": "Hello! Can you give me a brief overview of your capabilities?"}
        ],
        "temperature": 0.7
    }
    
    try:
        print("📤 Sending request to Horizon Beta...")
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            message = data['choices'][0]['message']['content']
            
            print("📥 Response from Horizon Beta:")
            print("=" * 50)
            print(message)
            print("=" * 50)
            print("✅ OpenRouter integration successful!")
            return True
        else:
            print(f"❌ Request failed with status code {response.status_code}")
            print(response.text)
            return False
            
    except Exception as e:
        print(f"❌ Error testing OpenRouter: {str(e)}")
        return False

def test_model_switching():
    """Test switching between different models"""
    print("\n🔄 Testing model switching...")
    
    models = {
        "horizon-beta": "openrouter/horizon-beta",
        "gpt-4": "openai/gpt-4",
        "claude": "anthropic/claude-3-5-sonnet"
    }
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    for model_name, model_id in models.items():
        try:
            print(f"\n🧪 Testing {model_name}...")
            
            payload = {
                "model": model_id,
                "messages": [
                    {"role": "user", "content": "Say hello in one sentence."}
                ],
                "temperature": 0.7
            }
            
            response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                message = data['choices'][0]['message']['content']
                print(f"✅ {model_name}: {message}")
            else:
                print(f"❌ {model_name}: Status {response.status_code}")
                
        except Exception as e:
            print(f"❌ {model_name}: {str(e)}")

if __name__ == "__main__":
    print("🤖 Simple OpenRouter Integration Test")
    print("=" * 50)
    
    # Test Horizon Beta
    success = test_horizon_beta()
    
    if success:
        # Test other models
        test_model_switching()
    
    print("\n🎉 Test completed!") 