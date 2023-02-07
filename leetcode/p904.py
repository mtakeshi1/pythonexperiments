from typing import List
from typing import TypedDict
from functools import reduce


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        picked = dict()
        most_recent = -1
        global_max = 0
        for i, fruit in enumerate(fruits):
            if fruit in picked:
                picked[fruit] = picked[fruit] + 1
                most_recent = fruit
            elif len(picked) < 2:
                picked[fruit] = 1
                most_recent = fruit
            else:
                global_max = max(global_max, reduce(lambda a, b: a + b, picked.values()))
                new_picked = dict()
                new_picked[fruit] = 1
                new_picked[most_recent] = 0
                j = i-1
                while j >= 0 and fruits[j] == most_recent:
                    new_picked[most_recent] = new_picked[most_recent] + 1
                    j -= 1

                picked = new_picked
                most_recent = fruit

        return max(global_max, reduce(lambda a, b: a + b, picked.values()))


if __name__ == '__main__':
    print(Solution().totalFruit([1, 2, 1]))
