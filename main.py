if __name__ == "__main__":
    M = N = 0
    flag_positive = flag_negative = True
    i = 0
    while flag_positive or flag_negative:
        if flag_positive:
            x_pos = eval(str(i+1))
            y_pos = eval(str(i+1))
            flag_positive = id(x_pos) == id(y_pos)
            if not flag_positive:
                N = i
        if flag_negative:
            x_neg = eval(str(-i-1))
            y_neg = eval(str(-i-1))
            flag_negative = id(x_neg) == id(y_neg)
            if not flag_negative:
                M = i
        i += 1
    
    print(f"[-{M}; {N}]")
    # Output: [-5; 256]
    # M = 5, N = 256


