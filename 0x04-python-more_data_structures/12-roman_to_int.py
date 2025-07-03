#!/usr/bin/python3
def roman_to_int(roman_string):
    '''
    I	V	X	L	C	D	M
    1	5	10	50	100	500	1000
    '''
    if roman_string is None or not isinstance(roman_string, str):
        return None
    roman={'I': 1, 'V':5, "X":10, "L":50	, "C":100, "D":500, "M":1000}
    rom_dec = 0
    for digt in roman_string:
        rom_dec += roman[digt]
    return rom_dec