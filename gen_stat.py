from random import uniform

fp = open('RoadAccident.csv', 'w')
fp.write(r"Speed,%death")
fp.write("\n")

for x in range(485):
    R = x * (75.892038 / 160)
    R = uniform((R-(R*0.15)), (R+(R*0.15)))
    if R >= 100:
        R = 100
    fp.write("{},{}\n".format(x, R))
    last = R