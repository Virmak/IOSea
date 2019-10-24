import re
import json

oceanMassList = []

f = open("../ocean_mass_200204_201706.txt")
oceanMass = f.read()



for row in oceanMass.split('\n')[35+114:]:
    data = row.split()
    if (len(data) == 4):
        oceanMassList.append({"date": data[0], "sea_level": data[1], "uncertainty": data[2]})


of = open("test_data.json", "w")
of.write(json.dumps(oceanMassList))
of.close()

print(len(oceanMassList))