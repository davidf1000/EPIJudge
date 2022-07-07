
def check_if_ok(take_out: list, take_in: list, served_orders: list) -> bool:
    # create pointer to track take_out and take_in
    # while served_orders is not empty, popleft list
    # check if the number == take_out or take_in, if not then false
    # if ==, move the pointer
    while served_orders:
        item = served_orders.pop(0)
        if take_in and item == take_in[0]:
            take_in.pop(0)
        elif take_out and item == take_out[0]:
            take_out.pop(0)
        else:
            return False
    return True


if __name__ == '__main__':
    A = [1, 3, 5]
    B = [2, 4, 6]
    C = [1, 2, 4, 6, 5, 3]
    print(check_if_ok(A, B, C))
    A = [17, 8, 24]
    B = [12, 19, 2]
    C = [17, 8, 12, 19, 24, 2]
    print(check_if_ok(A, B, C))
