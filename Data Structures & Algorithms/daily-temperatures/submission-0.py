class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create a list of days until higher temp
        res = [0] * len(temperatures)

        # Create a stack to figure out how many days passed?
        stack = []

        # For each day, count the days forward until you get the result
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
            elif temp <= stack[-1][0]:
                stack.append((temp, i))
            else:
                while stack and temp > stack[-1][0]:
                    previous_temp = stack.pop()
                    difference = i - previous_temp[1]
                    res[previous_temp[1]] = difference

                stack.append((temp, i))

        return res
