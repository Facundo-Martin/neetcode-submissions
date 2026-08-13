class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.is_end_of_word = True
        
    def search(self, word: str) -> bool:

        def dfs(start_idx: int, node: TrieNode)-> bool:
            cur = node
            
            for i in range(start_idx, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        # If at least 1 path matches we return true
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.is_end_of_word
            
        return dfs(0, self.root)