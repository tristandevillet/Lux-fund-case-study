# Lux Fund Case Study

*Work in progress — Bloc 1 (Fund Alpha: NAV, accounting, reconciliation) complete. Currently building Bloc 2 (Fund Beta: PE/RE, waterfalls, financial statements).*

**Skills demonstrated:** NAV calculation · double-entry fund accounting · accruals & cut-off · NAV tie-out · bank reconciliation (Python, fuzzy matching) · fund-of-funds structuring

## Context

This repo is a practical case study built alongside my accounting studies, to prepare for fund accounting roles in Luxembourg. The goal: apply theory (NAV, fund-specific accounting, PE/RE, regulatory reporting) concretely to two fictional funds, rather than accumulating theoretical knowledge alone.

## The two funds in this case study

**Fund Alpha** — UCITS SICAV, equity fund Europe/US, EUR, daily NAV, open-ended. Serves as the foundation for: NAV, fund-specific accounting, reconciliations, FX.

**Fund Beta** — Private Equity RAIF with a Real Estate sleeve. Serves as the foundation for: capital calls, waterfalls, financial statements, CSSF/BCL regulatory reporting.

## Folder structure

- `nav/`, `ledger/`, `reconciliation/` — modules built for **Fund Alpha**
- `beta/` — module dedicated to **Fund Beta**, with its own specific needs (waterfall, RE)
- `excel/` — Excel deliverables (always the priority)
- `python/` — Python automation (optional, only where it adds real value)
- `dashboard/` — consolidated Power BI dashboard

## Fund Alpha

- **Legal structure**: SICAV under UCITS status
- **Strategy**: equity fund, broad exposure to developed markets (Europe/US)
- **Base currency**: EUR
- **NAV calculation frequency**: daily
- **Structure**: open-ended (regular subscriptions/redemptions)
- **Simulated actors**: fictional TA (Transfer Agent), depositary, ManCo (Management Company)

Fund Alpha serves as the foundation for: NAV, fund-specific accounting, reconciliations, FX.

## NAV Calculator — Fund Alpha

NAV calculator built in Excel, in [nav/fund_alpha_nav_calculator.xlsx](nav/fund_alpha_nav_calculator.xlsx):
- **Assets**: equity positions (ASML, LVMH, Microsoft), cash, receivable, accrued income, fund-of-funds position
- **Liabilities**: payables, accrued fees (management fees calculated on a daily pro-rata basis, performance fees, fund-of-funds accrued fees)
- **Fund-of-Funds**: detail of 3 UCITS sub-funds held by Fund Alpha (bonds, US equities, emerging market equities), with cascading fees
- **NAV Calculation**: final Net Asset Value ÷ number of shares

Result: NAV per share = 129.58 €, reflecting both direct positions and fund-of-funds exposure with its cascading fees.

## Fund-Specific Accounting & NAV Tie-Out — Fund Alpha

Transaction journal and reconciliation process built in [nav/fund_alpha_nav_calculator.xlsx](nav/fund_alpha_nav_calculator.xlsx) (Transaction Journal and Trial Balance tabs), illustrating the daily accounting cycle of a fund:

- **Transaction Journal**: 5 representative entries (subscription, dividend received, management fee accrual, bond interest accrual, depositary invoice payment), each with its debit/credit logic
- **Trial Balance**: aggregation of movements by account via SUMIF, with balance verification (sum of net balances = 0)
- **NAV Tie-Out**: comparison between the operational NAV (Assets/Liabilities) and the day's accounting movements — a 48,300 € discrepancy was detected on the Cash account (stale snapshot vs. actual movements), then corrected methodically account by account

Result after tie-out: NAV per share = 129.75 €, up from 129.58 € before integrating the day's transactions.

## Reconciliation Engine — Fund Alpha (Python, fuzzy matching)

Bank reconciliation module built in `reconciliation/`, comparing the fund's internal accounting records against an independent custodian bank statement:

- [transaction_journal_cash.csv](reconciliation/transaction_journal_cash.csv): cash movements extracted from the accounting ledger (subscription, dividend, depositary fee payment)
- [bank_statement.csv](reconciliation/bank_statement.csv): independent custodian view of the same cash movements, with a realistic 1-day timing discrepancy on the depositary payment
- [reconciliation_engine.py](reconciliation/reconciliation_engine.py): Python script (pandas, fuzzywuzzy) matching transactions on exact amount, a ±2-day date tolerance, and description similarity scoring — rather than requiring an exact match on every field
- [reconciliation_report.csv](reconciliation/reconciliation_report.csv): exported output documenting each match, the date discrepancy found, and the similarity score

Result: all 3 transactions successfully matched, correctly identifying and tolerating the 1-day timing gap on the depositary payment — illustrating how reconciliation distinguishes normal processing delays from genuine accounting breaks.

## Fund Beta

- **Legal structure**: RAIF (Reserved Alternative Investment Fund)
- **Strategy**: Private Equity, with a Real Estate sleeve
- **Base currency**: EUR
- **Structure**: closed-ended (commitments, capital calls, no free redemptions)
- **Total Commitments**: €50,000,000 (3 LPs)
- **Waterfall**: European style (deal-by-deal), 8% hurdle rate, 100% GP catch-up, 80/20 carried interest split
- **Simulated actors**: fictional AIFM (Alternative Investment Fund Manager), depositary

## PE Waterfall — Fund Beta (European style, deal-by-deal)

European-style PE waterfall built in Excel, in [beta/fund_beta_waterfall.xlsx](beta/fund_beta_waterfall.xlsx), applied to a first realistic deal:

- **Deal**: MedTech Solutions SA — €8,000,000 invested, held 4 years, exited at €16,500,000 (≈2.06x MOIC)
- **4-stage waterfall**: Return of Capital → Preferred Return (8%/year, compounded) → GP Catch-Up (100% GP, until 20% of cumulative profit is reached) → Carried Interest (80/20 split)
- **Verification**: total distributed reconciles exactly to €16,500,000, with the GP receiving precisely 20% of total profit (€1,700,000 of €8,500,000) — confirming the catch-up mechanism correctly rebalances the split despite the LP receiving 100% of capital and preferred return first

Result: LP receives €14,800,000 total, GP receives €1,700,000 total (catch-up + carried interest).

## Additional Excel Practice

Separate from the Fund Alpha/Beta case study, a supplementary exercise practicing advanced Excel techniques — [excel-skills/exos_formules.xlsx](excel-skills/exos_formules.xlsx): XLOOKUP, VLOOKUP (with IFERROR), SUMIFS, Pivot Tables, and Power Query (merge queries, calculated columns, filtering) — applied to a generic transaction-matching scenario with intentional test cases (a genuine amount break, an unmatched transaction).