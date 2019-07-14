# -*- coding: utf-8 -*-
#
# DCG documentation build configuration file.
#
# This file is execfile()d with the current directory set to its
# containing dir.

import sys
import os
import sphinx_rtd_theme
from datetime import date

#sys.path.append(os.path.abspath('_ext/phpdomain'))
#sys.path.append(os.path.abspath('_ext/tk.phpautodoc/src'))

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx',
    #'sphinxcontrib-phpdomain',
    #'sphinxcontrib_phpautodoc',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'DC_General'
copyright = u'{:d}, Team DCG'.format(date.today().year)
version = '2.1'
release = '2.1.0'
language = 'de'
exclude_patterns = ['_build', '_ext']
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes', ]
# html_static_path = []
html_use_modindex = False
htmlhelp_basename = 'DCGdoc'
html_favicon = '_img/favicon.ico'
html_last_updated_fmt = '%d.%m.%Y'
html_show_sphinx = False
html_show_copyright = True

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
  'papersize': 'a4paper',
  'pointsize': '10pt',
  'classoptions': ',openany,oneside',
  'babel' : '\\usepackage[german]{babel}',
}

latex_documents = [
  ('index', 'DCG.tex', u'DCG Documentation',
   u'Team DCG', 'manual'),
]

# -- Options for manual page output ---------------------------------------

man_pages = [
    ('index', 'DCG', u'DCG Documentation',
     [u'Team DCG'], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
  ('index', 'DCG', u'DCG Dokumentation',
   u'Team DCG', 'DCG', 'Online-Handbuch des Projektes.',
   'Miscellaneous'),
]

intersphinx_mapping = {
    'dcgeneral': ('http://contao-community-alliance.github.io/dc-general-docs/', None)
}
