def calculate_score(a, b, c):
    a_mayor_b_mayor = a > 5 and b > 5
    c_mayor_a_menor = c > 10 and a < 3
    if (a_mayor_b_mayor) or (c_mayor_a_menor):
        return True
    return False