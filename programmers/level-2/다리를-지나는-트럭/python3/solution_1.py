# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# time complexity: O(N \times L)
# space complexity: O(N + L)
def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    time = 0
    queue = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0
    
    while queue:
        time += 1
        exited_truck = queue.popleft()
        current_weight -= exited_truck
        
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.popleft()
                queue.append(new_truck)
                current_weight += new_truck
            else:
                queue.append(0)
                
    return time
