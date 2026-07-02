from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

def read_csv_rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

contract_rows = read_csv_rows(ROOT / 'data' / 'catalog' / 'contract_catalog.csv')
exp2_rows = read_csv_rows(ROOT / 'data' / 'results' / 'exp2_provider_summary.csv')
exp5_rows = read_csv_rows(ROOT / 'data' / 'results' / 'exp5_human_evaluation_summary.csv')
print('PromptCraft public artifact quick check')
print('--------------------------------------')
print(f"Candidate-pool contracts: {len(contract_rows)}")
print(f"Released Exp2 provider rows: {len(exp2_rows)}")
print(f"Released Exp5 summary rows: {len(exp5_rows)}")
print('Top Exp2 provider by overall mean:', exp2_rows[0]['provider'], exp2_rows[0]['overall_mean'])
print('Exp5 sampled test cases:', exp5_rows[0]['num_sampled_test_cases'])
print('Exp5 expert scoring instances:', exp5_rows[0]['num_expert_scores'])
