from floodsystem import geo
from floodsystem.stationdata import build_station_list


def run():
    """requirements for task 1b"""

    # build list of stations
    stations = build_station_list()
    # coordinates of cambridge city centre for the test case.
    ccc = (52.2053, 0.1218)

    final = []  # final list for structured data
    stats = geo.stations_by_distance(stations, ccc)  # implementation of the stations by distance functionality

    for s in stats[:10]:  # generating name - town - distance triples
        final.append((s[0].name, s[0].town, s[1]))
    for s in stats[-10:]:
        final.append((s[0].name, s[0].town, s[1]))

    print(final)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
