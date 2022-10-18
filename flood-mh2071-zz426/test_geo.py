from floodsystem import geo
from test_station import test_create_monitoring_station


def test_distance():
    # test for haversine distance
    st = test_create_monitoring_station()
    st2 = test_create_monitoring_station()
    st2.coord = (2, 3)
    g = geo.stations_by_distance([st, st2], (0, 0))
    assert round(g[1][1], 1) == 497.2 and round(g[0][1], 1) == 400.9


def test_radius():
    # test for correct output with stations within radius
    st = test_create_monitoring_station()
    st2 = test_create_monitoring_station()
    st2.coord = (2, 3)
    g = geo.stations_within_radius([st, st2], (0, 0), 450)
    assert len(g) == 1 and g[0] == st2


def test_rivers_with_station():
    # test for correct stations for a river
    st = test_create_monitoring_station()
    mt = geo.stations_by_river([st])
    assert type(mt) == dict and len(mt[st.river]) != 0


def test_rivers_by_station_number():
    # test specifically for case where a number of stations exist in multiple rivers
    stats = []
    for i in range(11):
        st = test_create_monitoring_station()
        st.name = "station" + "{}".format(i + 1)
        st.river = "river" + "{}".format(i % 3)
        stats.append(st)

    numbers = geo.rivers_by_station_number(stats, 2)
    nums = geo.rivers_by_station_number(stats, 3)

    assert numbers == nums
