'''
result = [] # 結果を格納
sentence = [] # 1文ごとの形態素リスト

with open("neko.txt.mecab", "r", encoding = "utf-8") as f:
    for line in f:
        line = line.strip() # 空白・改行を削除

        if line == "EOS":
            if sentence:
                result.append(sentence)
                sentence = []
            continue

        parts = line.split("\t")
        if len(parts) < 2: # "\t" で区切られていない行はスキップ
            continue

        surface = parts[0] # 表層系(surface): 元の単語
        features = parts[1].split(",")

        dic = {
            "surface": surface,
            "base": features[6], # 基本形
            "pos": features[0], # 品詞
            "pos1": features[1] # 品詞細分類1
        }

        result = sentence.append(dic)

for s in result[:2]:
    print(s)
'''

def parse_mecab(sentences):
    print("hello")

    result = []
    sentence = []

file_name = "neko.txt.mecab"
with open(file_name, "r") as f:
    sentences = f.readlines() # 全行をリストとして取得
    parse_mecab(sentences)


'''
ファイル読み込み
1行ずつ取ってくる。このとき、行の前後の空白・改行を削除

MeCab は 文の終わり に "EOS"(End of Sentence)を出力
1. line に "EOS" が入った場合、現在の文(sentence)が終わった ことを意味する。
2. これまでの sentence(1文分の形態素リスト)を result に追加。
3. sentence = [] で、次の文のためにリストをリセット。
4. continue で "EOS" の行自体はスキップ し、次の行の処理に移る。
'''
