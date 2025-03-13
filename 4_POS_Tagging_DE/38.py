""" 38.Histogram
Draw a histogram of word frequency
- x-axis is a scalar range representing a frequency ranging from 1 to the largest frequency
of a given word in the entire corpus
- y-axis is the count of unique words that fall into the count of the x value
>>>出現頻度ごとの単語の種類
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

frq_num = [w[1] for w in frq.w_frq] 
# 出現頻度のグラフを作る

##print(frq.w_frq)
##print(frqency)

plt.hist(frq_num, range(1, 30)) 
plt.xlabel("出現頻度")
plt.ylabel("種類数")
plt.title("ヒストグラム")
plt.grid(True)
plt.show()


