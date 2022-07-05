def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    x=[]
    while i<len(list1):
        if list1[i]==list1:
            x.append(True)

        else:
            x.append(False)

        i+=1

    return x==list1

a=[1,1,1,1]
print(main(a))
