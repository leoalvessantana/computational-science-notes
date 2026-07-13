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
    "sphinx.ext.mathjax",   
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "dollarmath",   # habilita $...$ (inline) e $$...$$ (bloco)
    "amsmath",      # habilita ambientes LaTeX tipo align, cases, etc.
    # ... outras extensões que você já tenha (colon_fence, deflist, etc.)
]


# Configuração de sintaxe de código
pygments_style = "monokai"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'  # Visual moderno e clean
html_static_path = ['_static']




# ---- CONFIGURAÇÕES DA BARRA LATERAL (MULTILINGUAL) ----

html_theme_options = {
    # Remove o nome do projeto repetido acima da barra de pesquisa
    "sidebar_hide_name": False,
}

html_sidebars = {
    # Remove completamente a barra lateral apenas na Landing Page (Home)
    "index": [
        "sidebar/brand.html",
        "sidebar/search.html",
    ],
    # Para todas as outras páginas, exibe a barra lateral focada no conteúdo atual
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",  # Mostra apenas a estrutura do idioma atual
        "sidebar/scroll-end.html",
    ]
}

# -------------------------------------------------------

def setup(app):
    app.add_css_file('custom.css')