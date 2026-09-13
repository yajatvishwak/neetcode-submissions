class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        meta = 0
        fleet = 0

        car = zip(position, speed)
        
        car = sorted(car, reverse = True)

        for (p,s) in car:
            eta = (target-p) / s
            if eta > meta:
                meta = eta
                fleet += 1
        return fleet
        