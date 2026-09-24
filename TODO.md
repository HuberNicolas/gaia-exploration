# TODO

Open tasks before the repository is made public. See also [Known issues](README.md#known-issues).

## 1. Run again

- [x] Replace Poetry with uv and lock the versions from April 2024 (`exclude-newer`); there was no lock file before
- [x] Declare `setuptools<70` (for `pkg_resources` in ydata-profiling 4.7) and `tabulate` (for `to_markdown()`)
- [x] Run the whole notebook headless: no errors, and the Excel results are identical to the submitted ones
- [x] Run the four task scripts: outputs identical to the submitted `task1-4.xlsx`
- [x] Show plots in the notebook again after the profiling reports (ydata-profiling had disabled inline figures)
- [x] Export the notebook to PDF again with `export_pdf.py` (nbconvert webpdf, no LaTeX): `fda_a2_25061944_rerun_2026.pdf`

## 2. Clean up

- [x] Make the plots for every pair of attributes opt-in (`GENERATE_PAIR_PLOTS`) and remove the 3,780 generated files
  from the index; they stay in the history
- [x] Stop committing the intermediate pickle files (`data_lab/output/pk/`)
- [x] Stop the notebook from deleting `output/excel/task*.xlsx` and the solution workbook
- [x] Wrap the task scripts in `main()`, make paths independent of the working directory, fix two small bugs
- [x] Shrink the history with `git filter-repo`: remove the per-pair plots and pickles from all commits

## 3. Documentation

- [x] README with outputs, data licence and acknowledgements
- [x] `docs/` with notebook, dataset and troubleshooting

## 4. Before publishing

- [x] Choose and add a license (MIT)
- [x] Add the project context (course, institution, year) to the README
- [x] Credit third parties (ESA Gaia, DPAC, UTS teaching team)
- [x] Check for secrets in the files and the git history (none found)
- [x] Rewrite the commit author e-mail to the current address
- [ ] Force-push the rewritten history (`git push --force origin main`)
- [ ] Set the GitHub repository to public
