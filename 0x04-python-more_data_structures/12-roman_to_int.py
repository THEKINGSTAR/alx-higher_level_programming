#!/usr/bin/python3
def roman_to_int(roman_string):
    '''
    I	V	X	L	C	D	M
    1	5	10	50	100	500	1000
    '''
    if roman_string is None or not isinstance(roman_string, str):
        return None
    roman = {'I': 1, 'V': 5, "X": 10,
             "L": 50, "C": 100, "D": 500,
             "M": 1000}
    rom_dec = 0
    roman_string = roman_string.upper()

    for idx, digt in enumerate(roman_string):
        if idx + 1 < len(roman_string):
            if roman[digt] < roman[roman_string[idx + 1]]:
                # print(f"Subtrac: {roman[digt]} from {roman_string[idx+1]}")
                rom_dec -= roman[digt]
            else:
                # print(f"Adding {roman[digt]} to total")
                rom_dec += roman[digt]
        else:
            # print(f"Adding {roman[digt]} to total")
            rom_dec += roman[digt]
    return rom_dec


# Example usage:
'''
print(roman_to_int("XIX"))  # Example usage, should return 19:
print(roman_to_int("XLII"))  # Example usage, should return 42:
print(roman_to_int("MCMXCIV"))  # Example usage, should return 1994
print(roman_to_int("MMMCMXCIX"))  # Example usage, should return 3999
print(roman_to_int("MMXXIII"))  # Example usage, should return 2023
print(roman_to_int("MMXXIV"))  # Example usage, should return 2024
print(roman_to_int("MMXXV"))  # Example usage, should return 2025
print(roman_to_int("MMXXVI"))  # Example usage, should return 2026
print(roman_to_int("MMXXVII"))  # Example usage, should return 2027
'''
