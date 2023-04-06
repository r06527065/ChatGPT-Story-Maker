# from flask import Flask, render_template, request
# import requests
# import json
# import base64
# import os
# import openai
# from googletranslate import *
#
#
# app = Flask(__name__)
#
# openai.api_key = "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"
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         text = request.form['text']
#         text_data = chatGPT(text)
#         image_data = make_photo(chinese_to_english(text_data))
#         return render_template('index.html', image_data=image_data, text_data=text_data)
#     else:
#         return render_template('index.html')
#
#
# def chatGPT(message):
#
#     conversation = [{"role": "user", "content": message}]
#
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=conversation,
#         max_tokens=1000,
#     )
#
#     conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
#     answer = response['choices'][0]['message']['content']
#
#     return answer
#
#
# gradio_url = "https://f8d894e0fe78c70fe6.gradio.live/"
# txt2img_url = f'{gradio_url}sdapi/v1/txt2img'
#
#
# def submit_post(url: str, data: dict):
#     return requests.post(url, data=json.dumps(data))
#
#
# def save_encoded_image(b64_image: str, output_path: str):
#     with open(output_path, "wb") as image_file:
#         image_file.write(base64.b64decode(b64_image))
#
#
# def make_photo(prompt):
#     data = {'prompt': prompt, 'steps': 25}
#     response = submit_post(txt2img_url, data)
#     output_name = "pic.png"
#     save_encoded_image(response.json()['images'][0], output_name)
#
#     with open(output_name, "rb") as f:
#         b64_image = base64.b64encode(f.read())
#
#     return b64_image.decode()
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
from stable_diffusion import *
from gpt import *
from googletranslate import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        text_data = chatGPT(text)
        image_data = make_photo(chinese_to_english(text_data))
        return render_template('index.html', image_data=image_data, text_data=text_data)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
