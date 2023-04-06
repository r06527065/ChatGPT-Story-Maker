import openai

openai.api_key = ""

def chatGPT(prompt):

    conversation = [{"role": "user", "content": f'幫我生成一個50字以內的故事,包含{prompt},限制50個字以內'}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        max_tokens=400,
        temperature=0.8,
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    answer = response['choices'][0]['message']['content']

    print(answer)

    return answer
