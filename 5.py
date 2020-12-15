# Author: Kali Regenold

def fun1(seat_list):
    max_id = 0

    for c in seat_list:
        # Convert from seat notation to binary string: F,L=>0 and B,R=>1
        c = c.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        # Convert binary string to integer id and keep max id
        max_id = max(int(c, 2), max_id)

    print(max_id)


def sort_func1(seat):
    return seat[:-3]

def sort_func2(seat):
    return seat[-3:]


def fun2(seat_list):
    # Sort alphabetically by last three characters (R and L)
    seat_list.sort(reverse=False, key=sort_func2)
    # Sort reverse alphabetically by first seven characters (F and B)
    # Seat list is now sorted numerically, ascending
    seat_list.sort(reverse=True, key=sort_func1)
    # First seat is ruled out and is an edge case, default to 0
    seat_list[0] = 0

    for idx in range(1, len(seat_list)):
        # Convert from seat notation to integer id
        seat_list[idx] = int(seat_list[idx].replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
        # Compare to the previous seat id
        # If there's a gap, that's our seat
        if seat_list[idx] - seat_list[idx-1] == 2:
            print(seat_list[idx]-1)
            return


if __name__ == "__main__":
    # Read seats (in seat notation) into a list separated by newline
    with open('5.in', 'r') as f:
        seat_list = f.readlines()
    seat_list = [x.strip() for x in seat_list]
    fun1(seat_list)
    fun2(seat_list)
