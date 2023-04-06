import requests


def chinese_to_english(chinese_text):
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'key': 'AIzaSyAnKfxCOh9j_FZkSXicbJAUTmOy3nMbkT8',
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


def chinese_to_japanese(chinese_text):
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'key': 'AIzaSyAnKfxCOh9j_FZkSXicbJAUTmOy3nMbkT8',
        'source': 'zh-TW',
        'target': 'ja',
        'q': chinese_text
    }

    response = requests.get(url, params=params)
    json_data = response.json()
    translated_text_jp = json_data['data']['translations'][0]['translatedText']

    with open("japan_translate.txt", "w",encoding="utf-8") as f:
        f.write(translated_text_jp)

    return(translated_text_jp)
