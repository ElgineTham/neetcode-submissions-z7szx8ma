class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        changes = 0
        seen = set()
        
        while q:
            length = len(q)
            changes += 1
            for _ in range(length):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return changes
                seen.add(curr_word)
                for new_word in wordList:
                    if new_word in seen:
                        continue
                    if self.can_change(curr_word, new_word):
                        q.append(new_word)
        
        return 0
    
    def can_change(self, curr_word, new_word):
        if len(curr_word) != len(new_word):
            return False
        
        differences = 0
        for i in range(len(curr_word)):
            if curr_word[i] != new_word[i]:
                differences += 1
            
            if differences > 1:
                return False
        
        return differences <= 1



