class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for r, c in reservedSeats:
            rows.setdefault(r, set()).add(c)
        
        count = 2 * (n - len(rows))
        
        left = {2, 3, 4, 5}
        middle = {4, 5, 6, 7}
        right = {6, 7, 8, 9}
        
        for seats in rows.values():
            can_left = not (seats & left)
            can_middle = not (seats & middle)
            can_right = not (seats & right)
            
            if can_left and can_right:
                count += 2
            elif can_left or can_middle or can_right:
                count += 1
        
        return count
