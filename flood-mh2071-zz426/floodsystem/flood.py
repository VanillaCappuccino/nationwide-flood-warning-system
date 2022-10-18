from .stationdata import update_water_levels
from .utils import sorted_by_key


def stations_over_threshold(stations, tol):
    stats = []
    # updates water levels to operate, the levels are None by default
    update_water_levels(stations)
    for station in stations:
        # check to ensure the level - tolerance comparison will not produce an error
        if type(station.relative_water_level()) == float:
            lvl = station.relative_water_level() 
            if lvl > tol:
                # collecting relative levels greater than the tolerance
                stats.append((station, lvl))
    return stats


def stations_highest_rel_level(stations, N):
    # bringing over functionality from prev func
    rivers = stations_over_threshold(stations, 0)
    # yielding highest relative levels by sorting in descending order
    final = sorted_by_key(rivers, 1, reverse=True)
    # slicing to obtain desired length
    return final[:N]
