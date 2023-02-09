from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        sorted_ideas = sorted(ideas)
        names = set(ideas)
        initials = sorted(set([s[0] for s in names]))
        c = 0
        starting_points = dict()
        for name in sorted_ideas:
            starting_points.setdefault(name[0], []).append(name)

        possible_starting_letters = dict()
        for word in ideas:
            for letter in initials:
                if letter != word[0] and (letter + word[1:]) not in names:
                    possible_starting_letters.setdefault(word, set()).add(letter)

        for word in ideas:
            my_letter = word[0]
            for letter in possible_starting_letters.get(word, []):
                for other_word in starting_points[letter]:
                    if other_word in possible_starting_letters and my_letter in possible_starting_letters[other_word]:
                        c += 1

        # for i, part1 in enumerate(ideas):
        #     for j in range(i + 1, len(ideas)):
        #         if ideas[i][0] != ideas[j][0]:
        #             a0 = ideas[i][0] + ideas[j][1:]
        #             b0 = ideas[j][0] + ideas[i][1:]
        #             if a0 not in names and b0 not in names:
        #                 c += 2
        return c
