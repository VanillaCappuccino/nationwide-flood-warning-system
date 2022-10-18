import matplotlib.pyplot as plt
from .analysis import polyfit
import matplotlib.dates as dts


def plot_water_levels(station, dates, levels):

    # adjusting plotting parameters
    plt.plot(dates, levels, "-r", label = "River water level")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=90)
    plt.title(station.name)

    # highlighting interval for typical range
    plt.axhspan(station.typical_range[0], station.typical_range[1], color='blue', alpha=0.2, label="Typical range")
    # adding legend to plot
    plt.legend(loc="upper right")
    plt.tight_layout()

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):

    # the intention was to bring over the prev func but the show command made this infeasible
    # the plot adjustments were therefore made again

    # obtaining fitted polynomial and norm shift
    poly, shift = polyfit(dates,levels,4)
    plt.plot(dates,poly(dts.date2num(dates)), "-g", label = "Polynomial fit")

    # parameter adjustment
    plt.plot(dates, levels, "-r", label = "River water level")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=90)
    plt.title(station.name)

    # highlighting typical range
    plt.axhspan(station.typical_range[0], station.typical_range[1], color='blue', alpha=0.2, label="Typical range")
    plt.legend(loc="upper right")
    plt.tight_layout()

    plt.show()
