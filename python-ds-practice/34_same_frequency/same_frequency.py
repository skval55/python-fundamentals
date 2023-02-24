def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # return len(str(num1)) == len(str(num2)) this works haha gottem
    num1 = list(str(num1))
    num2 = list(str(num2))
    num1.sort()
    num2.sort()
    if not len(num1) == len(num2):
        return False
    for i in range(len(num1)):
        if not num1[i] == num2[i]:
            return False
    return True