"""
Creates a piechart from a JSON file.
See class_structure.json for an example.

example usage:

    python pie2.py class_structure.json piechart.png

"""
import pandas as pd
from matplotlib import pyplot as plt
import sys


def create_piechart(
    json_filename: str,
    output_filename: str,
    title: str,
    explode: int = 0.1,
    dpi: int = 90,
    **kwargs
) -> None:
    """creates a pie chart using matplotlib"""
    df = pd.read_json(json_filename)
    df["explode"] = explode
    plt.pie(df["size"], labels=df["labels"], explode=df["explode"], **kwargs)
    plt.title(title)
    plt.savefig(output_filename, dpi=dpi)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        create_piechart(
            sys.argv[1],
            output_filename=sys.argv[2],
            title="Classroom Activities in DS:F22",
            dpi=150,
            shadow=True,
            normalize=True,
        )
    else:
        print("usage: python pie2 <json_filename> <diagram_filename>")
