roman_numerals = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}
print("***Constraints : Only works for values less than 4000***\n")
class Translator:

    def __init__(self):
        self.const_int = int(input("Enter a natural number : "))
        self.var_int = self.const_int
        self.size = 1
        self.roman = ''
        self.broken = []
        self.tens = []

        # Error Handling 
        if (self.const_int > 3999):
            print("Input Error : Input shouldn't be greater than 5000\n")
            exit(0)
        elif (self.const_int < 0 or self.const_int == 0):
            print("-")

        while self.var_int > 10:
            self.var_int //= 10
            self.size += 1
        self.var_int = self.const_int

    def decb(self, num_size):
        ten = 1
        for i in range(num_size):
            ten *= 10
        return ten//10

    def integer_decomposition(self):
        self.start = 10
        self.test = self.var_int
        self.decimal_count = 1

        while self.test > 10:
            self.test //= self.start
            self.decimal_count *= 10

        self.test *= (self.decimal_count)
        self.var_int -= self.test
        self.broken.append(self.test)
        self.tens.append(self.decimal_count)

    def exception_four_or_nine(self, y, tens):
        if (y == 4):
            self.roman += roman_numerals[tens]
            self.roman += roman_numerals[5*tens]
        elif (y == 9):
            self.roman += roman_numerals[tens]
            self.roman += roman_numerals[10*tens]

    def break_num(self):
        for i in range(self.size):
            self.integer_decomposition()
        self.var_int = self.const_int
        x = 0
        fifty_forty_diff = 0

        for i in range(self.size):
            x = self.broken[i]//self.tens[i]
            if (self.tens[i] == 1000):
                for j in range(x):
                    self.roman += roman_numerals[self.tens[i]]

            elif (self.tens[i] == 100 or self.tens[i] == 10):
                if (x < 4):
                    for k in range(x):
                        self.roman += roman_numerals[self.tens[i]]
                elif (x > 5 and x < 9):
                    if (x < 9):
                        self.roman += roman_numerals[(5*self.tens[i])]
                        for f in range(x-5):
                            self.roman += roman_numerals[self.tens[i]]
                elif (x == 4 or x == 9):
                    self.exception_four_or_nine(x, self.tens[i])

            elif (self.tens[i] == 1):
                if (self.broken[i] < 4):
                    for f in range(x):
                        self.roman += roman_numerals[1]
                elif (self.broken[i] > 5):
                    if (self.broken[i] < 9):
                        self.roman += roman_numerals[5]
                        for i in range(x-5):
                            self.roman += roman_numerals[1]
                    else:
                        self.roman += 'IX'
                elif (x == 4):
                    self.roman += 'IV'
        return self.roman 
    


obj1 = Translator()
roman = obj1.break_num()
print(roman)
