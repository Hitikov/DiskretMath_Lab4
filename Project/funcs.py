import re, math

from prettytable import PrettyTable

def func_is_correct(arr):
    arrlen = len(arr)

    if arrlen <= 0:
        return False
    log_value = math.log2(arrlen)
    first = log_value == int(log_value)

    allowed = '01'
    pattern = f'^[{re.escape(allowed)}]*$'
    second = re.match(pattern, arr) is not None

    return first and second

def make_int_arr(arr):
    int_list = [int(char) for char in arr]

    return int_list

def check_zerosave(arr):
    if arr[0] == 0:
        return True
    return False

def check_onesave(arr):
    if arr[-1] == 1:
        return True
    return False

def check_selfdouble(arr):

    if len(arr) == 1:
        return False

    sublen = int(len(arr) / 2)

    for i in range(sublen):
        if arr[i] == arr[-1 - i]:
            return False

    return True


def check_monotone(arr):
    num_inputs = len(arr)

    if num_inputs == 1:
        return True

    for i in range(num_inputs):
        for j in range(num_inputs):
            if i < j:
                if (i | j) == j and arr[i] > arr[j]:
                    return False

    return True


def check_linear(arr):
    num_inputs = len(arr)

    if num_inputs == 1:
        return True

    for i in range(num_inputs):
        for j in range(num_inputs):
            if i != j:
                xor_result = i ^ j

                if arr[xor_result] == arr[i] ^ arr[j]:
                    return False

    return True


def get_properties(arr):

    if not func_is_correct(arr):
        return []

    sub = make_int_arr(arr)

    res = [arr,
           check_zerosave(sub),
           check_onesave(sub),
           check_selfdouble(sub),
           check_monotone(sub),
           check_linear(sub)]

    return res

def make_table(res):
    table_content = []
    for el in res:
        sub = []
        for subel in el:
            if isinstance(subel, bool):
                if subel:
                    sub.append('+')
                else:
                    sub.append('-')
            else:
                sub.append(subel)
        table_content.append(sub)


    header_values = ['Function', 'T0', 'T1', 'Ts', 'Tm', 'Tl']

    columns = len(header_values)

    table = PrettyTable(header_values)

    while table_content:
        table.add_rows(table_content[:columns])
        table_content = table_content[columns:]

    print(table)

def manage_all_arr(strs):

    res = [get_properties(strr) for strr in strs]

    make_table(res)

    check_fullness(res)


def get_logic_funcs():
    res = []

    is_input_continuing = True

    while is_input_continuing:

        val = input()

        if len(val) == 0:
            is_input_continuing = False
        else:
            res.append(val)

    return res

#check basis
def check_fullness(arr):
    T0, T0_count, T0_pos = False, 0, 0
    T1, T1_count, T1_pos = False, 0, 0
    Ts, Ts_count, Ts_pos = False, 0, 0
    Tm, Tm_count, Tm_pos = False, 0, 0
    Tl, Tl_count, Tl_pos = False, 0, 0

    for elem in arr:
        if not elem[1]:
            T0 = True
            T0_count += 1
        else:
            T0_pos += 1

        if not elem[2]:
            T1 = True
            T1_count += 1
        else:
            T1_pos += 1

        if not elem[3]:
            Ts = True
            Ts_count += 1
        else:
            Ts_pos += 1

        if not elem[4]:
            Tm = True
            Tm_count += 1
        else:
            Tm_pos += 1

        if not elem[5]:
            Tl = True
            Tl_count += 1
        else:
            Tl_pos += 1

    if T0 and T1 and Ts and Tm and Tl:
        print('System is full')

        if ((T0_count > 1 or T1_count > 1 or Ts_count > 1 or Tm_count > 1 or Tl_count > 1)
                and (T0_pos > 1 or T1_pos > 1 or Ts_pos > 1 or Tm_pos > 1 or Tl_pos > 1)):
            print('System is not basis')
        else:
            print('System is basis')

    else:
        print('System is not full')
