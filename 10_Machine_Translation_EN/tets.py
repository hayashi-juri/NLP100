from transformers import MarianMTModel, MarianTokenizer

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# ドイツ語から英語への翻訳を行う場合のモデル名
model_name = "Helsinki-NLP/opus-mt-de-en"

# モデルとトークナイザーの読み込み
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# 翻訳するドイツ語の文
text = "Wie geht es dir?"

# テキストをトークナイズ
translated = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt")

# 翻訳の実行
translated_text = model.generate(**translated)

# 翻訳結果をデコード
translated_text = tokenizer.decode(translated_text[0], skip_special_tokens=True)

# 結果の表示
print(translated_text)
