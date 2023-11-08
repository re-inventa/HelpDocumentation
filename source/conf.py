# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Re-AuditIA | Ayuda'
copyright = '2023, Andi Moya'
author = 'Andi Moya'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser', # Parsea codigo md a stR
    'sphinx_markdown_tables', # Añade tablas para md
    'sphinxcontrib.httpdomain', # Permite escribir documentacion APIs RESTful
]
# extensions = ['sphinx.ext.autodoc',
        # 'sphinx.ext.intersphinx',
        # 'sphinx.ext.todo',
        # 'sphinx.ext.mathjax',
        # 'sphinx.ext.napoleon',
        # 'sphinx.ext.autosummary', # solamente si se la quiere usar
        # 'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Agrega un directorio de codigo fuente para analizar
#sys.path.insert(0, os.path.abspath('../api'))

# Tabla de contenidos
html_sidebars = { '**': ['globaltoc.html', 'relations.html',
        'sourcelink.html', 'searchbox.html'], }