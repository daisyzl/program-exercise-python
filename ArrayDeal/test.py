#-*-coding:utf-8-*-

class Solution(object):
    def plusOne(self, digits):
        if digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.append(0)
        else:
            digits[-1] += 1
        return digits
    def plusOne2(self, digits):
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits = self.plusOne2(digits[:-1])
            digits.append(0)
        return digits

if __name__ == '__main__':
    digits = [9]
    digits2 = [4, 3, 9]
    print(digits[-1: -3])
    #这样输出的结果为空
    print(digits[-3:-1])
    #[3, 2]
    print(Solution().plusOne2(digits))