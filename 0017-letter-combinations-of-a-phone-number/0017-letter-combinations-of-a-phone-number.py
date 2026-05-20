class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
            
        
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        
        combinations = [""]
        
        for digit in digits:
            next_combinations = []
            for current_str in combinations:
                for letter in phone_map[digit]:
                    next_combinations.append(current_str + letter)
            combinations = next_combinations
            
        return combinations