from itertools import combinations

def negate(literal):
    return literal[1:] if literal.startswith('~') else '~' + literal

def resolve(ci, cj):
    resolvents = []
    for li in ci:
        for lj in cj:
            if li == negate(lj):
                new_clause = set(ci.union(cj))
                new_clause.discard(li)
                new_clause.discard(lj)
                resolvents.append(new_clause)
    return resolvents

def resolution_entailment(KB, query):
    negated_query = negate(query)
    clauses = KB + [{negated_query}]
    new = set()
    step = 0

    print("\n--- Resolution Process ---")
    print("Initial clauses (KB ∪ ¬Q):")
    for c in clauses:
        print(" ", c)
    print("\n---------------------------------------------------")

    while True:
        pairs = list(combinations(clauses, 2))
        progress = False

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for r in resolvents:
                step += 1
                print(f"\nStep {step}: Resolving {ci} and {cj}")
                if not r:
                    print("  → Derived EMPTY CLAUSE □ (Contradiction Found!)")
                    return True
                print(f"  → New clause: {r}")
                new.add(frozenset(r))
                progress = True

        new_clauses = new.difference(map(frozenset, clauses))
        if not new_clauses:
            print("\nNo new clauses can be derived → Entailment failed.")
            return False

        print(f"\nAdded {len(new_clauses)} new clause(s) this round.")
        print("---------------------------------------------------")

        for c in new_clauses:
            clauses.append(set(c))

def build_wumpus_kb():
    KB = []
    KB += [
        {'B11', '~P12'}, {'B11', '~P21'},
        {'B12', '~P11', '~P22'},
        {'B21', '~P11', '~P22'},
    ]
    KB += [
        {'S11', '~W12'}, {'S11', '~W21'},
        {'S12', '~W11', '~W22'},
        {'S21', '~W11', '~W22'}
    ]
    KB += [{'~B11'}, {'~S11'}, {'~B12'}, {'~S12'}, {'~B21'}, {'~S21'}]
    KB += [{'~P11'}, {'~W11'}]
    return KB

if __name__ == "__main__":
    KB = build_wumpus_kb()
    query = input("Enter the literal to check (e.g., ~P12 or W22): ").strip()
    result = resolution_entailment(KB, query)
    print("\n==================== RESULT ====================")
    if result:
        print(f"✅ The KB ENTAILS {query} → It is TRUE based on KB")
    else:
        print(f"❌ The KB DOES NOT ENTAIL {query} → Cannot prove it")
    print("================================================")
