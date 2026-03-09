a_mat, a_eng = map(int, input().split())
b_mat, b_eng = map(int, input().split())

if a_mat > b_mat and a_eng > b_eng:
    print(1)
else:
    print(0)