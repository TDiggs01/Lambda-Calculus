dfa.py has two functions, dfa() and transitionFunction tf().

dfa() takes one parameter, list, and will return a boolean if the given list is a valid input. If the string is
accepted by the DFA, i.e. it reaches the accepting state by the end, then dfa() will return True. Otherwise,
it will return False.
NOTE: For this DFA, the List must have three or more 'TRUE's to reach the accepting state.

tf() takes one parameter, representing the DFA's current state. This function will be called
by dfa() to compute the new state based on the current state. This function exists to more explicitly represent the
transition function of the DFA.

Example of calling the dfa() to evaluate a list
list_ = PAIR(TRUE)(PAIR(FALSE)(PAIR(FALSE)(PAIR(TRUE)(PAIR(TRUE)(PAIR(FALSE)(PAIR(TRUE)(NIL)))))))
dfa(list_) --> return true