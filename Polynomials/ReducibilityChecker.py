'''
Created on Apr 15, 2021

@author: keenan
'''



def getCoefficients(poly,field,n):
    terms = poly.split('+')
    lst = [0] * n
    for term in terms:
        coef = term[0]
        power = term[-1]
        lst[power] = coef
    return lst

def getDivisors(n):
    ret = []
    for i in range(n):
        if n%i ==0:
            ret.append(i);
    return ret

def allGCDs(coefs,dlist):
    """
    TODO: This function
    my idea here is to create a 
    loop through all the d's in dlist
    and check to see any of them do not equal 1
    return 1 if all are 1
    return 0 otherwise
    """
    
def isReducible(poly,field,n):
    poly.replace(" ","")
    field.replace(" ","")
    coefs = getCoefficients(poly,field,n)
    dlist = getDivisors(n);
    """STUCK.  I have to find gcd(f,x^p^d-x)"""
    are_all_gcd_1 = allGCDs(coefs,dlist)
    if are_all_gcd_1 == 1:
        return 0
    elif are_all_gcd_1 != 1:
        return 1
    return -1
    
    

def main():
    poly = input("Hello, I hope you are doing well! My name is Reducibility Checker, and I am here to help you find out if your polynomial is reducible or not. Let's get to it!  Can you enter the polynomial you wish to check:")
    field = input("Great! Could you also tell me characteristic of the field.  If you do not know this please type 'Help':")
    n = input("Ok! Last thing before I work my magic.  What is the degree of the polynomial?")
    print("Working my magic...")
    '''TODO: If characteristic of the field is 0'''
    if field.lower() == "help":
        print("In mathematics, the characteristic of a ring R, often denoted char(R), is defined to be the smallest number of times one must use the ring's multiplicative identity (1) in a sum to get the additive identity (0). If this sum never reaches the additive identity the ring is said to have characteristic zero.")
    canReduce = isReducible(poly,field,n)
    if canReduce == 1:
        print("Oops! Looks like the polynomial you entered can be reduced. Keep trying!")
    elif canReduce == 0:
        print("Hooray! The polynomial you entered is irreducible!")
    if canReduce == -1:
        print("Error")
    return


if __name__ == '__main__':
    main()