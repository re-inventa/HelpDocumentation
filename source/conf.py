# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Re-AuditIA | Ayuda'
copyright = '2023, Re-Inventa'
author = 'Andi Moya'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser', # Parsea codigo md a stR
    'sphinx_markdown_tables', # Añade tablas para md
    'sphinxcontrib.httpdomain', # Permite escribir documentacion APIs RESTful
]
exclude_patterns = []
language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
html_css_files = ['styles.css']         # Fichero para personalizar el tema
html_favicon = "_static/favicon.ico"

# Configuración de sphinxawesome_theme
html_theme_options = {
    "logo_light": "logo_dark.png",
    "logo_dark": "logo_light.png",
    "awesome_headerlinks": False
}
html_title = "> Documentación R2
"
