import openai
import json

with open('setting.json', 'r', encoding="utf-8") as f:
  jdata = json.load(f)

openai.api_key = jdata['openai_key']

conversation = []

def chatGPT(prompt):
    global conversation
    conversation = [{"role": "user", "content": f'幫我生成一個100字以內的{prompt}故事,限制100個字以內,並提供我選項1,2,3讓我能接下去選擇故事的劇情,大約讓我選擇三次就讓故事結束.具體格式如下:\n故事:\n選項:\n選項1\n選項2\n選項3'}]
    print(conversation)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=500,
        temperature=0.8,
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    answer = response['choices'][0]['message']['content']
    story = answer.split("選項:")[0]
    print(answer)

    answer = answer.replace('\n', '<br>')

    return answer,story

def next_story(number):
    global conversation
    conversation.append({"role": "user", "content": number})
    print(conversation)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=500,
        temperature=0.8,
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    answer = response['choices'][0]['message']['content']
    story = answer.split("選項")[0]

    print(answer)

    answer = answer.replace('\n', '<br>')

    return answer,story
