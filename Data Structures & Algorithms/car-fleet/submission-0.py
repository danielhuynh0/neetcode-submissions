class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars_stack = sorted(cars) # lambda x: x[0] but auto sorts by tuple's first element in asc
        
        fleets = 1
        fleet_car = cars_stack.pop()

        fleet_to_reach = (target - fleet_car[0])/fleet_car[1] 

        while cars_stack:
            cur = cars_stack.pop()

            to_reach = (target - cur[0])/cur[1]

            if to_reach > fleet_to_reach:
                fleets += 1
                fleet_to_reach = to_reach

        return fleets