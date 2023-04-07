import requests
import json

with open('setting.json', 'r', encoding="utf-8") as f:
  jdata = json.load(f)

def chinese_to_english(chinese_text):
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'key': jdata['google_key'],
        'source': 'zh-TW',
        'target': 'en',
        'q': chinese_text
    }

    response = requests.get(url, params=params)
    json_data = response.json()
    translated_text_en = json_data['data']['translations'][0]['translatedText']

    with open("english_translate.txt", "w",encoding="utf-8") as f:
        f.write(translated_text_en)

    return(translated_text_en)
