""" 33. AのB
2つの名詞が「の」で連結されている名詞句を抽出せよ
"""
import gen_morphs

noun_von = set()
# if A von B, add the set
tmp = ""
for morphs in gen_morphs.result: # 形態素解析した文
    for i in range(1, len(morphs)-1):
        # (det) A von (det) B
        if (morphs[i]["surface"] == "von" and morphs[i]["pos"] == "ADP"
            and (morphs[i-1]["pos"] == "NOUN") or ( morphs[i-1]["pos"] == "DET" and morphs[i-2]["pos"] == "NOUN")
            and (morphs[i+1]["pos"] == "NOUN") or ( morphs[i+1]["pos"] == "DET" and morphs[i+2]["pos"] == "NOUN")):

            tmp = morphs[i-2]["surface"] + " " + morphs[i-1]["surface"] + " von " + morphs[i + 1]["surface"] + morphs[i-2]["surface"]

            noun_von.add(tmp)


print('A von B （所有）の出現数: {}'.format(len(noun_von)))
print('===10個表示===')
for v in list(noun_von)[:10]:
    print(v)