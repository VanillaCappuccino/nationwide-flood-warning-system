from floodsystem import station, stationdata


def run():
    # requirements for task f
    stations = stationdata.build_station_list()  # building stations list
    print(station.inconsistent_typical_range_stations(stations))  # inconsistency demo


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
