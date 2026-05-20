class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Shuruat mein hum queue mein ek khali string, open_count aur close_count rakhenge
        # Format: [current_string, open_count, close_count]
        queue = [["", 0, 0]]
        
        # Ek perfect combination ki length hamesha 2 * n hoti hai
        # Hum 2 * n baar loop chalayenge aur har baar string mein 1 character badhayein ge
        for _ in range(2 * n):
            next_queue = []
            
            for current_string, open_count, close_count in queue:
                # Rule 1: Agar '(' bache hain, toh '(' lagakar nayi string banao
                if open_count < n:
                    next_queue.append([current_string + "(", open_count + 1, close_count])
                    
                # Rule 2: Agar ')' ki sankhya '(' se kam hai, toh ')' lagakar nayi string banao
                if close_count < open_count:
                    next_queue.append([current_string + ")", open_count, close_count + 1])
            
            # Agle round ke liye queue ko update kar do
            queue = next_queue
            
        # Aakhri mein queue ke andar sirf valid full-length strings hi bachengi
        return [item[0] for item in queue]