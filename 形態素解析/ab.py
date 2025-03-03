""" 33. AのB
2つの名詞が「の」で連結されている名詞句を抽出せよ
"""
import mecab_result as m

noun_n = set()

# "の"　の前後が名詞だったらセットに加える
for morphs in m.result:
    for i in range(1, len(morphs) - 1):
        if morphs[i]["surface"] == "の" and morphs[i-1]["pos"] == "名詞" and morphs[i+1]["pos"] == "名詞":
            tmp = morphs[i-1]["surface"] + "の" + morphs[i+1]["surface"]
            noun_n.add(tmp)

print('AのB: {}'.format(len(noun_n)))
print('===10個表示===')
for nn in list(noun_n)[:10]:
    print(nn)