from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from datetime import timedelta


def run():
    # build stations list
    stats = build_station_list()
    # time interval of two days
    dt = 2
    # five highest relative level stations
    stats = stations_highest_rel_level(stats, 5)
    for stat in stats:
        # fetching and plotting
        dates, levels = fetch_measure_levels(stat[0].measure_id, dt=timedelta(days=dt))
        plot_water_level_with_fit(stat[0], dates, levels, dt)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
