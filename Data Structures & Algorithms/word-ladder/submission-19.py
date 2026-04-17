class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        seen = set()
        word_map = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + "*" + word[i+1:]
                word_map[new_word].append(word)
        
        q = deque()
        change = 0
        q.append(beginWord)
        seen.add(beginWord)

        while q:
            change += 1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return change
                for i in range(len(word)):
                    new_word = word[:i] + "*" + word[i+1:]
                    for next_word in word_map[new_word]:
                        if next_word not in seen:
                            seen.add(next_word)
                            q.append(next_word)
        
        return 0

            