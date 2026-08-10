class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            new_s = "".join(sorted(list(s)))
            group[new_s].append(s)
        
        return list(group.values())