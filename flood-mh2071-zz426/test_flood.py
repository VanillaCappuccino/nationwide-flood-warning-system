from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.flood import stations_over_threshold, stations_highest_rel_level


def test_stations_over_threshold():
    stats = build_station_list()
    update_water_levels(stats)
    odd = stations_over_threshold(stats, 0.8)
    assert len(odd) > 0


def test_stations_highest_rel_level():
    stats = build_station_list()
    update_water_levels(stats)
    assert len(stations_highest_rel_level(stats, 3)) == 3
