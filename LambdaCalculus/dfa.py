# The TRUE and FALSE value function
TRUE = lambda x: lambda y: x  # TRUE(x)(y) chooses the left
FALSE = lambda x: lambda y: y  # FALSE(x)(y) chooses the right

PAIR = lambda a: lambda b: lambda s: s(a)(b)      # This is a PAIR (a, b) use TRUE or FALSE to pick a or b.
HEAD = lambda p: p(TRUE)                             # Choose HEAD.
TAIL = lambda p: p(FALSE)                            # Choose TAIL.
ISEMPTY = lambda l: l(lambda h: lambda t: FALSE)       # Determine whether a list is NIL or non-NIL.
NIL = lambda x: TRUE                                # TRUE is the termination of the list
IF = lambda b: lambda t: lambda f: b(t)(f)

def dfa(list_):
    # ===========================THIS DFA REQUIRES THREE '1's IN INPUT STRING TO PASS================================
    s = PAIR(FALSE)(TRUE)  # all possible states of the DFA

    # Checks the head of the list: FALSE or TRUE
    return IF(ISEMPTY(list_)(FALSE)(IF(HEAD(list_))((tf(HEAD(s))(s)))(tf(TAIL(s))(s))))

def tf(t):
    return lambda s: t(t(HEAD(s))(t))(TAIL(s))  # if true is input then it comes out false


#dfa('1001101')
list_ = PAIR(TRUE)(PAIR(FALSE)(PAIR(FALSE)(PAIR(TRUE)(PAIR(TRUE)(PAIR(FALSE)(PAIR(TRUE)(NIL)))))))
# dfa returns FALSE List is not accepted otherwise accepted with a TRUE
print(dfa(list_)("(TRUE) The string is accepted by the dfa.")("(FALSE) The string is not accepted by the dfa."))
