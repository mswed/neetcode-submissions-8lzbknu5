from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We combine position and speed to a single list
        cars = [[p, s] for p, s in zip(position, speed)]
        # We keep a stack of finish times, each finish time
        # represents a fleet (one or more cars that will finish together)
        stack = []

        # We need to process the list in reverse order. The closer the car
        # is to the target the sooner we want to look at it
        cars.sort(key=lambda x: x[0], reverse=True)
        for car in cars:
            # Calculate when it will reach the end
            finish = (target - car[0]) / car[1]
            # We always add the finish to the stack since this is where we'll do our comparisons
            stack.append(finish)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # We have more than one fleet check which will get there faster
                # if the one we just added is faster, it will be slowed by the previous car, so pop it
                stack.pop()

        return len(stack)
