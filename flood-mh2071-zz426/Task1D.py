from floodsystem import geo, stationdata


def run():
    # requirements for task d
    stations = stationdata.build_station_list()  # building list of stations
    final = sorted(geo.rivers_with_station(stations))
    # implementing rivers with stations
    print("{} stations in total. The first 10 alphabetically are: {}".format(len(final), final[:10]))
    # printing the 10 stations

    sorts = geo.stations_by_river(stations)  # compiling the stations by river
    for k in ["River Aire", "River Cam", "River Thames"]:
        print("\n")
        print(k + ": " + str(sorted(sorts[k])))
        # printing the stations corresponding to the three rivers alphabetically


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
