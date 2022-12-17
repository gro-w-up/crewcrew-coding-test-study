from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    now = 0

    truck_on_bridge = deque(bridge_length * [0])
    truck_weights = deque(truck_weights)

    while len(truck_on_bridge):
        answer += 1

        now -= truck_on_bridge[0]
        truck_on_bridge.popleft()

        if truck_weights:
            if now + truck_weights[0] <= weight:
                now += truck_weights[0]
                truck_on_bridge.append(truck_weights.popleft())
            else:
                truck_on_bridge.append(0)

    return answer