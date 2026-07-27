class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Cool trick but Onlogn time instead of Onlogk with heap
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]