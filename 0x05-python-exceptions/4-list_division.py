#!/use/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0
            division_result = my_list_1[i] / my_list_2[i]
            result.append(division_result)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
