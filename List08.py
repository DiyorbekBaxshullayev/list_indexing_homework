def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i=0
    list2=[]
    while i<len(list1):
        if list1[i]==1:
            list2.append(True)

        elif list1[i]==0:
            list2.append(False)

        i+=1
    
    return list2

a=[1,1,0,1,0,1]
print(main(a))
