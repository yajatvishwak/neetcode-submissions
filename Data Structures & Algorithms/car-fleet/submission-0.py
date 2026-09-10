class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = sorted(zip(position, speed),reverse = True)
        fleet = 0
        prev = 0
        for (p,s) in zipped:
            eta = (target - p) / s
            if prev < eta:
                fleet += 1
                prev = eta
        return fleet
        