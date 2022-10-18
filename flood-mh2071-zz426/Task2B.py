from floodsystem import flood, stationdata
from floodsystem.utils import sorted_by_key


def run():
    # building stations list, as per usual
    stats_list = stationdata.build_station_list()
    # obtaining a list containing stations above the threshold tolerance
    faulty = flood.stations_over_threshold(stats_list, 0.8)
    final = []
    # reducing the values down to station names and relative levels
    for f in faulty:
        final.append((f[0].name, f[1]))
    # sorting by decreasing relative water level
    final = sorted_by_key(final, 1, reverse=True)
    for f in final:
        print(f[0], f[1])


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
