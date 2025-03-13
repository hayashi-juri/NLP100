import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind"

words = text.split() # list

text_gen = []
for w in words:
    if len(w) < 5: # <= 4
        text_gen.append(w)
    else:
        first = w[0] # 最初の文字
        last = w[-1] # 最後の文字

        # 中間の文字をリストにしてシャッフル
        middle = list(w[1:-1])
        random.shuffle(middle)

        # middle をリストから文字列にする
        tmp_w = first + "".join(middle) + last
        text_gen.append(tmp_w)

print(" ".join(text_gen))

''' 末尾からn文字
末尾から1文字の場合、負のインデックス表記が有効である。
Pythonでは、インデックスに負の値を指定した場合、
後方から数えた要素を取得する
'''