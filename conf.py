project = 'La Docu 🏠'
copyright = '2022, Mendoza Nicolás'
author = 'Mendoza Nicolás'
version = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx.ext.githubpages'
]

templates_path = ['_templates']
language = 'es'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
  'display_version': True,
  'prev_next_buttons_location' : 'both'
}

html_static_path = ['_static']