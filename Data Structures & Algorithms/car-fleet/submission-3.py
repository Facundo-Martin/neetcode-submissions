class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        slowest_time = 0.0
        
        for p, s in pairs:
            time_to_target = (target - p) / s
            
            # We found a new, slower leader that forms its own bottleneck
            if time_to_target > slowest_time:
                fleets += 1
                slowest_time = time_to_target
                
        return fleets