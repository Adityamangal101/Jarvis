from openai import OpenAI

def Ai_response(command):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="api_key",
    )
    completion = client.chat.completions.create(
    
    model="deepseek/deepseek-r1-0528:free",
    messages=[
        {
        "role": "system",
        "content": "you are a virtual assistant named Jarvis who is skilled in general tasks like Alexa and google cloud"
        },
        {
        "role": "user",
        "content": command
        }
    ]
    )
    print(completion.choices[0].message.content)

    return completion.choices[0].message.content
