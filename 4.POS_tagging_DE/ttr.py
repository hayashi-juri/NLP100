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
result