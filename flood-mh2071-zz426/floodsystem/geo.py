# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from .utils import sorted_by_key


def stations_by_distance(stations, p):
    sdp = []  
    # an empty list to include the stations

    # looping over station coordinates to calculate distances and associate.
    for station in stations: 
        coord = station.coord
        distance = haversine(p,coord, unit=Unit.KILOMETERS)  # using haversine library to calculate spherical distances
        sdp.append((station, distance))

    # sorting by distance with built-in functionality
    sdp = sorted_by_key(sdp, 1)

    return sdp


def stations_within_radius(stations, centre, r):
    sdp = []  
    # an empty list to include the stations

    # looping over station coordinates to calculate distances and associate.
    for station in stations: 
        coord = station.coord
        distance = haversine(centre,coord, unit=Unit.KILOMETERS)
        sdp.append((station, distance))

    # sorting by distance with built-in functionality
    sdp = sorted_by_key(sdp, 1)

    final = []

    # sequential check comes in handy to narrow down the range of operation by going in ascending order
    for i in range(len(sdp)):
        if sdp[i][1] <= r:
            final.append(sdp[i][0])

    return final


def rivers_with_station(stations):
    rivers  = []
    for station in stations: # creating a list with unique elements (effectively a set but implemented with this data structure for added functionality)
        if station.river not in rivers:
            rivers.append(station.river)
    return rivers


def stations_by_river(stations):
    rivers = rivers_with_station(stations) # obtaining a list of rivers with stations
    rivers_dict = {}
    for river in rivers:
        stats = []
        for station in stations:
            if station.river == river:
                stats.append(station.name)
        rivers_dict[river] = stats
    return rivers_dict


def rivers_by_station_number(stations, N):
    rivers = rivers_with_station(stations)
    stats = stations_by_river(stations)  # implementing previous function
    nums_set = []  # station numbers set
    numbs = []  # station - number pairs
    final = []  
    # final container for n different counts to enable the inclusion of multiple rivers with same station number
    for river in rivers:
            length = len(stats[river])
            numbs.append((river, length))
    numbs = sorted_by_key(numbs, 1, True)
    
    for s in numbs:
        final.append(s)
        if s[1] not in nums_set:
            nums_set.append(s[1])
        if len(nums_set) == N:
            break  # continuing to add to final list until n different counts are reached

    return final
