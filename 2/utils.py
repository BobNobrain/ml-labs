from IPython.display import HTML, display
import matplotlib.pyplot as plt
import numpy as np


def heatmap(matrix, xlabels=[], ylabels=[], canvas=None, title=None, digit_size=72, digits_round=4):
    ax = canvas
    if canvas is None:
        fig, ax = plt.subplots()
    im = ax.imshow(matrix)
    
    w, h = matrix.shape
    
    if xlabels is not None:
        ax.set_xticks(np.arange(w))
        ax.set_xticklabels(xlabels)
        
    if ylabels is not None:
        ax.set_yticks(np.arange(h))
        ax.set_yticklabels(ylabels)

    for i in range(h):
        for j in range(w):
            text = ax.text(
                j, i,
                round(matrix[i, j], digits_round),
                ha='center',
                va='center',
                color='w',
                fontdict={ 'size': digit_size }
            )

    if title is not None:
        ax.set_title(title)


def tr_html(cells, tag="td"):
    return "<tr>{}</tr>".format(
        "".join(["<{tag}>{cell}</{tag}>".format(cell=cell, tag=tag) for cell in cells])
    )


def table_html(headers, rows):
    tbl = """<table width="100%" class="htable">
    <thead>{header}</thead>
    <tbody>{body}</tbody>
    </table>"""
    header_html = tr_html(headers, tag="th")
    body_html = "".join([tr_html(row) for row in rows])
    return tbl.format(header=header_html, body=body_html)


def table(headers, rows):
    display(HTML(table_html(headers, rows)))


def printf(string, *args, **kwargs):
    wrapped = "<p>{}</p>".format(string)
    display(HTML(
        wrapped.format(*args, **kwargs)
    ))


def load_styles(path="style.css"):
    file = open(path, "r")
    styles = file.read()
    display(HTML(
        "<style>{}</style>".format(styles)
    ))
 