import requests
import json
import base64

with open('setting.json', 'r', encoding="utf-8") as f:
  jdata = json.load(f)

stable_diffuison_url = jdata['stable_diffusion_ip']
txt2img_url = f'{stable_diffuison_url}sdapi/v1/txt2img'


def submit_post(url: str, data: dict):
    return requests.post(url, data=json.dumps(data))


def save_encoded_image(b64_image: str, output_path: str):
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))


def make_photo(prompt):
    positive_prompt = jdata["positive_prompt"]
    negative_prompt = jdata["negative_prompt"]
    data = {'prompt': f"{positive_prompt},{prompt}", 'steps': 20, 'width': 512, 'height': 512, "sampler_index": "DDIM", "negative_prompt": negative_prompt}
    response = submit_post(txt2img_url, data)
    output_name = "pic.png"
    save_encoded_image(response.json()['images'][0], output_name)

    with open(output_name, "rb") as f:
        b64_image = base64.b64encode(f.read())

    return b64_image.decode()