class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for w in words:
            cur = self.root
            for i in w:
                if i not in cur.children:
                    cur.children[i] = TrieNode()
                cur = cur.children[i]
            cur.word = True
        
        path = set()
        res = set()
        rows = len(board)
        cols = len(board[0])
        

        def dfs(r, c, w, head):
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in path or board[r][c] not in head.children:
                return
            path.add((r,c))
            head = head.children[board[r][c]]
            w+=board[r][c]
            if head.word == True:
                res.add(w)
            
            dfs(r+1, c, w, head)
            dfs(r-1, c, w, head)
            dfs(r, c+1, w, head)
            dfs(r, c-1, w, head)
            path.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "", self.root)
        
        return list(res)










