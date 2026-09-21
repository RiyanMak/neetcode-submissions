class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        for string in strs:
            sortedString = ''.join(sorted(string))
            
            if sortedString in dic:
                dic[sortedString].append(string)
            else:
                dic[sortedString] = [string]            

        return list(dic.values())
