#!/usr/bin/env python3
# Based on Will McGugan https://github.com/willmcgugan/willmcgugan/blob/master/willmcgugan.py
# Uses Will McGugan's fantastic Rich library to generate markdown https://rich.readthedocs.io/en/latest/

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
import subprocess
import os
from random import choice
import datetime

###########################################################################################################
console = Console(record=True, width=200)
###########################################################################################################
tree = Tree("[link=https://www.informatik.uni-leipzig.de/~akiki/]Christopher Akiki", guide_style="bold")
interest_tree = tree.add("Interests")
interest_tree.add("Representation Learning")
interest_tree.add("Language Generation")
interest_tree.add("Text Mining")
interest_tree.add("Dataset Creation")
full_stack_tree = tree.add("Lorem Ipsum")
full_stack_tree.add("Lorem Ipsum")
tree.add("Lorem ipsum dolor sit amet")
###########################################################################################################
cows = os.listdir('/usr/share/cowsay/cows/')
cows = [cow.split('.')[0] for cow in cows]
cow = choice(cows)
fortune = subprocess.run(["fortune"], check=True, stdout=subprocess.PIPE, universal_newlines=True)
cowsay = subprocess.run(['cowsay', '-f', f'{cow}', f'{fortune.stdout}'], stdout=subprocess.PIPE, check=True, universal_newlines=True)
cowsay = cowsay.stdout
###########################################################################################################
about = ''
about += f'\n\n[italic]This message was brought to you by the [bold link=https://en.wikipedia.org/wiki/Cowsay]cowsay[/] {cow}, [bold link=https://en.wikipedia.org/wiki/Fortune_(Unix)]fortune[/] and [bold link=https://github.com/willmcgugan/rich]Rich[/]. '
about += "\n\n[bold]Follow me on twitter: [bold link=https://twitter.com/christopher]@christopher[/]"
###########################################################################################################
date = datetime.date.today()
day = date.strftime('%A')
month = date.strftime('%B')
day_int = date.day
year = date.year
date_string = f'{day}, {day_int} {month} {year}'
panel = Panel.fit(about, box=box.ASCII, border_style="royal_blue1", title=f'[b]{date_string}', width=40)

console.print(Columns([cowsay, panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
