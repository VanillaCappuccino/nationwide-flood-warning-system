from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list


def run():
    # building list of stations
    stats = build_station_list()
    # producing list of stats with highest relative level and their respective relative levels
    stats = stations_highest_rel_level(stats, 10)
    for i in range(10):
        print(stats[i][0].name, stats[i][1])


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
