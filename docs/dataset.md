# Dataset

The sample comes from the ESA mission Gaia, Data Release 3 (DR3). The course 32130 Fundamentals of Data Analytics at
UTS provided it for Assessment Task 2; the number in the file name is the author's student ID. The column names
match the Gaia DR3 catalogue in VizieR (for example `SpType-ELS`, `Lum-Flame`).

Gaia data are licensed under [CC BY-NC 3.0 IGO](https://www.cosmos.esa.int/web/gaia-users/license). See the
[Acknowledgements](../README.md#acknowledgements) for the required credit.

## Files

| File | Rows | Content |
|---|---|---|
| `data/32130_AT2_25061944.csv` | 3,000 | The sample (1,666 A, 1,334 B) |
| `data/sample.csv` | 99 | First rows of the sample |
| `data/head_description.csv`, `.xlsx` | 30 | Description of every column and the cleaning action taken; the notebook reads the `.xlsx` |

## Columns

| Column | Description |
|---|---|
| `Unnamed: 0.1`, `Unnamed: 0` | Index columns from earlier exports, no meaning |
| `RA_ICRS`, `DE_ICRS` | Right ascension and declination (ICRS) |
| `Source` | Gaia source identifier |
| `Plx` | Parallax (mas) |
| `PM`, `pmRA`, `pmDE` | Total proper motion and its components (mas/yr) |
| `Gmag`, `BPmag`, `RPmag`, `GRVSmag` | Mean magnitudes in the G, BP, RP and RVS bands |
| `e_Gmag`, `e_BPmag`, `e_RPmag`, `e_GRVSmag` | Errors of these magnitudes |
| `BP-RP`, `BP-G`, `G-RP` | Colour indices |
| `pscol` | Pseudocolour (µm⁻¹), 97 % missing |
| `Teff` | Effective temperature (K) |
| `Dist` | Distance (pc) |
| `Rad`, `Lum-Flame`, `Mass-Flame` | Radius, luminosity and mass in solar units |
| `Age-Flame` | Age (Gyr) |
| `z-Flame` | Redshift (km/s) |
| `SpType-ELS` | Spectral class: `A` or `B`, padded with six spaces |

The missing-value shares per column are summarised in the notebook section "Initial Data Exploration Insights".
