class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for ch in word:
                if ch not in indegree:
                    indegree[ch] = 0
        
        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i+1]
            minlen = min(len(w1),len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j] != w2[j]:
                    parent = w1[j]
                    child = w2[j]

                    if child not in graph[parent]:
                        graph[parent].add(child)
                        indegree[child] += 1

                    break

        q = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)

        result = []
        while q:
            ch = q.popleft()
            result.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(result) != len(indegree):
            return ""

        return "".join(result)        