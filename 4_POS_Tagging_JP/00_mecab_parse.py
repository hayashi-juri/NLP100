import MeCab

with open("neko.txt", "r", encoding = "utf-8") as f:
    text = f.read()

m = MeCab.Tagger("-r /etc/mecabrc")
gen_text = m.parse(text)

with open("neko.txt.mecab", "w", encoding = "utf-8") as f:
    f.write(gen_text)

print("形態素解析をファイルに保存")