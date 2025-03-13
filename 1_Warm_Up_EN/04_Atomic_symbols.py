text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'
# split the sentence into words
words_list = text.replace('.', '').split()

# extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words
dic = {}
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
# extract the first two letters from the other words

# 関数 enumerate(): 何番目かと中身を取得
for i, word in enumerate(words_list):
    if i+1 in num:
        temp = word[0] # wordの0番目: 最初の1文字
    else:
        temp = word[:2] # wordの0番目から2文字目まで
    dic[temp] = i+1

print(dic)

# 辞書は キー (key) と 値 (value) をセットで管理するデータ構造 
# dic["H"] = 1  : "H" をキー、1 を値として辞書に追加
# i は 0 から始まるインデックス
# i + 1 は 単語の位置（1から始まる数)