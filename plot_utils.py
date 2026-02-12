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
    plot_args["color"] = colour    
    
    pl.plot(x, y, **plot_args)
    pl.xlim(xlim)
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

    pl.xlabel(xlabel, fontproperties=axis_font, fontsize=axis_size)
    pl.ylabel(ylabel, fontproperties=axis_font, fontsize=axis_size)

    pl.xticks(fontproperties=axis_font, fontsize=axis_size)
    pl.yticks(fontproperties=axis_font, fontsize=axis_size)

    pl.title(title, fontproperties=title_font, fontsize=title_size)
    
    pl.legend(legend, fontsize=legend_size) if legend else None
    
    pl.show()


def plot2d_contour(x, y, Z, contour=True, levels=20, cmap='viridis', xlabel=None, ylabel=None, title=None, legend=None, xlim=None, ylim=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    # Check if Z is 1D (scattered data) or 2D (grid data)
    if Z.ndim == 1:
        if contour:
            cs = pl.tricontourf(x, y, Z, levels=levels, cmap=cmap)
        else:
            # For 1D data, pcolormesh won't work easily;
            # we use tricontourf or a scatter plot
            cs = pl.scatter(x, y, c=Z, cmap=cmap)
    else:
        # Your existing code for 2D grids
        X, Y = np.meshgrid(x, y)
        if contour:
            cs = pl.contourf(X, Y, Z, levels=levels, cmap=cmap)
        else:
            cs = pl.pcolormesh(X, Y, Z, shading='auto', cmap=cmap)
    pl.colorbar(cs)

    pl.xlim(xlim)
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

    pl.xlabel(xlabel, fontproperties=axis_font, fontsize=axis_size)
    pl.ylabel(ylabel, fontproperties=axis_font, fontsize=axis_size)

    pl.xticks(fontproperties=axis_font, fontsize=axis_size)
    pl.yticks(fontproperties=axis_font, fontsize=axis_size)

    pl.title(title, fontproperties=title_font, fontsize=title_size)
    
    pl.legend(legend, fontsize=legend_size) if legend else None
    
    pl.show()

def semilogx2d(x, y, xlabel=None, ylabel=None, title=None, legend=None, colour=None, xlim=None, ylim=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    plot_args = {}
    plot_args["color"] = colour    
    
    pl.semilogx(x, y, **plot_args)
    pl.xlim(xlim)
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

    pl.xlabel(xlabel, fontproperties=axis_font, fontsize=axis_size)
    pl.ylabel(ylabel, fontproperties=axis_font, fontsize=axis_size)

    pl.xticks(fontproperties=axis_font, fontsize=axis_size)
    pl.yticks(fontproperties=axis_font, fontsize=axis_size)

    pl.title(title, fontproperties=title_font, fontsize=title_size)
    
    pl.legend(legend, fontsize=legend_size) if legend else None

    pl.show()


def semilogy2d(x, y, xlabel=None, ylabel=None, title=None, legend=None, colour=None, xlim=None, ylim=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    plot_args = {}
    plot_args["color"] = colour    
    
    pl.semilogy(x, y, **plot_args)
    pl.xlim(xlim)
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

    pl.xlabel(xlabel, fontproperties=axis_font, fontsize=axis_size)
    pl.ylabel(ylabel, fontproperties=axis_font, fontsize=axis_size)

    pl.xticks(fontproperties=axis_font, fontsize=axis_size)
    pl.yticks(fontproperties=axis_font, fontsize=axis_size)

    pl.title(title, fontproperties=title_font, fontsize=title_size)
    
    pl.legend(legend, fontsize=legend_size) if legend else None
    
    pl.show()


def loglog2d(x, y, xlabel=None, ylabel=None, title=None, legend=None, colour=None, xlim=None, ylim=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    plot_args = {}
    plot_args["color"] = colour    
    
    pl.loglog(x, y, **plot_args)
    pl.xlim(xlim)
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

    pl.xlabel(xlabel, fontproperties=axis_font, fontsize=axis_size)
    pl.ylabel(ylabel, fontproperties=axis_font, fontsize=axis_size)

    pl.xticks(fontproperties=axis_font, fontsize=axis_size)
    pl.yticks(fontproperties=axis_font, fontsize=axis_size)

    pl.title(title, fontproperties=title_font, fontsize=title_size)
    
    pl.legend(legend, fontsize=legend_size) if legend else None

    pl.show()


def scatter2d(x, y, xlabel=None, ylabel=None, title=None, legend=None, colour=None, xlim=None, ylim=None, size=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None, grid=None, grid_axis='both', grid_color=None, grid_linestyle='-', grid_linewidth=None, grid_transparency=1):
    plot_args = {}
    plot_args["color"] = colour    
    plot_args["s"] = size
    
    pl.scatter(x, y, **plot_args)
    pl.xlim(xlim)
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
                    
    pl.xlabel(xlabel, fontproperties=axis_font, fontsize=axis_size)
    pl.ylabel(ylabel, fontproperties=axis_font, fontsize=axis_size)

    pl.xticks(fontproperties=axis_font, fontsize=axis_size)
    pl.yticks(fontproperties=axis_font, fontsize=axis_size)

    pl.title(title, fontproperties=title_font, fontsize=title_size)
    
    pl.legend(legend, fontsize=legend_size) if legend else None

    pl.show()

# 3d plots
def plot3d(x, y, z, xlabel=None, ylabel=None, zlabel=None, title=None, legend=None, colour=None, axis_font=None, axis_size=None, title_font=None, title_size=None, legend_size=None):
    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_args = {}
    plot_args["color"] = colour
    ax.plot(x, y, z, **plot_args)
    ax.view_init(elev=20, azim=90)

    if xlabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                ax.set_xlabel(xlabel, fontproperties=axis_font, fontsize=axis_size)
            else:
                ax.set_xlabel(xlabel, fontproperties=axis_font)
        elif axis_size is not None:
            ax.set_xlabel(xlabel, fontsize=axis_size)
        else:
            ax.set_xlabel(xlabel)

    if ylabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                ax.set_ylabel(ylabel, fontproperties=axis_font, fontsize=axis_size)
            else:
                ax.set_ylabel(ylabel, fontproperties=axis_font)
        elif axis_size is not None:
            ax.set_ylabel(ylabel, fontsize=axis_size)
        else:
            ax.set_ylabel(ylabel)

    if zlabel is not None:
        if axis_font is not None:
            if axis_size is not None:
                ax.set_zlabel(zlabel, fontproperties=axis_font, fontsize=axis_size)
            else:
                ax.set_zlabel(zlabel, fontproperties=axis_font)
        elif axis_size is not None:
            ax.set_zlabel(zlabel, fontsize=axis_size)
        else:
            ax.set_zlabel(zlabel)

    if title is not None:
        if title_font is not None:
            if title_size is not None:
                ax.set_title(title, fontproperties=title_font, fontsize=title_size)
            else:
                ax.set_title(title, fontproperties=title_font)
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
