class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 0. Defensive programming (edge cases)
            # - [x] Handle out of bounds pointer for shortest word
            # - [ ] Handle efficient merging of longest word (optimization)
        # 1. Data structure (choose and init, identify problem)
        # 2. Data manipulation (block, edge cases, iterations)
        # 3. Data cleaning & return statements

        upper_bound = max(len(word1), len(word2))  
        s = ''

        for i in range(upper_bound):
            if i <= len(word1) - 1:
                s += word1[i]
            if i <= len(word2) - 1:
                s += word2[i]        

        return s
