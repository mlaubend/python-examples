def even_minus_odd(start, end, multiple=None, first_digit=None):
    evenlist = []
    oddlist = []   
    first = str(first_digit)
    
    for element in range(start, end+1):
        if multiple == None or (element%multiple==0) and (first_digit ==None or str(element).startswith(first)):
            if element%2 ==0:
                evenlist = evenlist + [element]
            else:
                oddlist = oddlist + [element]

    print(evenlist)
    print(oddlist)
    return (sum(evenlist)- sum(oddlist))

print (even_minus_odd(0,100,1,1))
