import numpy as np
import matplotlib.pyplot as plt
from colorhash import ColorHash
import pandas as pd


def html_pivot_table(arr):
    """creates an html pivot table from a 2d array"""

    some_prop, counts = np.unique(arr, return_counts=True)
    
    # show percentage (optional) instead of actual data
    counts = ["%.2f" % (c/sum(counts)*100) for c in counts]
    html = """<table><tr><th>Some Property</th><th>UNIQUE COUNT</th></tr>"""
    for i in range(0, len(some_prop)):
        if some_prop[i]:
            [some_prop_name] = some_prop[i]
            html += """<tr><td>{0}</td><td>{1}</td></tr>""".format(some_prop_name, counts[i])
    html += """</table>"""
    return html


def plot_line_chart(title, data_table, series_labels, category_labels, 
    colors=None, x_label=None, y_label=None):
    """create a matplotlib line chart"""

    # get all points / data
    data = []
    for i in range(0, len(data_table[0])):
        data[i] = list([f[i] for f in data_table])
    # total data
    total_data = list([sum(f[i]) for f in data_table])

    # create panda data frame
    df = pd.DataFrame({'x': category_labels, 'y1': data[0], 'y2': data[1], 'y3': data[2], 'y4': total_data})
    
    # chart figure properties, 
    # (Tip: ideal values provided, do not modify dimensions)
    plt.figure(figsize=(15, 10))
    plt.title(title)
    plt.grid(True)
    
    plt.plot('x', 'y1', label=series_labels[0], data=df, marker='o', color=colors[0], linewidth=4)
    plt.plot('x', 'y2', label=series_labels[1], data=df, marker='o', color=colors[1], linewidth=4)
    plt.plot('x', 'y3', label=series_labels[2], data=df, marker='o', color=colors[2], linewidth=4)
    plt.plot('x', 'y4', label=series_labels[3], data=df, marker='o', color=colors[3], linewidth=4)
    
    plt.xticks(category_labels)
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    plt.legend()
    
    plt.savefig('line_chart.png')


def plot_pie_chart(title, labels, sizes):
    """create a matplotlib pie chart"""

    # chart figure properties, 
    # (Tip: ideal values provided, do not modify dimensions)
    plt.figure(figsize=(16, 12))
    plt.title(title)

    colors = []
    for s in labels:
        colors.append(str(ColorHash(s).hex))

    patches, text = plt.pie(sizes, colors=colors, startangle=90)
    
    # some nice data showing on legends
    legends = [labels[i] + ": " + sizes[i] + "%" for i in range(0, len(labels) - 1)]
    plt.legend(patches, labels=legends, loc="center right", bbox_to_anchor=(1, 0.5), fontsize=10,
               bbox_transform=plt.gcf().transFigure)
    
    # Tip: DO NOT change this, very crucial for side-by-side legend / chart balance
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.6)
    
    plt.axis('equal')
    plt.tight_layout()
    
    plt.savefig('pie_chart.png')


# src: https://stackoverflow.com/a/50205834/2453382
def plot_stacked_bar(title, data_table, series_labels, show_values=False, value_format="{}", x_label=None, y_label=None,
                     colors=None, grid=True, reverse=False):
    """create a matplotlib pie chart"""

    data = list([f[i] for f in data_table] for i in [0, len(data_table[0])])

    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    category_labels = [f[0] for f in data_table]
    if reverse:
        data = np.flip(data, axis=1)
        category_labels = reversed(category_labels)

    plt.figure(figsize=(15, 10))
    plt.title(title)
    plt.grid(True)

    for i, row_data in enumerate(data):
        color = colors[i] if colors is not None else None
        axes.append(plt.bar(ind, row_data, bottom=cum_size,
                            label=series_labels[i], color=color))
        cum_size += row_data

    if category_labels:
        plt.xticks(ind, category_labels)

    if y_label:
        plt.ylabel(y_label)

    if x_label:
        plt.xlabel(x_label)

    plt.legend()

    if grid:
        plt.grid()

    if show_values:
        for axis in axes:
            for bar in axis:
                w, h = bar.get_width(), bar.get_height()
                plt.text(bar.get_x() + w / 2, bar.get_y() + h / 2,
                         value_format.format(int(h)), ha="center",
                         va="center")

    plt.savefig('bar_chart.png')
