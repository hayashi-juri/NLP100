text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics'
# str.relpace(): 文字列の変換・削除
# str.split(): 文字列を空白で分割
words_list = text.replace(',','').split()

num_list = []
for word in words_list:
    # list.append(): リストの後に要素を加える
    num_list.append(len(word))

print(num_list)


