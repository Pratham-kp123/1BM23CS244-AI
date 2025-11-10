def occurs_check(var, expr):
    if var == expr:
        return True
    elif isinstance(expr, list):
        return any(occurs_check(var, subexpr) for subexpr in expr)
    return False

def substitute(expr, var, val):
    if expr == var:
        return val
    elif isinstance(expr, list):
        return [substitute(subexpr, var, val) for subexpr in expr]
    else:
        return expr

def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    if isinstance(x, str) and x.islower():
        if x in subst:
            return unify(subst[x], y, subst)
        elif occurs_check(x, y):
            return None
        else:
            subst[x] = y
            return subst

    elif isinstance(y, str) and y.islower():
        if y in subst:
            return unify(x, subst[y], subst)
        elif occurs_check(y, x):
            return None
        else:
            subst[y] = x
            return subst

    elif x == y:
        return subst

    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        for xi, yi in zip(x, y):
            subst = unify(xi, yi, subst)
            if subst is None:
                return None
        return subst

    else:
        return None

if __name__ == "__main__":
    expr1 = ["Knows", "John", "x"]
    expr2 = ["Knows", "y", "Mary"]

    result = unify(expr1, expr2)
    if result:
        print("Unification successful. Substitution set:")
        for k, v in result.items():
            print(f"{k} / {v}")
    else:
        print("Unification failed.")
