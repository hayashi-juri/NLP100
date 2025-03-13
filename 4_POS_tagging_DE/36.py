""" 36. Top-ten frequent words
Visualize the top-ten frequent words 
and their frequencies with a chart (e.g., bar chart).
"""

import frq
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# インストールされた IPAex フォントのパスを確認
font_path = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
# フォントプロパティを設定
font_prop = fm.FontProperties(fname=font_path)
# フォントを `matplotlib` に適用
plt.rc('font', family=font_prop.get_name())

top_10 = frq.w_frq[:10]
w_10 = [w[0] for w in top_10]
c_10 = [w[1] for w in top_10]

plt.bar(w_10, c_10)
plt.xlabel("頻出単語")
plt.ylabel("出現頻度")
plt.title('頻出上位10語')  # タイトル
plt.xticks(rotation=45)  # X軸ラベルを45度回転して見やすくする
plt.show()

top_10_v = frq.w_frq_v[:10]
v_10_w = [w[0] for w in top_10_v]
v_10_c = [i[1] for i in top_10_v]

plt.bar(v_10_w, v_10_c)
plt.title("Verb Top 10")
plt.show()

top_10_n = frq.w_frq_n[:10]
n_10_w = [w[0] for w in top_10_n]
n_10_c = [i[1] for i in top_10_n]

plt.bar(n_10_w, n_10_c)
plt.title("Noun Top 10")
plt.show()
