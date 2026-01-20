
import os

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx_copybutton',
#    'hoverxref.extension',
]

autosummary_generate = True

#hoverxref_roles = ['term']
#hoverxref_role_types = {'term': 'tooltip'}
#hoverxref_mathjax = True

source_suffix = ['.rst', '.md']

root_doc = 'index'

language = 'en'

add_module_names = False

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*/shared/*.rst',]

pygments_style = 'sphinx'

todo_include_todos = False

copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"

if os.environ.get('READTHEDOCS', False):
    pass

html_theme = 'sphinx_rtd_theme'
html_logo = "_static/test.png"

copyright = 'D-Wave'
version = "0.1"

html_static_path = ['_static']
templates_path = ['_templates']

def setup(app):
   app.add_css_file('theme_overrides.css')

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    }