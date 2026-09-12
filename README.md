# Lux Fund Case Study

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

NAV calculator built in Excel, in `nav/fund_alpha_nav_calculator.xlsx`:
- **Assets**: equity positions (ASML, LVMH, Microsoft), cash, receivable, accrued income, fund-of-funds position
- **Liabilities**: payables, accrued fees (management fees calculated on a daily pro-rata basis, performance fees, fund-of-funds accrued fees)
- **Fund-of-Funds**: detail of 3 UCITS sub-funds held by Fund Alpha (bonds, US equities, emerging market equities), with cascading fees
- **NAV Calculation**: final Net Asset Value ÷ number of shares

Result: NAV per share = 129.58 €, reflecting both direct positions and fund-of-funds exposure with its cascading fees.

## Fund-Specific Accounting & NAV Tie-Out — Fund Alpha

Transaction journal and reconciliation process built in `nav/fund_alpha_nav_calculator.xlsx` (Transaction Journal and Trial Balance tabs), illustrating the daily accounting cycle of a fund:

- **Transaction Journal**: 5 representative entries (subscription, dividend received, management fee accrual, bond interest accrual, depositary invoice payment), each with its debit/credit logic
- **Trial Balance**: aggregation of movements by account via SUMIF, with balance verification (sum of net balances = 0)
- **NAV Tie-Out**: comparison between the operational NAV (Assets/Liabilities) and the day's accounting movements — a 48,300 € discrepancy was detected on the Cash account (stale snapshot vs. actual movements), then corrected methodically account by account

Result after tie-out: NAV per share = 129.75 €, up from 129.58 € before integrating the day's transactions.