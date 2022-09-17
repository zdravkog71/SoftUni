import math

class Integer:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

    @classmethod
    def from_float(cls,float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        new_value = math.floor(float_value)
        return cls(new_value)

    @classmethod
    def from_roman(cls, value):
        in_val = Integer.roman_to_int(value)
        return cls(in_val)

    @classmethod
    def from_string(cls, value):
        if value.isdigit():
            return cls(int(value))
        return f"wrong type"




first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
