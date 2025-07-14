#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    """
    length = []
    for idx in range(list_length):
        try:
            div = my_list_1[idx] / my_list_2[idx]
        except TypeError as e:
            div = 0
            print("wrong type")
            continue
        except IndexError as e:
            div = 0
            print("out of range")
            continue
        except ValueError as e:
            div = 0
            print("wrong type")
            continue
        except ZeroDivisionError as e:
            div = 0
            print("division by 0")
            continue
        except Exception as e:
            div = 0
            print(e)
            continue
        finally:
            length.append(div)
    return length

