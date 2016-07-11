# -*- coding: utf-8 -*-
#
# docs/bbob-biobj/functions documentation build configuration file, created by
# sphinx-quickstart on Thu Dec 24 16:35:27 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import shlex

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------
authors = "The BBOBies"
# WHEN CHANGING THIS CHANGE ALSO the abstract in index.rst accordingly
abstract = """The ``bbob-largescale`` test suite containing 24 single objective
    functions in continuous domain is an extension of the well-known
    single-objective noiseless ``bbob`` test suite in large dimension.
    The core idea is to make rotational transformations :math:`\textbf{R}` and :math:`\textbf{Q}`
    in search space, introduced in the ``bbob`` test suite, cheaper but remaining some desired
    properties. This documentation presents our approach where the rotational transformation will
    be replaced by the product of a permutation matrix times a block-diagonal matrix times a
    permutation matrix in order to construct large scale testbeds.
"""

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
#    'sphinx.ext.mathjax',
    'sphinx.ext.pngmath'
]


pngmath_use_preview = True  # "When this is enabled, the images put into the HTML document will get a vertical-align style that correctly aligns the baselines."
pngmath_dvipng_args = [ # see http://www.nongnu.org/dvipng/dvipng_4.html#Command_002dline-options
    '-gamma', '1.5',  # heavyness of color 0.5 is between black and background, 1.5 is blacker than black, --gamma works as well?
    '-D', '109',  # size, 100=current font size
#    '-D', '110',  # size, 100=current font size, 110 is default
#    '-gif',  # doesn't work in browser and doesn't look less pixelated
#    '--bdpi', '440',  # see man dvipng
#    '-Q', '5',
    '-bg', 'Transparent',
#    '-T', '1.1in,1.3cm',   # image size, affects size, but nothing is rendered
]

latex_commands = r"""
  \newcommand{\R}{\ensuremath{\mathbb{R}}}
  \newcommand{\ve}[1]{{\boldsymbol{#1}}}
  \newcommand{\x}{\ensuremath{\ve{x}}}
  \newcommand{\finstance}{\ensuremath{f^j}}
"""

pngmath_latex_preamble = latex_commands


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'bbob-largescale-functions-doc'
copyright = u'2016, The BBOBies'
author = u'The BBOBies'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.9'
# The full version, including alpha/beta/rc tags.
release = '0.9'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'sphinx_rtd_theme'
html_theme = 'bizstyle'  # white/blue, quite good, too blue on the start page
#html_theme = 'nature'  # underlays of sections titles
#html_theme = 'alabaster' #  white, times font 
#html_theme = 'sphinxdoc'  # puts too much empty spaces left and right
# html_theme = 'sphinx_rtd_theme'  # contents not structured (mobile style?)
# html_theme = 'agogo'  # fixed width
# html_theme = 'pyramid'  # relatively clean white/gray, sf font hard to read, too small section titles

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {'font_family': 'goudy old style'}
# sticky_navigation

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'COCO: The Large Scale Black-Box Optimization Benchmarking (bbob-largescale) Test Suite'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'bbob-largescale-functions-doc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

# Additional stuff for the LaTeX preamble.
'preamble': r"""
  \usepackage{amssymb}
  \pagestyle{plain}
  \newcommand{\chapter}[1]{}  % hack to be able to use article documentclass
  \newcommand{\ignore}[1]{}  % never used
  \newcommand{\COCO}{\href{https://githum.com/numbbo/coco}{COCO}}
  \newcommand{\ff}[1]{\ensuremath{f_{#1}}} 
    \renewcommand{\topfraction}{1} % max fraction of floats at top
    \renewcommand{\bottomfraction}{1} % max fraction of floats at bottom
    %   Parameters for TEXT pages (not float pages):
    \setcounter{topnumber}{3}
    \setcounter{bottomnumber}{3}
    \setcounter{totalnumber}{3}     % 2 may work better
    \setcounter{dbltopnumber}{4}    % for 2-column pages
    \renewcommand{\dbltopfraction}{1}  % fit big float above 2-col. text
    \renewcommand{\textfraction}{0.0}  % allow minimal text w. figs
    %   Parameters for FLOAT pages (not text pages):
    \renewcommand{\floatpagefraction}{0.9}  % require fuller float pages
    % N.B.: floatpagefraction MUST be less than topfraction !!
    \renewcommand{\dblfloatpagefraction}{0.8}  % require fuller float pages
  
""" + latex_commands,
# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'bbob-largescale-functions.tex', u'COCO: The Large Scale Black-Box Optimization Benchmarking (bbob-largescale) Test Suite',
  r"""
      Ouassim Ait Elhara$^3$,
      Duc Manh Nguyen$^{2,3}$,
      Tea Tu\v{s}ar$^1$,
      Dimo Brockhoff$^1$,
      Nikolaus Hansen$^{2,3}$, 
      Anne Auger$^{2,3}$ 
  \\
    $^1$Inria, research centre Lille, France
  \\
    $^2$Inria, research centre Saclay, France
  \\
    $^3$Universit\'e Paris-Saclay, LRI, France
    """, 
   'article'  # 'manual'
   ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# pngmath_latex_preamble = r"\newcommand{\R}{\mathbb{R}}"

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'bbob-largescale-functions-doc', u'Function Documentation of the bbob-largescale Test Suite',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'bbob-largescale-functions-doc', u'Function Documentation of the bbob-largescale Test Suite',
   author, 'bbob-largescale-functions-doc', 'Documents all functions of the bbob-largescale test suite.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False
