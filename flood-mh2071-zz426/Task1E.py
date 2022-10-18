from floodsystem import geo, stationdata


def run():
    stations = stationdata.build_station_list()  # building list of stations
    lst = geo.rivers_by_station_number(stations, 9)  # demo functionality for the greatest no of stations
    print(lst)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
