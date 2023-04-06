import requests
import json
import base64

gradio_url = ""
txt2img_url = f'{gradio_url}sdapi/v1/txt2img'


def submit_post(url: str, data: dict):
    return requests.post(url, data=json.dumps(data))


def save_encoded_image(b64_image: str, output_path: str):
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))


def make_photo(prompt):
    data = {'prompt': prompt, 'steps': 25}
    response = submit_post(txt2img_url, data)
    output_name = "pic.png"
    save_encoded_image(response.json()['images'][0], output_name)

    with open(output_name, "rb") as f:
        b64_image = base64.b64encode(f.read())

    return b64_image.decode()