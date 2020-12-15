# Author: Kali Regenold

def fun1(pass_list):
    valid_cnt = 0

    for rule_pass in pass_list:
        # Separate the rule and password
        rule, password = rule_pass.split(':')
        # Count occurences of rule letter in password
        char_cnt = password.count(rule[-1])
        # Increase valid count if number of rule letter occurences is within rule bounds
        valid_cnt += (char_cnt >= int(rule.split('-')[0]) and char_cnt <= int(rule.split('-')[1][0:-2]))

    print(valid_cnt)


def fun2(pass_list):
    valid_cnt = 0

    for rule_pass in pass_list:
        # Separate the rule and password
        rule, password = rule_pass.split(':')
        # Remove whitespace from password
        password = password.strip()
        # Extract valid rule letter positions from rule
        pos1 = int(rule.split('-')[0]) - 1
        pos2 = int(rule.split('-')[1][0:-2]) - 1
        # Increase valid count if rule letter in position 1 XOR rule letter in position 2
        valid_cnt  += ((password[pos1] == rule[-1]) ^ (password[pos2] == rule[-1]))

    print(valid_cnt)

if __name__ == "__main__":
    # Read rule and password into a list separated by newline
    with open('2.in', 'r') as f:
        pass_list = f.readlines()
    pass_list = [x.strip() for x in pass_list]
    fun1(pass_list)
    fun2(pass_list)
