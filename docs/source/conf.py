# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'Computational Science Notes'
copyright = '2026, Leonardo Alves Santana'
author = 'Leonardo Alves Santana'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Configuração de sintaxe de código
pygments_style = "monokai"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'  # Visual moderno e clean
html_static_path = ['_static']