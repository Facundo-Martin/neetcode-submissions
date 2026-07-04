class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair positions with speeds and sort descending (closest to target first)
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for p, s in pairs:
            time_to_target = (target - p) / s
            
            # If the stack is empty, or this car takes LONGER than the fleet ahead
            # it forms a new bottleneck (a new fleet).
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
                
            # If time_to_target <= stack[-1], it catches the fleet ahead.
            # We do nothing, because it gets absorbed into the existing bottleneck.
            
        return len(stack)