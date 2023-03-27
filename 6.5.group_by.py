
def group_by(func, iterable):
    result_dict = {}
    for item in iterable:
        key = func(item)
        if key not in result_dict:
            result_dict[key] = [item]
        else:
            result_dict[key].append(item)
    return result_dict


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))