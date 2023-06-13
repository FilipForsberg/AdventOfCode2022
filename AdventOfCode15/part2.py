import helpFunctions


def main(input: str, search_area) -> int:
    sensor_beacon_pairs = helpFunctions.parse_input(input)
    all_parallel_lines = []

    #Gets all lines that are parallel to each sensor boundries
    for current_sensor in sensor_beacon_pairs:
        all_parallel_lines += sensor_boundary_parallels(current_sensor)

    """
    The 4 different parallel lines
    {
        nw = north to west line (ascending)
        ne = north to east line (descending)
        es = east to south line (ascending)
        sw = south to west line (descending)
    }
    """
    nw_lines = all_parallel_lines[0::4]
    ne_lines = all_parallel_lines[1::4]
    es_lines = all_parallel_lines[2::4]
    sw_lines = all_parallel_lines[3::4]

    ascending_lines = []
    descending_lines = []

    #If a line exists in both ascending -> add to ascending
    #If a line exists in both descending -> add to descending
    for current_line in nw_lines:
        if current_line in es_lines:
            ascending_lines.append(current_line)
    for current_line in ne_lines:
        if current_line in sw_lines:
            descending_lines.append(current_line)

    points = []

    #Calculates the intersection point of all chosen lines
    for ascending in ascending_lines:
        for descending in descending_lines:
            x = (descending[1] - ascending[1]) // 2
            y = x + ascending[1]
            point = (x,y)
            points.append(point)

    """
        Check every valid points if it full fills our conditions
        1: The point is within our search area
        2: The point is not inside any sensor's range
    """
    for point in points:
        if (
            0 <= point[1] <= search_area[1]
            and 0 <= point[0] <= search_area[0]
            and is_not_in_range(point,sensor_beacon_pairs)
        ):
            return point[0] * 4000000 + point[1]


def sensor_boundary_parallels(sensor):
    sensor_x = sensor.position[0]
    sensor_y = sensor.position[1]
    epsilon = sensor.range


    #The 4 most outer points of the sensor boundry {west,north, east, south}
    sensor_w = (sensor_x - epsilon, sensor_y)
    sensor_n = (sensor_x, sensor_y + epsilon)
    sensor_e = (sensor_x + epsilon, sensor_y)
    sensor_s = (sensor_x, sensor_y - epsilon)

    """
        The 4 different lines im interested in
        Given as [bool, int]
        Bool gives if its ascending or descending  (-1 or 1 in the line equation)
        The int is the m in the line equation
        
        Line equation: y = kx + m
    """

    k_m_west_north = [True,sensor_w[1] - sensor_w[0] + 1]
    k_m_north_east = [False, sensor_n[1] + 1 + sensor_n[0]]
    k_m_east_south = [True, sensor_e[1] - sensor_e[0] -1]
    k_m_south_west = [False, sensor_s[1] + sensor_s[0] - 1]

    parallel_lines = [k_m_west_north, k_m_north_east , k_m_east_south , k_m_south_west]

    return parallel_lines


def is_not_in_range(point, sensors):
    for sensor in sensors:
        if sensor.in_range(point):
            return False
    return True

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    search_area = 4000000,4000000

    print(main(input, search_area))