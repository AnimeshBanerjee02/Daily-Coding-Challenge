from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        sum_salary = sum(salary) - min_salary - max_salary
        n = len(salary) - 2 # excluding min and max salaries
        return sum_salary / n if n > 0 else 0.0