# Notebook

[data_lab/fda_a2_25061944.ipynb](../data_lab/fda_a2_25061944.ipynb) contains the whole analysis. It reads
`../data/32130_AT2_25061944.csv` and `../data/head_description.xlsx` and writes to `./output/`, so it must run with
`data_lab/` as the working directory.

The notebook is stored without outputs. A full run takes about 11 minutes; most of the time goes into the two
profiling reports, the pair plot of all attributes, t-SNE and UMAP.

## Sections

| Section | What happens |
|---|---|
| 0. Preparation, Constants, Data Loading, Setup | Imports, settings, loading the CSV and the column descriptions, clearing the output folders |
| 1A. Initial data exploration | Profiling report of the raw data, statistics per attribute, missing values per class, outliers, pair plots, correlation heatmap, plots of correlated pairs |
| Handle missing data / values | Median imputation per class for `GRVSmag`, `e_GRVSmag` and `Age-Flame`; rows with missing `Mass-Flame`, `z-Flame` or `Lum-Flame` are removed. The protocol goes to `output/excel/cleaned_missing_data_protocol.xlsx` |
| 1B. Data preprocessing, Task 1–4 | Equi-width and equi-depth binning of `RA_ICRS` and `DE_ICRS`, scaling of `Age-Flame`, discretisation of `Mass-Flame`, binarisation of `SpType-ELS` |
| Further Preprocessing, Drop columns, Standardizing | Cleaning of the index columns, dropping columns, a scaler per column chosen by skewness and outliers, profiling report of the cleaned data |
| Correlation | Correlation of the preprocessed data; eight highly correlated scaled columns are dropped |
| Dimred, Clustering, Hierarchical Clustering | PCA, k-means (elbow method), UMAP, t-SNE and dendrograms with four linkage methods |
| Feature Selection | Feature importance of a random forest on the preprocessed data |
| 1C. Summary, Deliverables, Notes, Export | Assignment text, notes and the command used to export the PDF |

## Settings

The settings are in the "Constants" section:

| Constant | Value | Meaning |
|---|---|---|
| `SEED` | `31011997` | Random seed for k-means, UMAP and t-SNE |
| `SAMPLE_RATIO` | `0.1` | Only used in commented-out lines that sample the data to speed up development |
| `SKEWNESS_THRESHOLD` | `0.5` | Columns above this absolute skewness get a min-max scaler (or a robust scaler if they have outliers) |
| `CORRELATION_THRESHOLD` | `0.7` | Pairs above this absolute correlation are plotted and considered for removal |
| `OUTLIER_COUNT_THRESHOLD` | `0` | Columns with more IQR outliers than this get a robust scaler |
| `MAX_CLUSTER_LEVEL` | `6` | Dendrogram levels for hierarchical clustering |
| `GENERATE_PAIR_PLOTS` | `False` | Create plots for every pair of attributes (see below) |
| `PALETTE`, `ALPHA` | `coolwarm`, `0.6` | Colours and transparency of the plots |
| `OUTPUT_PATH` | `./output` | Output folder |

## Plots for every pair of attributes

Three functions plot every pair of numeric attributes whose absolute correlation is at least a threshold. With the
threshold `0`, this means every pair:

| Function | Output folder | Files |
|---|---|---|
| `scatter_plot_between_attributes_based_on_corr_subplots` | `output/exploration/features/corr_above_scatterplot_0/` | 756 |
| `distribution_plot_between_attributes_based_on_corr_subplots` | `output/exploration/features/corr_above_jointplot_0/` | 756 |
| `jointplots_between_attributes_based_on_corr_subplots` | `output/exploration/features/jointplots/corr_above_jointplot_0/` | 2,268 |

These calls only run when `GENERATE_PAIR_PLOTS = True`. The folders are listed in `.gitignore`. The plots for pairs
above `CORRELATION_THRESHOLD` (`output/exploration/features/corr_above_scatterplot_0.7/`, 50 files) are always
created and committed.

## Output folders

When the notebook starts, `setup_folders()` empties `exploration/statistics/`, `exploration/features/`,
`exploration/reports/`, `exploration/dimred/pca/`, `exploration/dimred/hclustering/` and `pk/` in `output/`.
`output/excel/` is not emptied because it also holds the Excel files of the task scripts and the solution workbook.

The pickle files in `output/pk/` pass DataFrames between sections: the "Correlation" section reads
`preprocessed_data.pkl`, which an earlier section wrote.

## Export to PDF

The submitted report [fda_a2_25061944.pdf](../fda_a2_25061944.pdf) was made with nbconvert and LaTeX (the command is
in the last cell). [fda_a2_25061944_rerun_2026.pdf](../fda_a2_25061944_rerun_2026.pdf) was made with
[export_pdf.py](../data_lab/export_pdf.py), which needs no LaTeX: nbconvert's webpdf exporter prints the notebook with
Chromium. The template in [pdf_template/](../data_lab/pdf_template) wraps long code lines, which would otherwise be cut
off at the page edge.

Run these commands in `data_lab/`:

1. Install Chromium for Playwright (once):

   ```bash
   uv run playwright install chromium
   ```

2. Run the notebook into an executed copy (about 11 minutes):

   ```bash
   uv run jupyter nbconvert --to notebook --execute fda_a2_25061944.ipynb --output fda_a2_25061944.executed.ipynb
   ```

3. Export the executed copy:

   ```bash
   uv run python export_pdf.py fda_a2_25061944.executed.ipynb ../fda_a2_25061944_rerun_2026.pdf
   ```

The executed copy is ignored by git. The PDF is about 26 MB; the pair plot of all attributes alone is 14 MB.

The profiling reports are shown as progress bars only; the reports themselves are HTML files in
`output/exploration/reports/`.
