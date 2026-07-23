class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        pairs= []

        while l < r:
            if people[l] + people[r] <= limit:
                pairs.append([people[l], people[r]])
                l += 1
                r -= 1
            # Right person is too heavy, can't pair them with anyone 
            else:
                pairs.append([people[r]])
                r -= 1

        return len(pairs)

        