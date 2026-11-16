class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """Neetcode Car fleet problem.

        P.S:
        The position = 1 is not the same as "p1" in F1. Here the positions
        are in the reverse. Which means car at position 4 is ahead of car at
        position 1.

        Giveaway in the question is:

        0 <= position[i] < target
        
        Args:
            target: Target in miles (atleast in my head)
            position: Position of the cars.
            speed: Speed of the cars.
        """
        fleet_times = []
        pos_speed_map = {position[i]: speed[i] for i in range(len(position))}
        sorted_pos_speed_map = {
            car_pos: pos_speed_map[car_pos] for car_pos in sorted(pos_speed_map, reverse=True)
        }

        for car_pos, speed in sorted_pos_speed_map.items():
            car_time = (target - car_pos)/speed

            if fleet_times and fleet_times[-1] >= car_time:
                continue
            fleet_times.append(car_time)
            
        return len(fleet_times)
        