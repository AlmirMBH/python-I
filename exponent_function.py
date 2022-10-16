print(2 ** 3)  # the same as 2*2*2 or 2^3


def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result


print(raise_to_power(2, 10))
