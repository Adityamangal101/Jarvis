from openai import OpenAI

def Ai_response(command):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
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