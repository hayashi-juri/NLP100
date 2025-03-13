def template(x, y, z):
    text = str(x) + " is " + str(z) + " at " + str(y)
    return text

text_gen = template(12, "tempareture", 22.4)
print(text_gen)

# f-string(フォーマット済み文字列リテラル)
# 文字列の中に変数や式を直接埋め込める
# print(f"{y} is {z} at {x}")