from collections import defaultdict

class AnagramGrouper:
    def group_anagrams(self, strs):
        anagrams = defaultdict(list)

        for s in strs:
            # Sort the string and use it as the key
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)

        return list(anagrams.values())

# Example usage
grouper = AnagramGrouper()
print(grouper.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))



from typing import List

class AnagramGrouper:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            # Sort the word to use as a key
            sorted_word = ''.join(sorted(word))
            if sorted_word in freq:
                freq[sorted_word].append(word)
            else:
                freq[sorted_word] = [word]
        
      
        print(freq)
        
   
        return list(freq.values())


grouper = AnagramGrouper()
result = grouper.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
