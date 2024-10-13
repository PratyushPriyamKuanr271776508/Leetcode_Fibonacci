class Solution:
    def convert_to_digits(self, n: int) -> list:
        result = []
        while n != 0:
            result.append(n % 10)
            n //= 10
        result.reverse()
        return result
    
    def convert_to_number(self, digits: list) -> int:
        result = 0
        for i in digits:
            result = result * 10 + i
        return result
    
    def add_to_digits(self, add: int, digits: list) -> None:
        digits.reverse()
        for i in range(len(digits)):
            digits[i] += add
            add = digits[i] // 10
            digits[i] %= 10
        if add > 0:
            digits.append(add)
        digits.reverse()
    
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        digits = self.convert_to_digits(n)
        
        # Calculate sum of digits
        total_sum = sum(digits)
        if total_sum <= target:
            return 0
        
        diff = total_sum - target
        digits_added_from_back = []
        
        while diff > 0:
            if digits[-1] == 0:
                digits.pop()
                digits_added_from_back.append(0)
                continue
            
            added = 10 - digits[-1]
            digits.pop()
            digits_added_from_back.append(added)
            
            self.add_to_digits(1, digits)
            
            total_sum = sum(digits)
            diff = total_sum - target
        
        digits_added_from_back.reverse()
        return self.convert_to_number(digits_added_from_back)
