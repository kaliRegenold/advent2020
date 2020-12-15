# Author: Kali Regenold

import re

def fun1(passport_list):
    # All required passport fields
    field_list = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    valid_cnt = 0

    for passport in passport_list:
        # Create list of fields that are present in passport
        present_fields = [p for p in field_list if (p in passport)]
        # Increase valid count if all fields are present
        valid_cnt += (len(present_fields) == len(field_list))

    print(valid_cnt)


# Helper functions to validate data in each field
def check_byr(byr):
    return byr >= 1920 and byr <= 2002
def check_iyr(iyr):
    return iyr >= 2010 and iyr <= 2020
def check_eyr(eyr):
    return eyr >= 2020 and eyr <= 2030
def check_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def check_pid(pid):
    return bool(re.match(r"^\d{9}$", pid))
def check_hgt(hgt):
    return ((hgt[-2:] == 'cm' and int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193) or
            (hgt[-2:] == 'in' and int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76))
def check_hcl(hcl):
    return bool(re.match(r"^#[A-Z,a-z,0-9]{6}$", hcl))


def fun2(passport_list):
    valid_cnt = 0
    valid_passport = True

    for p in passport_list:
        # Create dictionary from space separated list
        passport = dict((x.strip(), y.strip())
             for x, y in (element.split(':')
             for element in p.strip().replace("\n", ' ').split(' ')))
        try:
            # Check all fields; passport valid if all fields are valid
            valid_passport = (check_byr(int(passport['byr'])) and
                              check_iyr(int(passport['iyr'])) and
                              check_eyr(int(passport['eyr'])) and
                              check_ecl(passport['ecl'])      and
                              check_pid(passport['pid'])      and
                              check_hgt(passport['hgt'])      and
                              check_hcl(passport['hcl']))
        # This try-except will catch any failing int() calls, which is one of the checks I refuse to make
        except:
            valid_passport = False
        # Increase valid count if passport is valid (duh)
        valid_cnt += valid_passport
        valid_passport = True

    print(valid_cnt)


if __name__ == "__main__":
    # Read passports into a list separated by two newlines
    with open('4.in', 'r') as f:
        passport_list = f.read()
    passport_list = passport_list.split("\n\n")
    fun1(passport_list)
    fun2(passport_list)
