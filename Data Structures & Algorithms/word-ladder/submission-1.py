class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
            
        # Use sets instead of queues to easily check intersections
        begin_set = {beginWord}
        end_set = {endWord}
        steps = 1
        
        while begin_set and end_set:
            # Always expand the smaller set to minimize branching factor
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
                
            next_front = set()
            
            for word in begin_set:
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + char + word[i+1:]
                        
                        # The two ripples collided! We found the path.
                        if next_word in end_set:
                            return steps + 1
                            
                        if next_word in word_set:
                            word_set.remove(next_word)
                            next_front.add(next_word)
                            
            begin_set = next_front
            steps += 1
            
        return 0