"""Export an executed copy of the notebook to PDF with nbconvert's webpdf exporter (Chromium, no LaTeX).

Usage (in data_lab/, after `uv run playwright install chromium`):
    uv run python export_pdf.py NOTEBOOK.ipynb OUTPUT.pdf
"""
import argparse
from pathlib import Path

import nbformat
from nbconvert import WebPDFExporter

TEMPLATE_DIR = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("notebook", type=Path, help="executed notebook (with outputs)")
    parser.add_argument("output", type=Path, help="PDF file to write")
    args = parser.parse_args()

    # pdf_template/ extends nbconvert's webpdf template and wraps long code lines
    exporter = WebPDFExporter(template_name="pdf_template", extra_template_basedirs=[str(TEMPLATE_DIR)])
    notebook = nbformat.read(args.notebook, as_version=4)
    pdf, _ = exporter.from_notebook_node(notebook, resources={"metadata": {"name": args.output.stem}})
    args.output.write_bytes(pdf)
    print(f"Wrote {args.output} ({len(pdf) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
