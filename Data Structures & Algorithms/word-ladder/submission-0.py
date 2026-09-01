import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
            
        queue = collections.deque([(beginWord, 1)])
        
        while queue:
            current_word, steps = queue.popleft()
            
            if current_word == endWord:
                return steps
                
            # Dynamically generate edges
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    # Create the new word
                    next_word = current_word[:i] + char + current_word[i+1:]
                    
                    if next_word in word_set:
                        # Remove from set to mark as visited and prevent cycles
                        word_set.remove(next_word)
                        queue.append((next_word, steps + 1))
                        
        return 0