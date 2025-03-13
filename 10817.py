A, B, C = map(int, input().split())

if A>B:
    if B>C:
        print(B)
    elif C>B:
        if A>C:
            print(C)
        else:
            print(A)
    else:
        print(C)
elif A<B:
    if B>C:
        if A>C:
            print(A)
        else:
            print(C)
    elif B<C:
        print(B)
    else:
        print(C)
elif A==B:
    print(A)