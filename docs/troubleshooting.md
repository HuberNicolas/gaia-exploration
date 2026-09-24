# Troubleshooting

## `FileNotFoundError: ../data/32130_AT2_25061944.csv`

The notebook uses paths relative to `data_lab/`. Start Jupyter or `nbconvert` in `data_lab/`, see the
[Quick start](../README.md#quick-start). The task scripts work from any directory.

## `ModuleNotFoundError: No module named 'pkg_resources'`

ydata-profiling 4.7 imports `pkg_resources`, which newer setuptools versions no longer contain. `uv.lock` pins
setuptools 69.2.0. Run `uv sync` and start Jupyter with `uv run`.

## Plots are saved but not shown in the notebook

ydata-profiling leaves matplotlib unable to show figures inline ("FigureCanvasAgg is non-interactive, and thus cannot
be shown"). The cells that create a profiling report therefore end with `%matplotlib inline`. If you run cells out of
order, run `%matplotlib inline` again after a profiling report.

## `Executable doesn't exist` when exporting the PDF

Playwright needs its own Chromium. Run `uv run playwright install chromium` once.

## `ImportError: Missing optional dependency 'tabulate'`

`DataFrame.to_markdown()` needs tabulate. It is in `uv.lock`; run `uv sync`.

## Heatmaps show numbers only in the first row

This is a bug in matplotlib 3.8 with seaborn 0.12 (<https://github.com/mwaskom/seaborn/issues/3478>). The project pins
matplotlib 3.7.3 for this reason. Do not upgrade matplotlib without upgrading seaborn, which ydata-profiling 4.7 does
not allow.

## The run is slow or uses a lot of disk space

The profiling report of the cleaned data is about 356 MB. With `GENERATE_PAIR_PLOTS = True`, the notebook writes about
3,800 more files (about 330 MB) and takes much longer.
