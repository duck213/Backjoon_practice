from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    loading = deque([0] * bridge_length)
    bridge_pound = 0
    while loading:
        time += 1
        bridge_pound -= loading.popleft()
        if truck_weights:
            if bridge_pound+truck_weights[0] <= weight:
                bridge_pound+=truck_weights[0]
                loading.append(truck_weights.popleft())
            else:
                loading.append(0)

    return time