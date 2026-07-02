from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

with open(ROOT / 'data' / 'results' / 'exp2_provider_summary.csv', newline='', encoding='utf-8') as f:
    provider_rows = list(csv.DictReader(f))

with open(ROOT / 'data' / 'results' / 'exp2_gap_summary.csv', newline='', encoding='utf-8') as f:
    gap_rows = list(csv.DictReader(f))

print('Verified Exp2 released public summaries')
print('--------------------------------------')
for row in sorted(provider_rows, key=lambda r: float(r['overall_mean']), reverse=True):
    print(
        f"{row['provider']:8s} "
        f"zero={float(row['zero_shot_mean']):.2f} "
        f"few={float(row['few_shot_mean']):.2f} "
        f"overall={float(row['overall_mean']):.2f}"
    )

gap = gap_rows[0]
print(
    'Structural-to-semantic-understanding ratio: '
    f"{float(gap['structural_to_semantic_understanding_ratio']):.2f}x"
)
