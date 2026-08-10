class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)  # {tuple([]) : [words]}

        for word in strs:
            alph = [0] * 26
            for c in word:
                alph[ord(c) - ord('a')] += 1
            hash_map[tuple(alph)].append(word)
        
        return list(hash_map.values())