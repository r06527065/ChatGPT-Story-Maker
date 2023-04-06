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
