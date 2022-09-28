import json
import math


def distance(A: list, B: list) -> float:
    x = B[0] - A[0]
    y = B[1] - A[1]
    return math.sqrt(x**2 + y**2)


def optimal_order(places: dict, init: str) -> list:
    # Places -> {A : (x, y), ...}
    # Init -> "B"
    if not places:
        return []

    init_pos = places.pop(init)
    short_key = ''
    short_dist = math.inf

    for key in places:
        dist = distance(init_pos, places[key])
        if dist < short_dist:
            short_dist = dist
            short_key = key

    return [init] + optimal_order(places, short_key)


def _optimal_time(times: dict) -> list:
    # tIMES -> {A: 2.30, ...} Dos horas y media
    order = []
    while times:
        max_time = max(times, key=times.get)
        order.append(max_time)
        times.pop(max_time)
    return order


def optimal_time(times: dict) -> list:
    # Pythonic way
    sorted_keys = sorted(
        times,
        key=times.get,
        reverse=True
    )
    return sorted_keys


if __name__ == '__main__':
    f = open('input.json')
    data = json.load(f)

    places = data["places"]
    times = data["times"]
    init = data["init"]

    opt_dist = optimal_order(places, init)
    opt_time = optimal_time(times)

    print("Optimal path:")
    print("  Distances:", "->".join(map(str, opt_dist)))
    print("  Times:", "->".join(map(str, opt_time)))
