# ペアノ曲線による一筆書き

## 理論的背景

ペアノ曲線とは、平面を充填する曲線の一種である。
詳しくはWikipediaの[該当ページ](https://ja.wikipedia.org/wiki/%E3%83%9A%E3%82%A2%E3%83%8E%E6%9B%B2%E7%B7%9A)
を読んでいただければわかるであろう。

さて、ペアノ曲線は手で描ける曲線の極限として定義される。
このような抽象的な議論に慣れていない方もいるかもしれないが、
現代数学においてこのような構成法に出会ったとき、
多くの場合「この手法によって任意の精度が実現できる」
というように読み替えられることが多い。

例えば、点列の極限についてこう読み替えれば、通常のN-δ論法になる。

ただしこの読み替えは必ずしも簡単ではない。
実際、ペアノ曲線の主張を正確にこう読み替えるのは難しい。
この難しさの理由は、ペアノ曲線の定義が、
「空間は大きさのない点の集合として成り立っている」という点集合論
に依拠しており、
実はこれがそんなに理解のしやすいものではないということによると思われる。

点から空間を構成する古代ギリシャ以来の方法は「逆立ちしたやり方」であり、
むしろ点は「だんだん小さくなる領域の極限」として解釈すべきものなのではないか、
という見方は、例えば中世スコラ哲学においてもみられる。

現代数学において「pointless topology」などのジャンルでは、
点を基礎概念としない幾何が追求されている。

しかしペアノ曲線の非数学者でも扱いやすい読み替えを考えるのに、
そのような最先端の数学が必要となっては本末転倒だ。

そこで多少情報が落ちてもいい読み替えを探るように方針を転換する。
そうすれば、ペアノ曲線の構成法は、
「この手法によって、任意の長さ以上の一筆書きを正方形内部に収めることができる」
と読み替えることが可能なのだ。

点集合としての曲線や平面では、どこまで行っても曲線で埋められた平面の面積は0で、
極限において初めて0ではなくなってしまう。
しかし、現実世界の曲線においては、これは正方形の中にしめる黒の面積の割合がどんどん
大きくなっていることになる。

つまりペアノ曲線の理論を応用すれば、一筆書きによって任意の濃さのピクセルを表現することができるのだ。

今回は、これを応用して、任意の画像を一筆書きによって描く簡単なスクリプトを書いてみた。

## 仕組み

まず画像がカラーなら白黒にし、
そのピクセルの濃さを8段階に量子化する。

その濃さに合わせて、ペアノ曲線の構成法で線を描き、
ピクセル同士を繋いでいく。

コード自体は簡単なので、読めばわかると思う。

これは相当に単純な方法で行なっているので、
工夫すればもっといい方法が見つかるかもしれない。

## 動作例

サンプル画像のジョゼッぺ・ペアノの肖像（パブリックドメイン）

<img src="https://raw.githubusercontent.com/tannakaken/peanocurvestroke/master/Giuseppe_Peano.jpg" width="500">

を、このスクリプトの入力にすると、

`python main.py Gioseppe_Peano.jpg`

次の画像が生まれる。

<img src="https://raw.githubusercontent.com/tannakaken/peanocurvestroke/master/Giuseppe_Peano_peanocurved.sample.png" width="500">

一筆書きになっている様子は上の画像をクリックして拡大してみればわかるであろう。
