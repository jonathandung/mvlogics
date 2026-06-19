import os
project = 'mvlogics'
author = 'Jonathan Dung'
copyright = '2026 Jonathan Dung' # noqa: A001
version = '0.9'
release = '0.9.5'
need_sphinx = '9.1.0'
pygments_style = 'sphinx'
extensions = ['autoapi.extension', 'notfound.extension', 'sphinx_copybutton', 'sphinx.ext.viewcode']
default_role = 'py:obj'
suppress_warnings = ['autoapi.python_import_resolution']
if os.getenv('READTHEDOCS') == 'True':
    html_theme = 'furo'
    html_theme_options = {'top_of_page_buttons': ['view', 'edit'], 'source_repository': 'https://github.com/jonathandung/mvlogics', 'source_branch': 'main', 'source_directory': 'docs/source/'}
    source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
    extensions.append('myst_parser')
else:
    html_theme = 'sphinx_book_theme'
    suppress_warnings.append('toc.not_readable')
html_short_title = 'mvlogics 0.9.5 docs'
autoapi_dirs = ['../../mvlogics']
autoapi_file_patterns = ['*.pyi']
autoapi_root = 'api'
autoapi_python_class_content = 'both'
autoapi_member_order = 'groupwise'
autoapi_keep_files = True
autoapi_options = ['members', 'undoc-members', 'show-inheritance', 'show-module-summary', 'special-members']
copybutton_exclude = '.linenos, .gp, .go'
copybutton_prompt_text = '>>> '
