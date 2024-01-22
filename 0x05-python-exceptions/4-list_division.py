#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_03 = []
    for a in range(list_length):
        try:
            exc = my_list_1[a] / my_list_2[a]

        except (ValueError, TypeError):
            print("wrong type")
            exc = 0

        except ZeroDivisionError:
            print("division by 0")
            exc = 0

        except IndexError:
            print("out of range")
            exc = 0

        finally:
            my_list_03.append(exc)
    return my_list_03
