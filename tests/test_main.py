import pytest

import docky.utility
from docky.console import console
from docky.docky import xml
from docky.plugin.tex import create_latex_file
from rich.console import Console


def test_tex():

    xml_file = xml("test/tex/tex.docky")
    root = xml_file.get_root()

    tree = xml_file.get_tree()

    for item in tree.iter():
        console.print(
            "[blue]<{0}>[/]\n\t{1}\n[blue]</{0}>[/]".format(item.tag, item.text.strip())
        )
        pass

    latex_items = root.findall("latex")

    for item in latex_items:
        latex_text = item.text.strip()
        console.log(latex_text)

        create_latex_file(latex_text)


def test_manim():
    xml_file = xml("test/manim/manim.docky")
    root = xml_file.get_root()
    tree = xml_file.get_tree()

    manim_items = root.findall("manim")

    # docker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd -W)":/manim manimcommunity/manim

    for item in manim_items:
        item_text = item.text.strip()
        console.log(item_text)

        create_manim_file(item_text)
