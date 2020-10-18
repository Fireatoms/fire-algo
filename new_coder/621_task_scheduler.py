# link: https://leetcode-cn.com/problems/task-scheduler/
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = [0] * 26
        time = 0
        for task in tasks:
            task_counter[ord(task) - ord('A')] += 1

        task_counter.sort()
        while task_counter[25] != 0:
            for i in range(n + 1):
                if task_counter[25] == 0:
                    break

                if i < 26 and task_counter[25 - i] > 0:
                    task_counter[25 - i] -= 1

                time += 1
            task_counter.sort()

        return time

    def leastIntervalIdle(self, tasks: List[str], n: int) -> int:
        task_counter = [0] * 26
        for task in tasks:
            task_counter[ord(task) - ord('A')] += 1

        task_counter.sort()
        idle_layer = task_counter[25] - 1
        idle_slot = idle_layer * n

        i = 24
        while i >= 0 and task_counter[i] > 0:
            idle_slot -= min(idle_layer, task_counter[i])
            i -= 1

        return len(tasks) + idle_slot if idle_slot > 0 else len(tasks)


if __name__ == "__main__":
    tasks = ["A","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    n = 29
    sl = Solution()
    print(sl.leastIntervalIdle(tasks, 29))

