def cipher(text):
    tmp = [] # 変換した文字を格納
    for c in text:
        if c.islower():
            tmp_c = chr(219 -ord(c))
            # tmp_ord = 219 - ord(c)
            # tmp_c = chr(tmp_ord)
            tmp.append(tmp_c) # list.append(): リストの後に要素を加える
        else:
            tmp.append(c) # list.append(): リストの後に要素を加える
    tmp_str = "".join(tmp) # 間に何も入れず連結
    return tmp_str

''' リスト(list)の要素を連結して一つの文字列(str)に変換
【サンプルコード】
color_list = ["red", "green", "blue"]
color_string = ", ".join(color_list)
print(color_string)

【実行結果】
red, green, blue
リストcolor_listの各要素を「, 」（カンマとスペース）で連結
'''

text_gen_c = cipher("the quick brown fox jumps over the lazy dog")
print(text_gen_c)

text_gen_d = cipher(text_gen_c)
print(text_gen_d)
