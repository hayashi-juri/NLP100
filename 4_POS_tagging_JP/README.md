# Mecab
日本語解析ツール。
AIなどが日本語などの言語を機械的に処理するために使う。
Python, R, C, Java などに対応

# 形態素解析
形態素：単語が意味を持つ最小の単位
→ 文章をできるだけ分解する

例）
吾輩は猫である
→ 吾輩/は/猫/で/ある

# 辞書
IPA辞書：最新ワードを含む
Undic：古語まで含む

# 基本コード
import Mecab
A = Mecab.Tagger() ←　()にpathが入ることもある：Mecab.Tagger("-r /etc/mecabrc")
text = "xxxxxxxxxx"
result = A.parse(text)

<https://nlp100.github.io/ja/ch04.html>