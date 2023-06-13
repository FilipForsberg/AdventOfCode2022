def manhattan_distance(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class sensor:

    def __init__(self, position, nearest_beacon):
        self.position = position
        self.nearest_beacon = nearest_beacon
        self.range: int = manhattan_distance(self.position, nearest_beacon)

    def in_range(self, point):
        return self.range >= manhattan_distance(self.position, point)

def parse_input(string: input) -> list:
    result = []

    for line in string.splitlines():
        left, right = line.split(": ")

        sensor_x, sensor_y = left[12:].split(",")
        sensor_x = int(sensor_x)
        sensor_y = int(sensor_y[3:])
        #print(sensor_x, sensor_y)


        beacon_x, beacon_y = right[23:].split(",")
        beacon_x = int(beacon_x)
        beacon_y = int(beacon_y[3:])

        new_sensor = sensor((sensor_x, sensor_y) , (beacon_x ,beacon_y))
        result.append(new_sensor)
    return result
