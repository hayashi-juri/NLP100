'''
    n-gram

    任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法
    nが1の場合をユニグラム: uni-gram
    2の場合をバイグラム: bi-gram
    3の場合をトライグラム: tri-gram
'''

def n_gram(n, sequecne):
    n_list = []
    for i in range(len(sequecne) - n + 1):
        n_list.append(sequecne[i : i+n]) # [start:end]
    return n_list

text = 'I am an NLPer'
words = text.split()
word_bi_gram = n_gram(2, words)
print("Word bi-gram", word_bi_gram)

letters = text.replace(' ', '')
letter_bi_gram = n_gram(2, letters)
print("Letter bi-gram", letter_bi_gram)



