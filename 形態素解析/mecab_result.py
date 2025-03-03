""" 30. 形態素解析結果の読み込み
形態素解析結果(neko.txt.mecab)を読み込むプログラムを実装せよ.
ただし，各形態素は
- 表層形(surface)
- 基本形(base)
- 品詞(pos)
- 品詞細分類1(pos1)
をキーとするマッピング型に格納し，
1文を形態素(マッピング型)のリストとして表現せよ.

第4章の残りの問題では,ここで作ったプログラムを活用せよ.
"""

file_name = "neko.txt.mecab"
result = [] # 結果を格納するリスト
sentence = [] # 1文ごとの形態素リスト

with open(file_name, "r", encoding="utf-8") as f:
    sentences = f.readlines() # 行ごとにリストとして取得

    for line in sentences:
        dic = {}
        parts = line.split("\t")
        if parts[0] == "EOS\n": # EOS\n を発見したらスキップする
            continue # EOS は、形態素解析の出力で「文の終わり」を示す特殊な記号
        surface = parts[0] # 表層系(surface): 元の単語

        features = parts[1].split(",")

        dic = {
            "surface": surface,
            "base": features[6], # 基本形
            "pos": features[0], # 品詞
            "pos1": features[1] # 品詞細分類1
        }

        sentence.append(dic)
        if surface == "。":
            result.append(sentence) # 文全体を `result` に追加
            sentence = [] # 新しい文のためにリセット

# print(f"文の総数: {len(result)}")
# print(result[:2])
result

'''
ファイル読み込み
1行ずつ取ってくる。このとき、行の前後の空白・改行を削除

MeCab は 文の終わり に "EOS"(End of Sentence)を出力
1. line に "EOS" が入った場合、現在の文(sentence)が終わった ことを意味する。
2. これまでの sentence(1文分の形態素リスト)を result に追加。
3. sentence = [] で、次の文のためにリストをリセット。
4. continue で "EOS" の行自体はスキップ し、次の行の処理に移る。
'''
