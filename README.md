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