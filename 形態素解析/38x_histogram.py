""" 38. ヒストグラム
単語の出現頻度のヒストグラムを描け
ただし
- 横軸は出現頻度
- 1から単語の出現頻度の最大値までの線形目盛

縦軸はx軸で示される出現頻度となった単語の異なり数(種類数)である
"""

import module_frq as frq
import matplotlib.pylab as plt
import matplotlib.font_manager as fm

# インストールされた IPAex フォントのパスを確認
font_path = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
# フォントプロパティを設定
font_prop = fm.FontProperties(fname=font_path)
# フォントを `matplotlib` に適用
plt.rc('font', family=font_prop.get_name())

freqencies = [w[1] for w in frq.w_frequent]

plt.hist(freqencies, range = (1, 30)) # 階級（ヒストグラムの棒）の数
plt.xlabel("出現頻度")
plt.ylabel("種類数")
plt.title("ヒストグラム")
plt.grid(True)
plt.show()