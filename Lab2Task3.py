def is_valid(string: str):
    open_brackets_count = 0

    for c in string:
        if c == '(':
            open_brackets_count += 1
        elif c == ')':
            if open_brackets_count == 0:
                return False

            open_brackets_count -= 1

    if open_brackets_count == 0:
        result = True
    else:
        result = False

    return result


if __name__ == '__main__':
    string = input("sentence: ")

    if is_valid(string):
        result = "YES"
    else:
        result = "NO"

    print(result)
