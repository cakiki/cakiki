# Based on Will McGugan https://github.com/willmcgugan/willmcgugan/blob/master/willmcgugan.py
# Uses Will McGugan fantastic Rich library to generate markdown https://rich.readthedocs.io/en/latest/
from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

# CODE GOES HERE

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
