# Development

## Environment

The project uses [uv](https://docs.astral.sh/uv/). `pyproject.toml` sets `exclude-newer = "2024-04-03T00:00:00Z"`,
so uv only resolves package versions that existed when the assignment was submitted; `uv.lock` pins them
(Python 3.11, pandas 2.2.1, scikit-learn 1.4.1, ydata-profiling 4.7.0, matplotlib 3.7.3).

```bash
uv sync
```

Some pins matter:

| Package | Why |
|---|---|
| `matplotlib==3.7.3` | 3.8 breaks seaborn heatmaps; seaborn cannot be upgraded because of ydata-profiling |
| `setuptools<70` | ydata-profiling 4.7 imports `pkg_resources` |
| `tabulate` | `DataFrame.to_markdown()` in the notebook |
| `playwright` (dev) | PDF export with `export_pdf.py` |

## Linting and formatting

[Ruff](https://docs.astral.sh/ruff/) checks and formats the scripts. The rules are in `[tool.ruff]` in
`pyproject.toml`: errors, Pyflakes and import sorting (`E4`, `E7`, `E9`, `F`, `I`), line length 120. The notebook is
excluded so that it stays as submitted. Ruff is run with `uvx`, so it is not part of the locked dependencies.

```bash
uvx ruff check .
```

```bash
uvx ruff format .
```

## Code layout

| What | Where |
|---|---|
| Analysis, plots, constants such as `CORRELATION_THRESHOLD` and `GENERATE_PAIR_PLOTS` | [data_lab/fda_a2_25061944.ipynb](../data_lab/fda_a2_25061944.ipynb), see [notebook.md](notebook.md) |
| Preprocessing tasks 1–4 | [data_lab/task1.py](../data_lab/task1.py) … [task4.py](../data_lab/task4.py) |
| PDF export and its template | [data_lab/export_pdf.py](../data_lab/export_pdf.py), [data_lab/pdf_template/](../data_lab/pdf_template) |
| Files that git ignores (generated plots, pickles, HTML reports) | [.gitignore](../.gitignore) |

The task scripts read `data/32130_AT2_25061944.csv` and write `data_lab/output/excel/task<n>.xlsx`; their paths are
relative to the repository, so they run from any directory. The notebook uses paths relative to `data_lab/`.
