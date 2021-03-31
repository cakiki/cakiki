#!/usr/bin/env python3
# Based on Will McGugan https://github.com/willmcgugan/willmcgugan/blob/master/willmcgugan.py
# Uses Will McGugan fantastic Rich library to generate markdown https://rich.readthedocs.io/en/latest/

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
import subprocess

console = Console(record=True, width=200)

tree = Tree("[link=https://www.informatik.uni-leipzig.de/~akiki/]Christopher Akiki", guide_style="bold")
interest_tree = tree.add("Interests")
interest_tree.add("Representation Learning")
interest_tree.add("Language Generation")
interest_tree.add("Text Mining")
interest_tree.add("Dataset Creation")
full_stack_tree = tree.add("Lorem Ipsum")
full_stack_tree.add("Lorem Ipsum")
tree.add("Lorem ipsum dolor sit amet")


about = """\

[italic]Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

[royal_blue1]Follow me on twitter [bold link=https://twitter.com/christopher]@christopher[/]"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="royal_blue1", title="[b]Hello, friend!", width=40
)

process = subprocess.run(['cowsay',"Ceci n'est pas une vache"], check=True, stdout=subprocess.PIPE, universal_newlines=True)
cowsay = process.stdout

console.print(Columns([cowsay, panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
