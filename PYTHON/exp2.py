# def towerOfHanoi(n, source, dest, temp):
#     if n == 1:
#         print("Move disk 1 from source", source, "to destination", dest)
#         return
#     towerOfHanoi(n-1, source, temp, dest)
#     print("Move disk", n, "from source", source, "to destination", dest)
#     towerOfHanoi(n-1, temp, dest, source)

# n = 4
# towerOfHanoi(n, 'A', 'C', 'B')




# a = int(input("Enter the number: "))
# b = int(input("Enter the number: "))
# c = lambda a, b: a if a > b else b
# print("greater number =>", c(a, b))


# # map function to add 2 list
# l1 = [i for i in range(1, 11)]
# l2 = [i for i in range(11, 21)]
# l3 = list(map(lambda x,y:x+y, l1, l2))
# print(l3)

# # filter to find cube of all odd numbers
a = [1,2,3,4,5,6,7,8,9,10]
a2 = filter(lambda x: x % 2 != 0, a)
a3 = map(lambda x: x**3, a2)
final_list = list(a3)
print(final_list)


