def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    i=0
    if list_num[0]>list_num[-1]:
        i+=list_num[0]

    elif list_num[0]<list_num[-1]:
        i+=list_num[-1]
    
    return i

a=[8,2,3,4,5]
print(main(a))
