def is_set(bit, x):
    return (x & (1 << bit)) > 0

def set_bits_count(x):
    highest_bit = 63
    while highest_bit >= 0 and not is_set(highest_bit, x):
        highest_bit -= 1
    
    cnt = [0] * 64
    
    i = highest_bit
    while i >= 0:
        x -= (1 << i)
        cnt[i] += x + 1
        
        for j in range(i - 1, -1, -1):
            cnt[j] += (1 << i) // 2
        
        i -= 1
        while i >= 0 and not is_set(i, x):
            i -= 1
    
    return cnt

def sum_of_prices(n, x):
    cnt_bits = set_bits_count(n)
    
    result = 0
    for i in range(63, -1, -1):
        if (i + 1) % x == 0:
            result += cnt_bits[i]
    
    return result

class Solution:
    def findMaximumNumber(self, k, x):
        l, r = 1, int(1e15) * 64
        
        while l < r:
            m = (l + r + 1) // 2
            
            if sum_of_prices(m, x) <= k:
                l = m
            else:
                r = m - 1
        
        return l
