from floodsystem.flood import stations_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.geo import stations_within_radius
import matplotlib.dates as dts
from datetime import timedelta
import numpy as np


def severe_warning(stats):
    """function dedicated to severe warnings
    looping over every town name"""
    for s in stats:
        print("\n----SEVERE FLOODING WARNING----\n")
        print("The analysis of data from stations in close proximity suggest that ")
        print(f"the following location is prone to severe flooding: {s}")
        print("Immediate action by local authorities and extensive precautions advised.")
        print(
            "NOTE: This warning is directly dependent on data readings from the relevant station(s).")
        print("The warnings are thus advisory and not definite.")


def high_warning(stats):
    """function dedicated to high warnings
    looping over every town name"""
    for s in stats:
        print("\n----HIGH FLOODING WARNING----\n")
        print("The analysis of data from stations in close proximity suggest that ")
        print(f"the following location is prone to high flooding: {s}")
        print("Caution by local authorities and precautions advised.")
        print("NOTE: This warning is directly dependent on data readings from the relevant station(s).")
        print("The warnings are thus advisory and not definite.")


def moderate_warning(stats):

    """function dedicated to moderate warnings
    looping over every town name"""
    for s in stats:
        print("\n----STATUS: MODERATE HAZARD----\n")
        print("The analysis of data from stations in close proximity suggest that ")
        print(f"the following location is in moderate risk of flooding: {s}")
        print("Caution by local authorities and, if possible, precautions advised for the following days.")
        print("NOTE: This warning is directly dependent on data readings from the relevant station(s).")
        print("The warnings are thus advisory and not definite.")


def low_warning(stats):

    """function dedicated to low warnings
    yielding a list rather than individual warnings is more reasonable
    the number of towns is much greater and there isn't really a warning to be made"""
    print("\n----STATUS: LOW HAZARD----\n")
    print("The analysis of data from stations in close proximity suggest that ")
    print(f"the following locations are in low risk of flooding: {stats}")
    print("No immediate action is required.")
    print("NOTE: This warning is directly dependent on data readings from the relevant station(s).")
    print("The warnings are thus advisory and not definite.")


def run():

    # lists for every station category
    severe_stats = []
    high_stats = []
    moderate_stats = []

    # lists for every town category
    severe_towns = []
    high_towns = []
    moderate_towns = []
    low_towns = []

    # all stations
    low_mod_high_sev = build_station_list()
    # two days chosen as timeframe
    dt = 2

    # filtering wrt relative level or mod-high-sev analysis
    mod_high_sev = stations_over_threshold(low_mod_high_sev, 1.0)

    for stat in mod_high_sev:
        # fetching measure levels for potential stations
        dates, levels = fetch_measure_levels(stat[0].measure_id, dt=timedelta(days=dt))

        # calculating polynomial fit for the trend
        poly, shift = polyfit(dates, levels, 4)
        # derivative of polynomial to estimate change
        poly = poly.deriv()
        # adjusting reference frame to obtain the same interval
        adjusted = dts.date2num(dates)

        # differential lists for the past 24 and 48 hrs as well as the day before
        today_ds = [poly(i) for i in adjusted[len(adjusted) // 2:]]
        prev_day_ds = [poly(i) for i in adjusted[:len(adjusted) // 2]]
        two_day_ds = [poly(i) for i in adjusted]

        # calculating change by mean rate of change * spacing * number of spaces
        today_change = np.mean(today_ds) * len(adjusted) * (adjusted[1] - adjusted[0])
        prev_day_change = np.mean(prev_day_ds) * len(adjusted) * (adjusted[1] - adjusted[0])
        two_day_change = np.mean(two_day_ds) * len(adjusted) * (adjusted[1] - adjusted[0])

        # typical ranges imported
        rel = stat[0].typical_range

        # changes calculated proportionated to the typical range as a measure of hazard
        del_today = 2 * today_change / (rel[1] - rel[0])
        del_prev = 2 * prev_day_change / (rel[1] - rel[0])
        del_gen = 2 * two_day_change / (rel[1] - rel[0])

        """1.5 is chosen as the severe station datum
        this implies a 50% increase which most likely cannot be sustained by most embankments"""
        if stat[1] > 1.5:
            severe_stats.append(stat)
        else:
            # looking into the changes relative to the range as a measure of risk
            if del_gen > 0.1:
                # 10% chosen as severe change since this implies a 10 percent increase
                severe_stats.append(stat)
            elif 0 < del_prev < 0.1 and del_today > 0.05:
                high_stats.append(stat)
            else:
                moderate_stats.append(stat)

    """assessing risks posed to towns by distance
    radius adjustment needs further geographical data (topography)
    for station-specific precision, which cannot be implemented
    through functions and methods within the project's scope

    radii of 1km chosen as equivalent hazard, 4km as one grade below
    filtering stations according to decreasing level of hazard
    no duplicates generated between hazard levels"""

    for stat in severe_stats:
        close_stats = stations_within_radius(low_mod_high_sev, stat[0].coord, 1)
        farther_stats = stations_within_radius(low_mod_high_sev, stat[0].coord, 4)
        for i in close_stats:
            farther_stats.remove(i)
        for c in close_stats:
            if c.town not in severe_towns:
                severe_towns.append(c.town)
        for f in farther_stats:
            if f.town not in high_towns:
                high_towns.append(f.town)

    for stat in high_stats:
        close_stats = stations_within_radius(low_mod_high_sev, stat[0].coord, 1)
        farther_stats = stations_within_radius(low_mod_high_sev, stat[0].coord, 4)
        for i in close_stats:
            farther_stats.remove(i)
        for c in close_stats:
            if c.town not in severe_towns + high_towns:
                high_towns.append(c.town)
        for f in farther_stats:
            if f.town not in moderate_towns:
                moderate_towns.append(f.town)

    for stat in moderate_stats:
        close_stats = stations_within_radius(low_mod_high_sev, stat[0].coord, 1)
        for c in close_stats:
            if c.town not in severe_towns + high_towns + moderate_towns:
                moderate_towns.append(c.town)

    for stat in low_mod_high_sev:
        if stat not in severe_towns + high_towns + moderate_towns + low_towns:
            low_towns.append(stat.town)

    # warnings issued through previously explained functions
    severe_warning(severe_towns)
    high_warning(high_towns)
    moderate_warning(moderate_towns)
    low_warning(low_towns)


if __name__ == "__main__":
    run()
