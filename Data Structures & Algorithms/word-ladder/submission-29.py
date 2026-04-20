class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        word_map = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + "*" + word[i+1:]
                word_map[new_word].append(word)
        
        q = deque()
        q.append(beginWord)
        seen = set()
        seen.add(beginWord)
        changes = 0

        while q:
            
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return changes+1
                for i in range(len(word)):
                    new_word = word[:i] + "*" + word[i+1:]
                    for w in word_map[new_word]:
                        if w in seen:
                            continue
                        
                        seen.add(w)
                        q.append(w)
            
            changes += 1
        
        return 0
