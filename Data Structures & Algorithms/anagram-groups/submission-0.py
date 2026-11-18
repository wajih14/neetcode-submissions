class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base_stacker = {}
        for word in strs:
            k = "".join(sorted(list(word)))
            if k in base_stacker.keys():
                base_stacker[k].append(word)
                continue
            base_stacker[k] = [word]
        return list(base_stacker.values())