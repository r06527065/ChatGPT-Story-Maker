import openai

openai.api_key = ""

def chatGPT(prompt):

    conversation = [{"role": "user", "content": f'幫我生成一個100字以內的故事,包含{prompt}'}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=200,
        temperature=1,
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    answer = response['choices'][0]['message']['content']

    print(answer)

    return answer
