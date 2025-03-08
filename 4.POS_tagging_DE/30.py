""" 30. 形態素解析結果の読み込み
- NE = 固有名詞 (例: Rotkäppchen, Grimm, Johanna, Marie)
- VAFIN = 活用動詞 (例: ist, steht, geht)
- ART = 冠詞 (例: ein, die)
- NN = 名詞 (例: Märchen, Hausmärchen, Brüder, Stelle)
- APPR = 前置詞 (例: in, an, durch, über)
- KON = 接続詞 (例: und)
- ADJA = 形容詞 (例: mündliche)
- CARD = 数詞 (例: 26)

をキーとするマッピング型に格納し，
1文を形態素(マッピング型)のリストとして表現せよ.
"""

filename = "rotkaeppchen_treetagger.txt"
result = []
sentence = []
sentence_end = {".", "!", "?"}

with open (filename, "r", encoding = "utf-8") as f:
    sentences = f.readlines()

    for line in sentences:
        dic = {}
        parts = line.strip().split("\t")
        if len(parts) < 3: # 不正な行をスキップ
            continue


        surface, pos, base = parts[0], parts[1], parts[2]

        dic = {
            "surface": surface,
            "base": base, # 基本形
            "pos": pos # 品詞
        }

        sentence.append(dic)

        if surface in sentence_end:
            result.append(sentence) # 文全体を `result` に追加
            sentence = [] # 新しい文のためにリセット

print(f"文の総数: {len(result)}")
print(result[:2])