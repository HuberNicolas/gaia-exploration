# TODO

Open tasks before the repository is made public. See also [Known issues](README.md#known-issues).

## 1. Run again

- [x] Replace Poetry with uv and lock the versions from April 2024 (`exclude-newer`); there was no lock file before
- [x] Declare `setuptools<70` (for `pkg_resources` in ydata-profiling 4.7) and `tabulate` (for `to_markdown()`)
- [x] Run the whole notebook headless: no errors, and the Excel results are identical to the submitted ones
- [x] Run the four task scripts: outputs identical to the submitted `task1-4.xlsx`
- [ ] Export the notebook to PDF again (needs LaTeX; not tested)

## 2. Clean up

- [x] Make the plots for every pair of attributes opt-in (`GENERATE_PAIR_PLOTS`) and remove the 3,780 generated files
  from the index; they stay in the history
- [x] Stop committing the intermediate pickle files (`data_lab/output/pk/`)
- [x] Stop the notebook from deleting `output/excel/task*.xlsx` and the solution workbook
- [x] Wrap the task scripts in `main()`, make paths independent of the working directory, fix two small bugs
- [ ] Optional: shrink the history (376 MB, mostly the removed plots) with `git filter-repo`; needs a force-push

## 3. Documentation

- [x] README with outputs, data licence and acknowledgements
- [x] `docs/` with notebook, dataset and troubleshooting

## 4. Before publishing

- [x] Choose and add a license (MIT)
- [x] Add the project context (course, institution, year) to the README
- [x] Credit third parties (ESA Gaia, DPAC, UTS teaching team)
- [ ] Check for secrets in the files and the git history, right before publishing
- [ ] Commit author e-mail (university address) becomes public; add a `.mailmap` if you prefer another address
- [ ] Push and set the GitHub repository to public
