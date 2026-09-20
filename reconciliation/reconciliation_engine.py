import pandas as pd
from fuzzywuzzy import fuzz

# Charger les deux fichiers CSV
transaction_journal = pd.read_csv('transaction_journal_cash.csv', sep=';')
bank_statement = pd.read_csv('bank_statement.csv', sep=';')

# Nettoyer les espaces superflus dans les noms de colonnes
transaction_journal.columns = transaction_journal.columns.str.strip()
bank_statement.columns = bank_statement.columns.str.strip()

# Nettoyer et convertir la colonne Amount en nombre (format belge : point milliers, virgule décimale)
transaction_journal['Amount'] = transaction_journal['Amount'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
bank_statement['Amount'] = bank_statement['Amount'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

# Convertir les dates en vrai format date
transaction_journal['Date'] = pd.to_datetime(transaction_journal['Date'], format='%d-%m-%y')
bank_statement['Date'] = pd.to_datetime(bank_statement['Date'], format='%d-%m-%y')


print("Transaction Journal:")
print(transaction_journal)
print("\nBank Statement:")
print(bank_statement)
print(transaction_journal.dtypes)

# Fonction de matching
def find_match(bank_row, journal_df):
    for idx, journal_row in journal_df.iterrows():
        if bank_row['Amount'] != journal_row['Amount']:
            continue
        date_diff = abs((bank_row['Date'] - journal_row['Date']).days)
        if date_diff > 2:
            continue
        similarity = fuzz.token_sort_ratio(bank_row['Description'], journal_row['Description'])
        if similarity < 70:
            continue
        return idx, date_diff, similarity
    return None, None, None

# Construire le rapport de réconciliation
results = []
for i, bank_row in bank_statement.iterrows():
    match_idx, date_diff, similarity = find_match(bank_row, transaction_journal)
    if match_idx is not None:
        results.append({
            'Bank Description': bank_row['Description'],
            'Journal Description': transaction_journal.loc[match_idx, 'Description'],
            'Amount': bank_row['Amount'],
            'Bank Date': bank_row['Date'].date(),
            'Journal Date': transaction_journal.loc[match_idx, 'Date'].date(),
            'Date Difference (days)': date_diff,
            'Similarity (%)': similarity,
            'Status': 'Matched'
        })
    else:
        results.append({
            'Bank Description': bank_row['Description'],
            'Journal Description': None,
            'Amount': bank_row['Amount'],
            'Bank Date': bank_row['Date'].date(),
            'Journal Date': None,
            'Date Difference (days)': None,
            'Similarity (%)': None,
            'Status': 'Unmatched'
        })

# Exporter le rapport en CSV
reconciliation_report = pd.DataFrame(results)
reconciliation_report.to_csv('reconciliation_report.csv', sep=';', index=False)
print("Rapport de réconciliation exporté : reconciliation_report.csv")
print(reconciliation_report)