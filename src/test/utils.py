def gets(char_array):
    tmp = input()
    for i in range(len(tmp)):
        char_array[i] = tmp[i]

def strlen(char_array):
    if isinstance(char_array, str):
        return len(char_array)
    else:
        return char_array.index(0)

def atoi(char_array):
    tmp_str = ''
    for i in range(strlen(char_array)):
        tmp_str += str(char_array[i])
    if tmp_str.isdigit():
        return int(tmp_str)
    else:
        return -1


