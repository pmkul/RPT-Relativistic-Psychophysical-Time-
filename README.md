# RPT — Relativistic Psychophysical Time

> 相対論の**固有時間 τ**と、人間の**体感レート Λ(z)**を掛け合わせて**主観時間 T**を定義する最小モデル。

## Formula
`dT = Λ(z(t)) · dτ`, with `Λ = 1 + α·I + β·C + γ·A`.

- `τ`: proper time from relativity (SR/weak-field GR)
- `I`: surprise (prediction error), `C`: cognitive load, `A`: arousal
- `α, β, γ`: individual coefficients (estimated from data)

## Install (local)
```bash
pip install -e .
```

## Quickstart
```python
from rpt import rpt_model
T, tau, Lambda = rpt_model.run_demo()  # returns numpy arrays
```

Or open `notebooks/RPT_demo.ipynb`.

## Data
- `data/RPT_simulated_data.csv` — simulated example
- `data/RPT_blank_template.csv` — fill with your logs (t, v, Φ, I, C, A)

## Cite
See `CITATION.cff`. Draft article is in `docs/` (CC BY 4.0).

次回アップデート予定
RPTモデル（Relativistic Psychophysical Time）の補強メモ
1. 基本式

現行モデル：
dT = Λ(z(t)) · dτ

T：主観時間

τ：物理的固有時間

Λ(z)：体感レート（心理的要因の関数）

2. 問題点

相対論的固有時間 τ
→ 人間スケールでは意味が小さい。

Λ(z) の抽象性
→ I（驚き）・C（認知負荷）・A（覚醒）をどう測定するか不明確。

神経メカニズムの欠落
→ 夢・偽記憶・デジャヴを直接説明できない。

3. 補強の方向性
(A) τ（時間基準）の再定義

相対論的時間 → 神経生理学的時間に置き換える。

ニューロン発火リズム（シータ/ガンマ）

シナプス遅延

神経回路の振動周期

(B) Λ(z) の観測可能化

I（驚き／予測誤差） → mismatch negativity (EEG), prediction error (fMRI)

C（認知負荷） → ワーキングメモリ課題、瞳孔径変動

A（覚醒） → HRV（心拍変動）、GSR（皮膚電気反応）

(C) 新しい変数の導入

M（Memory error）：ソースモニタリング錯誤、偽記憶

E（Epileptic activity）：てんかん性放電による記憶断片活性化

S（Sleep fragmentation）：不眠・浅いレム睡眠による記憶統合の異常

(D) 数理的補強

単純な掛け算から非線形関数へ：

例：Λ(z) = exp(αI + βC + γA + δM + εS …)

→ 時間感覚の「急激な崩壊」や「非対称的伸縮」を再現可能。

4. 検証方法

時間再生課題（interval reproduction task）

心拍・脳波との相関分析

夢・デジャヴ体験の頻度との比較研究

## License
- Code: MIT (LICENSE)
- Text/figures: CC BY 4.0 (LICENSE-CC-BY-4.0)
