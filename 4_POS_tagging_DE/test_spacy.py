import spacy
nlp = spacy.load("de_dep_news_trf")
#import de_dep_news_trf
#nlp = de_dep_news_trf.load()
doc = nlp("Dies ist ein Satz.")
print([(w.text, w.pos_, w.lemma_) for w in doc])