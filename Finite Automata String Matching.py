# Finite Automata String Matching

def table(pattern):
    m = len(pattern)
    unique = set(pattern)
    table ={}

    for state in range(m+ 1):
        state_transitions ={}
        for ch in unique:
            state_transitions[ch] = 0 
        table[state] = state_transitions
    
    for state in range(m+1):
        for ch in unique:
            table[state][ch] =next_state(pattern,state, ch)
    
    return table,unique

def next_state(pattern,state, char):
    m = len(pattern)
    if state <m and char == pattern[state]:
        return state + 1
    for next_state in range(state,0, -1):
        if pattern[next_state - 1] == char:
            return next_state
    return 0

def fa(text, pattern):
    m = len(pattern)
    n = len(text)
    
    transition_table, unique= table(pattern)
    
    state = 0
    for i in range(n):
        if text[i] in unique: 
            state = transition_table[state][text[i]]  
        else:
            state = 0  
        
        if state == m:
            print(f"Pattern found at index {i -m + 1}")
            state = 0  

print("\nFinite Automata String Matching Example:")
fa("sdsdcfklkooop", "op")
