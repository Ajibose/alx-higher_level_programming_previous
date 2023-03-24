#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == "":
        return 0

    rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    equi = [1, 5, 10, 50, 100, 500, 1000]
    new_list = []
    integer = 0
    prev = 0

    for i in range(len(roman_string)):
        for j in range(7):
            if roman_string[i] == rom[j]:
                if (roman_string[i] == roman_string[0]):
                    integer += equi[j]
                else:
                    if roman_string[i - 1] in new_list:
                        for count in range(7):
                            if roman_string[i - 1] == rom[count]:
                                prev = equi[count]
                        integer += (equi[j] - (prev * 2))
                    else:
                        integer += equi[j]
                del new_list[:]
                break
            else:
                new_list.append(rom[j])

    return integer
