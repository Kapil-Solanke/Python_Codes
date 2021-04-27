# def factorial_recursive(a):
#     if a == 1 or a == 0:
#         return 1;
#     else:
#         return a * factorial_recursive(a - 1)
#
#
# def factorial_iterative(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac


# print(factorial_recursive(5))

# This funcn gives number of fibonnica series at positon n
def fibonnica(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonnica(n - 1) + fibonnica(n - 2)


print(fibonnica(5))
