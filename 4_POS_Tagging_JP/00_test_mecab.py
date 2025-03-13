import MeCab

m = MeCab.Tagger("-r /etc/mecabrc")
text = "吾輩は猫である"
print(m.parse(text))
