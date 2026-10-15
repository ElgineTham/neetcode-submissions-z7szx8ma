class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_length = min(len(w1), len(w2))
            if (len(w1) > len(w2) and
                w1[0:min_length] == w2[0:min_length]):
                return ""
            
            for j in range(min_length):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        answer = []
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            answer.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        answer.reverse()
        return "".join(answer)