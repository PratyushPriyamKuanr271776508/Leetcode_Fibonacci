MOD = int(1e9 + 7)
P = 31

# Initialize power and inverse power arrays
pwr_p = [0] * (int(5e5) + 1)
inv_p = [0] * (int(5e5) + 1)

def fast_power(a, b, mod=MOD):
    a %= mod
    b %= mod
    ans = 1
    while b:
        if b & 1:
            ans = (ans * a) % mod
        b //= 2
        a = (a * a) % mod
    return ans

class Solution:
    def __init__(self):
        self.pref = []

    def exist(self, sz, s):
        n = len(self.pref) - 1
        
        sum_ = 0
        for j in range(1, sz + 1):
            sum_ += pwr_p[j]
        sum_ %= MOD
        
        expected_hash = [0] * 27
        for j in range(1, 27):
            expected_hash[j] = (sum_ * j) % MOD
        
        hash_cnt = [0] * 27
        for l in range(1, n - sz + 2):
            r = l + sz - 1
            ch = ord(s[l - 1]) - ord('a') + 1
            hash_ = ((self.pref[r] - self.pref[l - 1] + MOD) * inv_p[l - 1]) % MOD
            
            if hash_ != expected_hash[ch]:
                continue
            
            hash_cnt[ch] += 1
            if hash_cnt[ch] == 3:
                return True
        
        return False

    def maximumLength(self, s):
        n = len(s)
        
        # Initialize prefix hash array
        self.pref = [0] * (n + 1)
        
        # Precompute powers of P modulo MOD
        pwr_p[0] = 1
        for j in range(1, n + 1):
            pwr_p[j] = (pwr_p[j - 1] * P) % MOD
        
        # Precompute inverse powers of P modulo MOD
        inv_p[n] = fast_power(P, MOD - n - 1)
        for j in range(n - 1, -1, -1):
            inv_p[j] = (inv_p[j + 1] * P) % MOD
        
        # Compute prefix hashes
        for j in range(1, n + 1):
            self.pref[j] = (self.pref[j - 1] + (pwr_p[j] * (ord(s[j - 1]) - ord('a') + 1)) % MOD) % MOD
        
        l, r = 1, n - 2
        while l < r:
            m = (l + r) // 2
            if self.exist(m + 1, s):
                l = m + 1
            else:
                r = m
        
        return l if self.exist(l, s) else -1
