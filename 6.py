# Author: Kali Regenold

def fun1(group_list):
    # Sum of number of unique answers in each group
    answer_sum = 0
    for answers in group_list:
        # Call set on the string to remove duplicate characters
        # Increase sum of unique answers by the length of the set
        answer_sum += len(set(answers.replace("\n", '')))
    print(answer_sum)


def fun2(group_list):
    # Sum of number of common answers in each group
    answer_sum = 0
    for answers in group_list:
        # Split a group's answers into each person's answers
        answer_split = answers.split("\n")
        # Turn each string of answers into a set and find the intersection of elements between all sets
        # Only characters exist in all strings from a group are left over
        intersection = set(list(answer_split[0]))
        for answer in answer_split:
            intersection &= set(list(answer))
        # Increase sum of common answers by length of intersection set
        answer_sum += len(intersection)
    print(answer_sum)


if __name__ == "__main__":
    # Read answers into a list, separated by two newlines
    with open('6.in', 'r') as f:
        group_list = f.read().strip()
    group_list = group_list.split("\n\n")
    fun1(group_list)
    fun2(group_list)
