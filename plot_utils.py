# import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pl
import numpy as np

# 2d plots
# when customising, check available fonts and colours online
# https://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/    for fonts
# https://matplotlib.org/stable/gallery/color/named_colors.html    for colours


def plot2d(x, y, xlabel=None, ylabel=None, title=None, legend=None, colour=None, xlim=None, ylim=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    plot_args = {}
    if colour is not None:
        plot_args["color"] = colour
    pl.plot(x, y, **plot_args)
    if xlim is not None:
        pl.xlim(xlim)
    if ylim is not None:
        pl.ylim(ylim)

    if grid is not None:
        if grid_color is not None:
            if grid_linewidth is not None:
                pl.grid(axis=grid_axis, color=grid_color, linestyle=grid_linestyle,
                        linewidth=grid_linewidth, alpha=grid_transparency)
            else:
                pl.grid(axis=grid_axis, color=grid_color,
                        linestyle=grid_linestyle, alpha=grid_transparency)
        elif grid_linewidth is not None:
            pl.grid(axis=grid_axis, linestyle=grid_linestyle,
                    linewidth=grid_linewidth, alpha=grid_transparency)

    if xlabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.xlabel(xlabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.xlabel(xlabel, fontname=axis_font)
        elif axis_size is not None:
            pl.xlabel(xlabel, fontsize=axis_size)
        else:
            pl.xlabel(xlabel)

    if ylabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.ylabel(ylabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.ylabel(ylabel, fontname=axis_font)
        elif axis_size is not None:
            pl.ylabel(xlabel, fontsize=axis_size)
        else:
            pl.ylabel(xlabel)

    if title is not None:
        if title_font is not None:
            if title_size is not None:
                pl.title(title, fontname=title_font, fontsize=title_size)
            else:
                pl.title(title, fontname=title_font)
        elif title_size is not None:
            pl.title(title, fontsize=title_size)
        else:
            pl.title(title)

    if legend is not None:
        if legend_size is not None:
            pl.legend(legend, fontsize=legend_size)
        else:
            pl.legend(legend)
    pl.show()


def semilogx2d(x, y, xlabel=None, ylabel=None, title=None, legend=None, colour=None, xlim=None, ylim=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    plot_args = {}
    if colour is not None:
        plot_args["color"] = colour
    pl.semilogx(x, y, **plot_args)
    if xlim is not None:
        pl.xlim(xlim)
    if ylim is not None:
        pl.ylim(ylim)

    if grid is not None:
        if grid_color is not None:
            if grid_linewidth is not None:
                pl.grid(axis=grid_axis, color=grid_color, linestyle=grid_linestyle,
                        linewidth=grid_linewidth, alpha=grid_transparency)
            else:
                pl.grid(axis=grid_axis, color=grid_color,
                        linestyle=grid_linestyle, alpha=grid_transparency)
        elif grid_linewidth is not None:
            pl.grid(axis=grid_axis, linestyle=grid_linestyle,
                    linewidth=grid_linewidth, alpha=grid_transparency)

    if xlabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.xlabel(xlabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.xlabel(xlabel, fontname=axis_font)
        elif axis_size is not None:
            pl.xlabel(xlabel, fontsize=axis_size)
        else:
            pl.xlabel(xlabel)

    if ylabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.ylabel(ylabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.ylabel(ylabel, fontname=axis_font)
        elif axis_size is not None:
            pl.ylabel(xlabel, fontsize=axis_size)
        else:
            pl.ylabel(xlabel)

    if title is not None:
        if title_font is not None:
            if title_size is not None:
                pl.title(title, fontname=title_font, fontsize=title_size)
            else:
                pl.title(title, fontname=title_font)
        elif title_size is not None:
            pl.title(title, fontsize=title_size)
        else:
            pl.title(title)

    if legend is not None:
        if legend_size is not None:
            pl.legend(legend, fontsize=legend_size)
        else:
            pl.legend(legend)
    pl.show()


def semilogy2d(x, y, xlabel=None, ylabel=None, title=None, legend=None, colour=None, xlim=None, ylim=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    plot_args = {}
    if colour is not None:
        plot_args["color"] = colour
    pl.semilogy(x, y, **plot_args)
    if xlim is not None:
        pl.xlim(xlim)
    if ylim is not None:
        pl.ylim(ylim)

    if grid is not None:
        if grid_color is not None:
            if grid_linewidth is not None:
                pl.grid(axis=grid_axis, color=grid_color, linestyle=grid_linestyle,
                        linewidth=grid_linewidth, alpha=grid_transparency)
            else:
                pl.grid(axis=grid_axis, color=grid_color,
                        linestyle=grid_linestyle, alpha=grid_transparency)
        elif grid_linewidth is not None:
            pl.grid(axis=grid_axis, linestyle=grid_linestyle,
                    linewidth=grid_linewidth, alpha=grid_transparency)

    if xlabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.xlabel(xlabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.xlabel(xlabel, fontname=axis_font)
        elif axis_size is not None:
            pl.xlabel(xlabel, fontsize=axis_size)
        else:
            pl.xlabel(xlabel)

    if ylabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.ylabel(ylabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.ylabel(ylabel, fontname=axis_font)
        elif axis_size is not None:
            pl.ylabel(xlabel, fontsize=axis_size)
        else:
            pl.ylabel(xlabel)

    if title is not None:
        if title_font is not None:
            if title_size is not None:
                pl.title(title, fontname=title_font, fontsize=title_size)
            else:
                pl.title(title, fontname=title_font)
        elif title_size is not None:
            pl.title(title, fontsize=title_size)
        else:
            pl.title(title)

    if legend is not None:
        if legend_size is not None:
            pl.legend(legend, fontsize=legend_size)
        else:
            pl.legend(legend)
    pl.show()


def loglog2d(x, y, xlabel=None, ylabel=None, title=None, legend=None, colour=None, xlim=None, ylim=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    plot_args = {}
    if colour is not None:
        plot_args["color"] = colour
    pl.loglog(x, y, **plot_args)
    if xlim is not None:
        pl.xlim(xlim)
    if ylim is not None:
        pl.ylim(ylim)

    if grid is not None:
        if grid_color is not None:
            if grid_linewidth is not None:
                pl.grid(axis=grid_axis, color=grid_color, linestyle=grid_linestyle,
                        linewidth=grid_linewidth, alpha=grid_transparency)
            else:
                pl.grid(axis=grid_axis, color=grid_color,
                        linestyle=grid_linestyle, alpha=grid_transparency)
        elif grid_linewidth is not None:
            pl.grid(axis=grid_axis, linestyle=grid_linestyle,
                    linewidth=grid_linewidth, alpha=grid_transparency)

    if xlabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.xlabel(xlabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.xlabel(xlabel, fontname=axis_font)
        elif axis_size is not None:
            pl.xlabel(xlabel, fontsize=axis_size)
        else:
            pl.xlabel(xlabel)

    if ylabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.ylabel(ylabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.ylabel(ylabel, fontname=axis_font)
        elif axis_size is not None:
            pl.ylabel(xlabel, fontsize=axis_size)
        else:
            pl.ylabel(xlabel)

    if title is not None:
        if title_font is not None:
            if title_size is not None:
                pl.title(title, fontname=title_font, fontsize=title_size)
            else:
                pl.title(title, fontname=title_font)
        elif title_size is not None:
            pl.title(title, fontsize=title_size)
        else:
            pl.title(title)

    if legend is not None:
        if legend_size is not None:
            pl.legend(legend, fontsize=legend_size)
        else:
            pl.legend(legend)
    pl.show()


def scatter2d(x, y, xlabel=None, ylabel=None, title=None, legend=None, colour=None, xlim=None, ylim=None, size=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    plot_args = {}
    if colour is not None:
        plot_args["color"] = colour
    if size is not None:
        plot_args["s"] = size
    pl.scatter(x, y, **plot_args)
    if xlim is not None:
        pl.xlim(xlim)
    if ylim is not None:
        pl.ylim(ylim)

    if grid is not None:
        if grid_color is not None:
            if grid_linewidth is not None:
                pl.grid(axis=grid_axis, color=grid_color, linestyle=grid_linestyle,
                        linewidth=grid_linewidth, alpha=grid_transparency)
            else:
                pl.grid(axis=grid_axis, color=grid_color,
                        linestyle=grid_linestyle, alpha=grid_transparency)
        elif grid_linewidth is not None:
            pl.grid(axis=grid_axis, linestyle=grid_linestyle,
                    linewidth=grid_linewidth, alpha=grid_transparency)

    if xlabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.xlabel(xlabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.xlabel(xlabel, fontname=axis_font)
        elif axis_size is not None:
            pl.xlabel(xlabel, fontsize=axis_size)
        else:
            pl.xlabel(xlabel)

    if ylabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                pl.ylabel(ylabel, fontname=axis_font, fontsize=axis_size)
            else:
                pl.ylabel(ylabel, fontname=axis_font)
        elif axis_size is not None:
            pl.ylabel(xlabel, fontsize=axis_size)
        else:
            pl.ylabel(xlabel)

    if title is not None:
        if title_font is not None:
            if title_size is not None:
                pl.title(title, fontname=title_font, fontsize=title_size)
            else:
                pl.title(title, fontname=title_font)
        elif title_size is not None:
            pl.title(title, fontsize=title_size)
        else:
            pl.title(title)

    if legend is not None:
        if legend_size is not None:
            pl.legend(legend, fontsize=legend_size)
        else:
            pl.legend(legend)
    pl.show()

# 3d plots


def plot3d(x, y, z, xlabel=None, ylabel=None, zlabel=None, title=None, legend=None, colour=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None):
    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_args = {}
    if colour is not None:
        plot_args["color"] = colour
    ax.plot(x, y, z, **plot_args)
    ax.view_init(elev=20, azim=90)

    if xlabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                ax.set_xlabel(xlabel, fontname=axis_font, fontsize=axis_size)
            else:
                ax.set_xlabel(xlabel, fontname=axis_font)
        elif axis_size is not None:
            ax.set_xlabel(xlabel, fontsize=axis_size)
        else:
            ax.set_xlabel(xlabel)

    if ylabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                ax.set_ylabel(ylabel, fontname=axis_font, fontsize=axis_size)
            else:
                ax.set_ylabel(ylabel, fontname=axis_font)
        elif axis_size is not None:
            ax.set_ylabel(ylabel, fontsize=axis_size)
        else:
            ax.set_ylabel(ylabel)

    if zlabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                ax.set_zlabel(zlabel, fontname=axis_font, fontsize=axis_size)
            else:
                ax.set_zlabel(zlabel, fontname=axis_font)
        elif axis_size is not None:
            ax.set_zlabel(zlabel, fontsize=axis_size)
        else:
            ax.set_zlabel(zlabel)

    if title is not None:
        if title_font is not None:
            if title_size is not None:
                ax.set_title(title, fontname=title_font, fontsize=title_size)
            else:
                ax.set_title(title, fontname=title_font)
        elif title_size is not None:
            ax.set_title(title, fontsize=title_size)
        else:
            ax.set_title(title)

    if legend is not None:
        if legend_size is not None:
            ax.legend(legend, fontsize=legend_size)
        else:
            ax.legend(legend)
    pl.show()
