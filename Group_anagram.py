
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This list will hold our final answer (a list of groups)
        result = []
        
        # This acts like a checklist. Once a word is placed into a group,
        # we add its index here so we don't accidentally check or group it again.
        visited = set()
        
        # Step 1: Pick the first available word in the list using its index 'i'
        for i in range(len(strs)):
            
            # If we already grouped this word earlier, skip it and move to the next one
            if i in visited:
                continue

            # Start a brand new group and put our current word inside it
            current_group = [strs[i]]
            
            # Mark this current word as 'visited' so we don't use it again
            visited.add(i)

            # Step 2: Compare our picked word (at index i) with every OTHER word 
            # that comes after it in the list (at index j)
            for j in range(i + 1, len(strs)):
                
                # Only check the word if it hasn't been grouped yet
                if j not in visited:
                    
                    # Ask our helper function: "Are these two words anagrams?"
                    if self.isAnagram(strs[i], strs[j]):
                        
                        # If yes, add the matching word to our current group
                        current_group.append(strs[j])
                        
                        # Mark this matching word as 'visited' too
                        visited.add(j)
                        
            # Step 3: Once we finish checking all remaining words for this round,
            # we add the completed group to our final result list
            result.append(current_group)
            
        # After looking at every single word, return the final grouped list
        return result


    # This is our helper function that checks if two words are anagrams
    def isAnagram(self, s: str, t: str) -> bool:
        # If the words don't have the exact same number of letters, 
        # they cannot possibly be anagrams. Return False immediately.
        if len(s) != len(t):
            return False
            
        # Sort the letters of both words alphabetically.
        # If "eat" becomes "aet" and "tea" becomes "aet", they match!
        return sorted(s) == sorted(t)
