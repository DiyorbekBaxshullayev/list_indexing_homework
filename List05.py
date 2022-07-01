from re import I


def main(list1,i):
    """
    A list of several elements is given. i Return the item in the index.
    Args:
        list1 (list): parameter
        i (int): parameter
    Returns:
        list: return answer
    """
    return list1[i]

i=3
x=[5,6,7,9]

print(main(x,i))