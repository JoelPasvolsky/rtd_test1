
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

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/test.png"

copyright = 'D-Wave'
version = "0.1"

html_theme_options = {
    "footer_start": ["copyright"],
#    "footer_end": ["version"],
    "icon_links_label": "Quick Links",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/JoelPasvolsky/rtd_test1",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
            "attributes": {
                "aria-label": "github repo link",
            },
        },
    ],
    "collapse_navigation": True,
    "header_links_before_dropdown": 5,
    "navbar_align": "left",
    "show_prev_next": False,
    "logo": {
        "image_light": "_static/test.png",
        "image_dark": "_static/test.png",
    },
    "secondary_sidebar_items": [
        "page-toc",
        "page-source",
    ],
    "navbar_end": ["navbar-icon-links"],
}
html_sidebars = {
    "**": ["sidebar-nav-bs"],  # remove ads
}
html_static_path = ['_static']
templates_path = ['_templates']

def setup(app):
   app.add_css_file('theme_overrides.css')

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    }