def n_gram(n, sequence):
    n_list = []
    for i in range(len(sequence) - n + 1):
        n_list.append(sequence[i :i+n])
    return n_list

word_1 = 'paraparaparadise'
word_2 = 'paragraph'

x = set(n_gram(2, word_1))
y = set(n_gram(2, word_2))

# 和集合（合併、ユニオン）は|演算子またはunion()メソッド
n_union = x.union(y)
print(n_union)

# 積集合（共通部分、交差、インターセクション）は
# &演算子またはintersection()メソッド
n_intersection = x.intersection(y)
print(n_intersection)

# 差集合は-演算子またはdifference()
n_difference = x.difference(y)
print(n_difference)

# Check 'se'
# in 演算子は、Pythonで要素が特定の データ構造 に含まれているか
# リスト: list, 集合: set, 辞書: dict, 文字列: str
is_se_x = 'se' in x
is_se_y = 'se' in y

print(f'Is "se" in X?: {is_se_x}')
print(f'Is "se" in Y?: {is_se_y}')