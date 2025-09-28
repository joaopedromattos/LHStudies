class Solution:
            
    def maximumProduct(self, arr: List[int]):
    
        if arr == []:
            return 0
        
        if len(arr) <= 3:
            return prod(arr)

        m1, m2, m3, n1, n2 = -inf, -inf, -inf, inf, inf
        
        for i in arr:
            if i > m1:
                m3 = m2
                m2 = m1
                m1 = i
                
            elif i > m2:
                m3 = m2
                m2 = i
                
            elif i > m3:
                m3 = i
                
            if i < n1:
                n2 = n1
                n1 = i
            
            elif i < n2:
                n2 = i
                
        return max(m1 * m2 * m3, m1 * n1 * n2)