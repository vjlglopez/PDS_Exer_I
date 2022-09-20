def count_and_print(n):
    for i in range(1, n+1):
        if i % 6 == 0:
            print(str(i) + " foo")
        elif i % 3 == 0:
            print(str(i) + " fuzz")
        elif i % 2 == 0:
            print(str(i) + " fizz")
        else:
            print(i)


def overlap_interval(start1, end1, start2, end2):
    list1 = list(range(int(start1),int(end1)+1))
    list2 = list(range(int(start2),int(end2)+1))
    list3 = [values for values in list1 if values in list2]
    
    if len(list3) == 0:
        print('No overlap!')   
    else:
        print(str(min(list3)) + " " + str(max(list3)))
        

def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


def cosine(theta):
    n = 0
    value = 1 
    sum_mac = 0 
    
    while abs(value) >= 10**(-15):
        value = ((-1)**n * theta**(2*n))/factorial(2*n)
        sum_mac += value
        n += 1
        
    return sum_mac


def gcd(a, b):
    i = 1
    val = 0
    while(i <= a and i <= b):
        if(a % i == 0 and b % i == 0):
            val = i
        i = i + 1
    return val


def biased_sum(*args, base = 2):
    if len(args) == 0:
        print('None')
    
    total = []
    for i in args:
        if i % base == 0:
            total.append(2 * i)
        else:
            total.append(i)
            
    return sum(total)


def last_in_sequence(digits):
    if '0' not in digits:
        return None    
    else:
        x = []
        for number in digits:
            if number == '0':
                x.append(int(number))
            elif (len(x) !=0) and (number == str(x[-1]+1)):
                x.append(int(number))
        return  x[-1]


def check_password(pwd):
    if len(pwd) < 8:
        return False
    else:
        lower = False
        upper = False
        number = False
        
        for i in range(len(pwd)):
            if pwd[i].islower():
                lower = True
            elif pwd[i].isupper():
                upper = True
            elif pwd[i].isnumeric():
                number = True
                
    if lower and upper and number:
        return True
    else:
        return False


def is_palindrome(text):
    if len(text) == 0:
        return False
    else:
        forward = text.strip()
        reverse = forward[::-1]
        if forward == reverse:
            return True
        else:
            return False


def create_squares(num_stars):
    fixed_line = ("+ " + "- " * num_stars) * 2 + "+" + '\n'
    row_star_first = ""
    row_space_first = ""
    for i in range(0, num_stars):
        row_star_first += ("| " + ("* " * num_stars) + "| "
                           + ("  " * num_stars) + "|" + '\n')
        row_space_first += ("| " + ("  " * num_stars) + "| "
                            + ("* " * num_stars) + "|" + '\n')
    fin_ans = (fixed_line + row_star_first +
               fixed_line + row_space_first + fixed_line)
    return fin_ans


def create_grid(dim_block, num_stars):
    line = ("+ " + "- " * num_stars) * dim_block + "+" + '\n'
    line1 = ("+ " + "- " * num_stars) * dim_block + "+ " + "- " + "+" + '\n'
    row1 = ""
    row2 = ""
    dimension = int(dim_block / 2)
    if dim_block == 1:
        for i in range(0, num_stars):
            row1 += "| " + ("* " * num_stars) + "|" + '\n'
        return line + row1 + line          
    elif dim_block % 6 == 0:
        for i in range(0, num_stars):
            row1 += (("| " + ("* " * num_stars) + "| " + ("  " * num_stars)) *
                     dimension + ("| " + ("* " * num_stars)) + "|" + '\n')
            row2 += (("| " + ("  " * num_stars) + "| " + ("* " * num_stars)) *
                     dimension + ("| " + ("  " * num_stars)) + "|" + '\n')
        return (line1 + row1 + line1 + row2) * dimension + line1
    elif dim_block % 3 == 0:
        for i in range(0, num_stars):
            row1 += (("| " + ("* " * num_stars) + "| " + ("  " * num_stars)) *
                     dimension + ("| " + ("* " * num_stars)) + "|" + '\n')
            row2 += (("| " + ("  " * num_stars) + "| " + ("* " * num_stars)) *
                     dimension + ("| " + ("  " * num_stars)) + "|" + '\n')
        return (line + row1 + line + row2) * dimension + line
    else:
        for i in range(0, num_stars):
            row1 += (("| " + ("* " * num_stars) + "| " +
                      ("  " * num_stars)) * dimension + "|" + '\n')
            row2 += (("| " + ("  " * num_stars) + "| " +
                      ("* " * num_stars)) * dimension + "|" + '\n')
        return (line + row1 + line + row2) * dimension + line

