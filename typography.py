from gmalthgtparser import HgtParser

import math


n = 34.72581233927868
e = 11.195068359375002

def getElevation(latLong):
    with HgtParser('N34E011.hgt') as parser:
        alt = parser.get_elevation(latLong)
        return alt

print(getElevation((n,e)))

# def convertTileToCoordinates(x, y, z):
#     n = 2.0 ** z
#     long_deg = x / n * 360.0 - 180.0
#     lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
#     lat_deg = lat_rad * 180.0 / math.pi
#     return (lat_deg, long_deg)

# with HgtParser('N34E011.hgt') as parser:
#     print(parser.get_elevation((n,e)))




    # for evel_value in parser.get_value_iterator():
    #     print(evel_value)
    #     break
    # print(parser.get_idx_in_file((n, e)))

    



#print(getElevation(convertTileToCoordinates(8703, 6507, 14)))