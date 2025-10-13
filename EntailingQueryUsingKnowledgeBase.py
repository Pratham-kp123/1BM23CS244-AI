def processsing_kb_rule(kb_rule):
    kb_rule = kb_rule.replace('~', ' not ')
    kb_rule = kb_rule.replace('^', ' and ')
    kb_rule = kb_rule.replace('v', ' or ')
    return kb_rule

def formatting_kb_rule(kb_rule, P, Q, R):
    P, Q, R = str(P), str(Q), str(R)
    kb_rule = kb_rule.replace('P', P)
    kb_rule = kb_rule.replace('Q', Q)
    kb_rule = kb_rule.replace('R', R)
    return kb_rule
kb = [
        (False, False, False),
        (False, False, True),
        (False, True, False),
        (False, True, True),
        (True, False, False),
        (True, False, True),
        (True, True, False),
        (True, True, True)
    ]
def to_check_entailment(kb_rule, query):
    
    is_entails = True
    
    kb_rule = processsing_kb_rule(kb_rule)
    
    for i, j, k in kb:
        formatted_rule = formatting_kb_rule(kb_rule, i, j, k) 
        print(f'To Evaluate: {formatted_rule}')
        KB = eval(formatted_rule)
        
        if query=='R':
            act_query = k
        elif query=='P':
            act_query = i
        else:
            act_query = j
        
        print(f'Knowledge Base: {KB}      Query: {act_query}',end="\n\n")
        
        if KB and not (KB and act_query):
            is_entails = False
            break

    if is_entails:
        print('Knowledge Base entailing the query')
    else:
        print("Knowledge Base doesn't entailing the query")

kb_rule = input('Enter the KB_rule: ')

query = input('Enter the query: ')
to_check_entailment(kb_rule, query)
