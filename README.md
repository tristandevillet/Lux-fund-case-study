# Lux Fund Case Study

## Contexte

Ce repo est un cas d'étude pratique construit en parallèle de mes études de comptabilité, pour me préparer aux métiers de fund accounting au Luxembourg. Objectif : appliquer concrètement la théorie (NAV, comptabilité spécifique fonds, PE/RE, reporting réglementaire) sur deux fonds fictifs, plutôt que d'accumuler uniquement des connaissances théoriques.

## Les deux fonds du cas d'étude

**Fund Alpha** — SICAV UCITS (Undertakings for Collective Investment in Transferable Securities), fonds actions Europe/US, EUR, NAV quotidienne, open-ended. Sert de fil rouge pour les fondations : NAV, comptabilité spécifique, réconciliations, FX.

**Fund Beta** — RAIF (Reserved Alternative Investment Fund) Private Equity avec une poche Real Estate. Sert de fil rouge pour : capital calls, waterfalls, états financiers, reporting CSSF (Commission de Surveillance du Secteur Financier)/BCL (Banque Centrale du Luxembourg).

## Structure des dossiers

- `nav/`, `ledger/`, `reconciliation/` — modules construits pour **Fund Alpha**
- `beta/` — module dédié à **Fund Beta**, avec ses propres besoins spécifiques (waterfall, RE)
- `excel/` — livrables Excel (toujours prioritaires)
- `python/` — automatisation Python (optionnelle, uniquement où elle apporte un vrai plus)
- `dashboard/` — dashboard Power BI consolidé

## Fund Alpha

- **Structure légale** : SICAV (Société d'Investissement à Capital Variable) sous statut UCITS
- **Stratégie** : fonds actions, exposition large marchés développés (Europe/US)
- **Devise de base** : EUR
- **Fréquence de calcul de la NAV (Net Asset Value)** : quotidienne (daily)
- **Structure** : open-ended (souscriptions/rachats réguliers)
- **Acteurs simulés** : TA (Transfer Agent), depositary, ManCo (Management Company) fictifs

Fund Alpha sert de fil rouge pour : NAV, comptabilité spécifique fonds, réconciliations, FX.
## NAV Calculator — Fund Alpha

Calculateur de NAV (Net Asset Value) construit en Excel, dans `nav/fund_alpha_nav_calculator.xlsx` :
- **Assets** : positions actions (ASML, LVMH, Microsoft), cash, receivable, accrued income, position fund-of-funds
- **Liabilities** : payables, accrued fees (frais de gestion calculés au prorata journalier, frais de performance, frais courus fund-of-funds)
- **Fund-of-Funds** : détail de 3 sous-fonds UCITS détenus par Fund Alpha (obligations, actions US, actions émergentes), avec frais en cascade
- **NAV Calculation** : calcul final Net Asset Value ÷ nombre de parts

Résultat obtenu : NAV per share = 129,58 €, reflétant à la fois les positions directes et l'exposition fund-of-funds avec ses frais en cascade.

## Comptabilité spécifique fonds & NAV Tie-Out — Fund Alpha

Journal des transactions et processus de rapprochement construits dans `ledger/`, illustrant le cycle comptable quotidien d'un fonds :

- **Transaction Journal** : 5 écritures représentatives (souscription, dividende reçu, accrual de frais de gestion, accrual d'intérêts obligataires, paiement de facture dépositaire), chacune avec sa logique débit/crédit
- **Trial Balance** : agrégation des mouvements par compte via SUMIF, avec vérification d'équilibre (somme des soldes nets = 0)
- **NAV Tie-Out** : comparaison entre la NAV opérationnelle (Assets/Liabilities) et les mouvements comptables du jour — un écart de 48 300 € a été détecté sur le compte Cash (photo figée vs mouvements réels), puis corrigé méthodiquement compte par compte

Résultat après tie-out : NAV per share = 129,75 €, contre 129,58 € avant intégration des transactions du jour.