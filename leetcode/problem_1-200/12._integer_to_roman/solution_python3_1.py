class Solution:
    def intToRoman(self, num: int) -> str:

        #
        res = list()
        hm = {
            1000: "M", 
            900 : "CM", 
            500 : "D", 
            400 : "CD", 
            100 : "C", 
            90 : "XC", 
            50 : "L", 
            40 : "XL", 
            10 : "X", 
            9 : "IX", 
            5 : "V", 
            4 : "IV", 
            1 : "I"
        }

        #
        for val in hm.keys():
            if num < val:
                continue
            else:
                res.append(hm[val] * int(num // val))
                num = num % val
        return "".join(res)
