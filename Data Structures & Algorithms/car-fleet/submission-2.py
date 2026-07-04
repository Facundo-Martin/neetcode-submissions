class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair positions with speeds and sort descending (closest to target first)
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for p, s in pairs:
            # Calculate and append theoretical empty-road time to target
            stack.append((target - p) / s)
            
            # If there are at least 2 elements on the stack, and the car behind (stack[-1])
            # arrives faster than or at the same time as the car in front (stack[-2]):
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # They collide and merge. The faster car (stack[-1]) joins the fleet
                # and is governed by the slower car (stack[-2]). We pop the faster car.
                stack.pop()
            
        return len(stack)