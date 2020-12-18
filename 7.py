# Author: Kali Regenold


# Gonna start using global variables cause it's nice and easy
bag_dict = {}


# For each rule, parse the sentence for bag names and how bags a bag can hold
# Bags that don't hold other bags will, by virtue of the code gods, have empty lists without needing a check
def extract_rule_data(rule):
    rule_split = rule.split(" ")
    outter_bag_name = rule_split[0] + rule_split[1]
    bag_count = int((len(rule_split) - 4)/4)
    inner_bag_names = [""]*bag_count
    inner_bag_counts = [0]*bag_count
    for i in range(0, bag_count):
        inner_bag_names[i] = rule_split[5+(i*4)] + rule_split[6+(i*4)]
        inner_bag_counts[i] = int(rule_split[4+(i*4)])
    return (outter_bag_name, inner_bag_names, inner_bag_counts)


# Recursive function to find if a bag can hold a shiny gold bag,
# or if one it's contained bags can hold a shiny gold bag
def can_hold_shiny_gold(bags):
    if len(bags) == 0:
        return False

    if "shinygold" in bags:
        return True

    for bag in bags:
        if can_hold_shiny_gold(bag_dict[bag][0]):
            return True

    return False


def fun1():
    outter_bag_count = 0

    # Check every higher level bag for the ability to hold a shiny gold bag
    for bag in bag_dict.keys():
        outter_bag_count += can_hold_shiny_gold(bag_dict[bag][0])

    print(outter_bag_count)


# Recursive function to count how many bags a bag can hold
def get_inner_bag_count(bag):
    inner_bag_count = 0
    bag_names = bag_dict[bag][0]
    bag_count = bag_dict[bag][1]
    for i in range(0, len(bag_names)):
        inner_bag_count += (bag_count[i] * (1+get_inner_bag_count(bag_names[i])))
    return inner_bag_count


# Just call the recursive function
def fun2():
    inner_bag_count = get_inner_bag_count('shinygold')
    print(inner_bag_count)


if __name__ == '__main__':
    # Read rules into a list separated by newline
    with open('7.in', 'r') as f:
        rule_list = f.readlines()
    rule_list = [x.strip() for x in rule_list]
    # Create bag dictionary "bag name" : ([list of inner bag names], [list of ine bag counts])
    for rule in rule_list:
        outter_bag_name, inner_bag_names, inner_bag_counts = extract_rule_data(rule)
        bag_dict[outter_bag_name] = (inner_bag_names, inner_bag_counts)
    fun1()
    fun2()
