class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ws = set(wordList)
        q = deque()

        if endWord not in ws:
            return 0
        
        q.append((beginWord,1))

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    neww = word[:i]+c+word[i+1:]

                    if neww in ws:
                        q.append((neww, steps+1))
                        ws.remove(neww)
        return 0
        