import datetime

from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels


def run():
    # building list of stations
    stats = build_station_list()
    # extracting five highest relative level stations
    stats = stations_highest_rel_level(stats, 5)
    dt = 10

    for stat in stats:
        # fetching and plotting data levels wrt time
        dates, levels = fetch_measure_levels(stat[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(stat[0], dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
