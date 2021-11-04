class Complex:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"{self.x}"

    def __add__(self, other):
        nums = []
        nums.extend(map(int, (''.join([i for i in str(self.x) if i == "+" or "9" >= i >= "0"]).split("+"))))
        nums.extend(map(int, (''.join([i for i in str(other.x) if i == "+" or "9" >= i >= "0"]).split("+"))))
        my_sum = str(nums[0] + nums[2]) + "+" + str(nums[1] + nums[3]) + "j"
        return Complex(complex(my_sum))

    def __mul__(self, other):
        nums = []
        nums.extend(map(int, (''.join([i for i in str(self.x) if i == "+" or "9" >= i >= "0"]).split("+"))))
        nums.extend(map(int, (''.join([i for i in str(other.x) if i == "+" or "9" >= i >= "0"]).split("+"))))
        my_mul = str((nums[0] * nums[2]) - (nums[1] * nums[3])) + "+" + str(
            (nums[1] * nums[2]) + (nums[0] * nums[3])) + "j"
        return Complex(complex(my_mul))


num_1 = Complex(1+5j)
num_2 = Complex(4+16j)
print(num_1 + num_2)
print((4+16j) + (1+5j))
print(num_1 * num_2)
print((4+16j) * (1+5j))
