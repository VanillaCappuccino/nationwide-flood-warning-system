# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self): # method for consistency
        rng = self.typical_range
        if type(rng) == tuple and len(rng) == 2 and rng[0] <= rng[1]:
            # checking whether a tuple with length two and with ascending range values is obtained
            return True
        else:
            return False

    
    def relative_water_level(self):
        # first check to make sure the latest water level is a (somewhat) valid value
        cond = type(self.latest_level) == float
        # combining the initial check with the range consistency function from milestone 1 to mitigate erroneous range values
        if self.typical_range_consistent() and cond:
            # this simple algebraic expression will produce 0 for the lower range boundary, 1 for the upper range boundary
            difference = self.typical_range[1] - self.typical_range[0]
            margin = self.latest_level - self.typical_range[0]
            return margin / difference
        else:
            # returning none if the values are not suitable for operation
            return None


def inconsistent_typical_range_stations(stations):
    incs = []
    for station in stations:
        if not station.typical_range_consistent():
        # running the built-in conditional check method on every station and building up a list of inconsistent stations
            incs.append(station.name)
    incs.sort()
    return incs
