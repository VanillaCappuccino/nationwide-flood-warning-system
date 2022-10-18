# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem import station


def test_create_monitoring_station():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    return s


def test_consistency():
    # test for the consistency function.
    st = test_create_monitoring_station()
    assert st.typical_range_consistent()
    assert station.inconsistent_typical_range_stations([st]) == []


def test_relative_water_level():
    s = test_create_monitoring_station()
    s.latest_level = -2.3
    q = test_create_monitoring_station()
    q.latest_level = 3.4445
    assert s.relative_water_level() == 0
    assert q.relative_water_level() == 1
