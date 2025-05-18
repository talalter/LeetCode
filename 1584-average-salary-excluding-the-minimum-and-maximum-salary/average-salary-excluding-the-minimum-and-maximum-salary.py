class Solution:
    def average(self, salary: List[int]) -> float:
        total_sum = salary[0]
        min_sal = salary[0]
        max_sal = salary[0]
        for sal in salary[1:]:
            min_sal = min(min_sal, sal)
            max_sal = max(max_sal, sal)
            total_sum += sal
        return (total_sum - min_sal- max_sal) / (len(salary) - 2)
        