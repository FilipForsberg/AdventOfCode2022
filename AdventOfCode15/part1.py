import helpFunctions
def get_sensor_candidates(sensors, y_line: int):
    sensor_candidates = []
    #Returns every sensor which has the given y_line passing through its boundry
    for current_sensor in sensors:
        if y_line <= current_sensor.position[1] + current_sensor.range and y_line >= current_sensor.position[1] - current_sensor.range:
            sensor_candidates.append(current_sensor)
    return sensor_candidates


def main(input: str, y_line) -> int:
    sensor_beacon_pairs = helpFunctions.parse_input(input)
    sensor_candidates = get_sensor_candidates(sensor_beacon_pairs,y_line)

    blocked_tiles = get_blocked_coordinates_total(sensor_candidates, y_line)

    #Test gives 26
    #Input gives 5083287
    return len(blocked_tiles)

def get_blocked_coordinates_total(sensor_candidates, y_line) -> int:
    blocked_points = set()
    for current_sensor in sensor_candidates:
        sensor_y_pos = current_sensor.position[1]
        sensor_x_pos = current_sensor.position[0]
        epsilon = current_sensor.range
        if y_line > sensor_y_pos:
            #Its in upper half of sensor
            x = sensor_x_pos - epsilon + y_line - sensor_y_pos

        elif y_line < sensor_y_pos:
            #Its bottom half of sensor
            x = sensor_x_pos - epsilon - y_line + sensor_y_pos
        elif sensor_y_pos == y_line:
            #Its in the middle
            x = sensor_x_pos - epsilon
            break
        else:
            raise Exception("Input is wrong")

        #The location of the 2nd intersection of sensor boundry
        x_2 = sensor_x_pos + abs(sensor_x_pos - x)

        #Goes through the x value of all points that intersects
        for x_pos_blocked in range(x, x_2):
            #Adds them to a set
            blocked_points.add((x_pos_blocked, y_line))

    return blocked_points


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    # y_line = 10 #test
    y_line = 2000000 #real

    print(main(input, y_line))