import spacy
nlp = spacy.load("de_dep_news_trf")

input_file = "rotkaeppchen.txt"
with open (input_file, "r", encoding = "utf-8") as f:
    sentences = f.read()
doc = nlp(sentences)

output_file = "rotkaeppchen_spacy.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for token in doc:
        f.write(f"{token.text}\t{token.pos_}\t{token.lemma_}\n")

print(f"解析結果を {output_file} に保存しました。")        