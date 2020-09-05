class Solution:
    def canCompleteCircuitBrute(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        start_candidate = []
        for i in range(l):
            if gas[i] >= cost[i]:
                start_candidate.append(i)

        res = -1
        for start in start_candidate:
            i = (start+1)%l
            gas_remain = gas[start] - cost[start]
            while i != start:
                gas_remain += gas[i] - cost[i]
                if gas_remain < 0:
                    break
                else:
                    i = (i+1)%l

            if i == start:
                res = start

        return res

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # link: https://leetcode-cn.com/problems/gas-station/solution/jia-you-zhan-by-leetcode/
        # It can travel from 0 to starting_station - 1 and travel from starting_station to 0.
        # If total_tank >= 0, the gas we have when we reach starting_station - 1 from stating_station can afford us to
        # move to starting_station.
        l = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(l):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                # notice this i + 1, not i.
                # index begin at 0
                starting_station = i + 1
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1