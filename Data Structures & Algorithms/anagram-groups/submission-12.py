class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)  # key is num of char in word
                      # value is list of anagrams
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
                
            # if tuple(count) not in hashMap:
            #     tempList = []
            #     tempList.append(word)
            #     hashMap[tuple(count)] = tempList
            # else:
            hashMap[tuple(count)].append(word)
        
        return list(hashMap.values())