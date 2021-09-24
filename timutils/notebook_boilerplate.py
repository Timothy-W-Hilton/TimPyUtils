"""things I like to run at the beginning of a Jupyter Notebook
"""

# use the full width of the browser window
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

# display current git revision and python environment
from timutils import describe_environment
describe_environment.print_env()
