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

## License
- Code: MIT (LICENSE)
- Text/figures: CC BY 4.0 (LICENSE-CC-BY-4.0)
