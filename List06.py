def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    i=0
    list2 = []
    while i<len(list1):
        if list1[i]==1:
            list2.append(True)

        else:
            list2.append(list1[i])
        
        i += 1
    
    return list2 
a=[1,0,0,1,0,0,1,3]

print(main(a))
