class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end_of_word = True

class Solution:
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        res = set()
        state = set()  # Tracking visited coordinates during traversal

        def backtrack(r: int, c: int, node: TrieNode, word: str):
            # Guard Clause
            if not (0 <= r < rows) or not (0 <= c < cols) or (r, c) in state:
                return
            
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]
            word += char

            # Base Case
            if next_node.is_end_of_word:
                res.add(word)
                next_node.is_end_of_word = False  # Avoid duplicates

            # 1. CHOOSE
            state.add((r, c))

            # 2. EXPLORE
            for dr, dc in self.DIRECTIONS:
                backtrack(r + dr, c + dc, next_node, word)

            # 3. UNCHOOSE
            state.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, trie.root, "")

        return list(res)