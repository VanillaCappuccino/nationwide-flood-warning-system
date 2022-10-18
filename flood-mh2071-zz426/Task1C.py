from floodsystem import geo, stationdata


def run():
    # requirements for task c

    stations = stationdata.build_station_list()  # obtaining stations list
    stats = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)
    # implementing requested functionality for stations within a given radius
    final = sorted([x.name for x in stats])  # sorting the results alphabetically
    print(final)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
