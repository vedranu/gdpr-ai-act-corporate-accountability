# GDPR, AI Act and ISO 27001 as Pillars of Corporate Accountability for Personal Data in AI Systems - search protocol and data

Replication package for the paper by **Marija Boban, Vedran Uroš and Ratko Brnabić**, submitted to the LIMEN 2026 conference.

The package documents the structured literature search in Scopus and Web of Science (8-9 November 2026), the screening record, the list of studies included in the synthesis, and the data and code used to produce Figures 1 and 2. The manuscript itself is not included.

## Contents

| Path | Description |
|---|---|
| `data/search_queries.csv` | Full Boolean strings for Scopus (TITLE-ABS-KEY) and Web of Science (TS), with the number of records per query |
| `data/screening_flow.csv` | Screening record following the PRISMA logic (367 identified, 248 screened, 22 included) |
| `data/included_studies.csv` | The 22 studies in the synthesis: type and method, search source, theme and model layer, DOI |
| `data/core_corpus_by_year.csv` | Core records per publication year in Scopus and Web of Science (Figure 1) |
| `data/scopus_core_subject_areas.csv` | Subject areas of the Scopus core records (Figure 2a) |
| `data/scopus_core_countries.csv` | Countries/territories of the Scopus core records (Figure 2b) |
| `scripts/` | Python scripts that reproduce Figures 1 and 2 from the CSV files |
| `figures/` | Figures 1 and 2 (PNG and 300 dpi TIF) |
| `docs/Supplementary_S1_search_strings.docx` | Search settings, full strings and screening record in one document |

## Search notes

- Period 2020-2026; searches run on 8 and 9 November 2026, so 2026 covers about ten months.
- Multi-word terms were searched as exact phrases in quotation marks. The bare term AI was not used.
- The core query was limited to articles, reviews and conference papers in English.
- Counts are snapshots and may change as the databases are updated.
- Bibliographic records and abstracts exported from Scopus and Web of Science are not redistributed, in line with the database licences. Only search strings, counts and the list of included studies with DOIs are provided.

## Reproducing the figures

```bash
pip install matplotlib numpy pillow
python scripts/figure1_publications_by_year.py
python scripts/figure2_subjects_countries.py
```

## Licence

Data and documentation: CC BY 4.0 (see `LICENSE-DATA.md`). Code: MIT (see `LICENSE`).

## How to cite

See `CITATION.cff`.
