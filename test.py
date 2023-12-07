def is_vowel(ch):
    vowels = "aeiou"
    return ch in vowels

def to_binary_string(s):
    binary_string = ""
    for char in s:
        if is_vowel(char):
            binary_string += "0"
        else:
            binary_string += "1"
    return binary_string.lstrip('0')

def binary_to_decimal(binary_str):
    decimal_num = 0
    for digit in binary_str:
        decimal_num = decimal_num * 2 + int(digit)
    return decimal_num

# Input
Str = input().strip()

# Step 1: Convert to binary string
binary_str = to_binary_string(Str)

# Step 2: Convert binary to decimal and print
decimal_result = binary_to_decimal(binary_str)
print(decimal_result)
