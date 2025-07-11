# No numbers and Single arguments only. THESE FUNCTIONS REPRESENT BEHAVIOR THERE IS NO BITS OR DATA STRUCTURE
# CANT STORE DATA however in these examples we will store data to demonstrate what is happening
def f(x):
    return x


def f(x):
    def g(y):
        return x(y)

    return g


# The Switch
def LEFT(a):
    def f(b):
        return a

    return f


def RIGHT(a):
    def f(b):
        return b

    return f


# Currying
# Taking multipul argument functions and turn it into a single argument
def add(x):
    def f(y):
        return x + y

    return f


# The TRUE value function
# Typed similarly to Switch function
def TRUE(x):  # Just like the SWITCH function
    return lambda y: x  # TRUE(x)(y) chooses the left

def FALSE(x):
    return lambda y: y  # FALSE(x)(y) chooses the right


# Boolean Logic
def NOT(x):
    return x(FALSE)(TRUE)
# NOT = lambda x: x(FALSE)(TRUE)


def OR(x):  # First input (is TRUE) sub x and second input (is FALSE) sub y
    return lambda y: x(x)(y)            # Sub x and becomes TRUE(TRUE)(y) then sub y becomes TRUE(TRUE)(FALSE)


def AND(x):                             # AND = Lambda xy: xyx
    return lambda y: x(y)(x)

def IF(b):
    return lambda t: lambda f: b(t)(f)
IFELSE = lambda p: lambda a: lambda b: p(a)(b)      # P is either TRUE or FALSE

# Numerical Representation
ZERO = lambda f: lambda x: x  # ZERO is written just like FALSE. This is why 0 is False and 1 is True.
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = lambda f: lambda x: f(f(f(f(x))))
# To represent a number we count the number of n times a function is being called.
def incr(x):
    """This is an example of incrementing a number"""
    return x + 1  # This is illegal in lambda calc rules

# Mathamatical Representation
# 0 is a number and the successor is the next number
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))     # n(ONE) this increments ONE n times
ADD = lambda x: lambda y: y(SUCC)(x)
MUL = lambda x: lambda y: lambda f: y(x(f))

#Reversing Functions
CONS = lambda a: lambda b: lambda s: s(a)(b)      # This is a PAIR (a, b) use TRUE or FALSE to pick a or b.
CAR = lambda p: p(TRUE)                             # Choose HEAD.
CDR = lambda p: p(FALSE)                            # Choose TAIL.
ISEMPTY = lambda l: l(lambda h: lambda t: FALSE)       # Determine whether a list is NIL or non-NIL.
NIL = lambda x: TRUE                                # TRUE is the termination of the list
                                                    # Non-NIL list is as a function that "stores" the head and tail of the list

T = lambda p: CONS(SUCC(CAR(p)))(CAR(p))            # This takes one argument and creats a pair (a+1, a)
PRED = lambda n: CDR(n(T)(CONS(ZERO)(ZERO)))        # This gives us the predessor a in (a+1, a)

SUB = lambda x: lambda y: y(PRED)(x)

ISZERO = lambda n: n(lambda f: EVAL_FALSE)(EVAL_TRUE)

# Evaluating
EVAL_TRUE = lambda x: lambda y: x()                 # Added a call function, x(), so Python can evaluate that function when needed
EVAL_FALSE = lambda x: lambda y: y()
FACT = lambda n: ISZERO(n)(lambda: ONE)(lambda: MUL(n)(FACT(PRED(n))))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''SWITCH'''
    print(LEFT('5v')('gnd'))                    # The LEFT and RIGHT functions are taking two inputs
    print(RIGHT('5v')('gnd'))

    '''CURRYING'''
    print('\n')
    print(add(2)(3))

    ''' BOOLEAN LOGIC'''
    print('\n')
    print(NOT(TRUE))                            # Output is FALSE.
    print(NOT(FALSE))                           # Output is TRUE.
    print(AND(TRUE)(TRUE))                      # Output is TRUE.
    print(AND(TRUE)(FALSE))                     # Output is FALSE.
    print(AND(FALSE)(TRUE))                     # Output is FALSE.
    print(AND(FALSE)(FALSE))                    # Output is FALSE.
    print(OR(TRUE)(FALSE))                      # Output is TRUE.

    '''NUMERICAL REPRESENTAION'''
    print('\n')
    print(incr(0))                              # 0 is an x of incr
    print(incr(incr(0)))
    print(incr(incr(incr(0))))
    print(THREE(incr)(0))                       # Repeats incr  function three times
    print(THREE(THREE)(incr)(0))                # Repeats incr function three to the Third times, so 3*3*3

    '''MATHAMATICAL REPRESENTATION'''
    print('\n')
    print(SUCC(TWO)(incr)(0))                   # Successor of two increments from 0 is 3
    print(SUCC(SUCC(THREE))(incr)(0))           # Incremnt 0 three times and find the successor of the successor = 5
    print(ADD(FOUR)(THREE)(incr)(0))            # Output is 7.
    print(SUCC(SUCC)(THREE)(incr)(0))           # This one is hard to explain but output is 3*4=12
    print(MUL(FOUR)(THREE)(incr)(0))            # 3*4=12 using MUL

    '''REVERSING FUNCTIONS'''
    print('\n')
    print(CAR(CONS(2)(3)))
    print(CDR(CONS(2)(3)))
    print(CAR(CONS(2)(CONS(3)(4))))             # Selecting the head of a Linked list = [2,3,4]
    print(CDR(CONS(2)(CDR(CONS(3)(4)))))        # Selecting the tail of a Linked list = [2,3,4]
    print(CDR(CONS(2)(CAR(CONS(3)(4)))))        # Selecting the middle of a Linked list = [2,3,4]
    print(ISEMPTY(CDR(CONS(2)(NIL))))           # Goes through the list until it reaches NIL returns TRUE
    print(CAR(FOUR(T)(CONS(ZERO)(ZERO)))(incr)(0))  # Output is 4
    print(CDR(FOUR(T)(CONS(ZERO)(ZERO)))(incr)(0))  # This is 4 previous, 3
    print((FOUR(THREE))(incr)(0))                   # 3^4 is 81
    print(PRED(FOUR(THREE))(incr)(0))               # The predessor of 3^4 is 80
    print(SUB(FOUR)(THREE)(incr)(0))                # 4-3 = 1
    print(FACT(THREE)(incr)(0))                     # 3!

    '''TESTS'''
    print('\n')
    s = CONS(FALSE)(TRUE)
    list_ = CONS(TRUE)(CONS(FALSE)(CONS(FALSE)(CONS(TRUE)(CONS(TRUE)(CONS(FALSE)(CONS(TRUE)(NIL)))))))

    def tf(t):
        return lambda s: t(t(CAR(s))(t))(CDR(s))

    def p(s):
        return s("HI")("BYE")
    #tf = lambda s: s(s(CAR(s))(s))(CDR(s))
    print(CAR(s))
    print(CDR(s))
    print(tf(NOT(CAR(s)))(s))
    print(FALSE)
    print(p(TRUE))
    print(ISEMPTY)
