def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i=0
    list2=[]
    while i<len(list1):
        if list1[i]==0:
            list2.append(False)
        else:
            list2.append(list1[i])

        i+=1

    return list2

a=[1,2,0,0,1]
print(main(a))
