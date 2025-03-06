import requests

URL = "https://de.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Rotkäppchen",
    "prop": "extracts",
    "explaintext": True  # HTMLタグを除去してプレーンテキストで取得
}

# APIリクエストを送信
response = requests.get(url = URL, params = PARAMS)

# レスポンスのJSONデータを解析
data = response.json()

# ページのテキスト抽出
page = next(iter(data['query']['pages'].values()))
extract = page.get('extract', 'テキストが見つかりませんでした。')

# テキストデータをファイルに書き込む
with open('rotkaeppchen.txt', 'w', encoding='utf-8') as file:
    file.write(extract)

# 結果を表示
print(extract)