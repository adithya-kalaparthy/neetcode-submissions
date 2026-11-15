class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        unsolved_days = []
        for curr_day, curr_temp in enumerate(temperatures):
            while unsolved_days and temperatures[unsolved_days[-1]] < curr_temp:
                prev_day = unsolved_days.pop()
                # Calculate the difference between current and previous days
                result[prev_day] = curr_day - prev_day
            unsolved_days.append(curr_day)
            
        return result