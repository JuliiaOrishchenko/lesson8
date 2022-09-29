def make_operation(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        new_list = [number*(-1) for number in args[1:]]
        return sum(new_list)+args[0]
    else:
        mul_result = 1
        for i in range(len(args)):
            mul_result *= args[i]
        return mul_result



