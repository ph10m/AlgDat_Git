#
# def nullify(A, d):
#     # add missing 0's in front of each array.
#     for item in A:
#         while len(item)<d:
#             item.insert(0, 0)

# def clearify(A, d):
#     # remove leading 0's
#     for item in A:
#         while (item[0]==0):
#             del item[0]
#
# def sortify(A, d, BASE = 26):
#     C = dict((q,[]) for q in range(BASE+1))
#     print_dict(C)
#     sub_array = 0
#     for i in range (d-1,-1,-1): # go from the last index and upwards
#         for subArr in A:
#             index = subArr[i]
#             C[index].append(subArr)
#         print ('--------------')
#         print ('Dict:')
#         print_dict(C)
#         print ('______________')
#         print ('The new array:')
#         A = [y for x in C.values() for y in x if y != []]
#         print (A)
#         print ('______________')
#         C = dict((q,[]) for q in range(BASE+1))
#     print ('Clearing up zeros...')
#     clearify(A, d)
#     print (A)
#     print ('Converting back to chars...')
#     charify(A, d)



    # test = [[1, 0], [1, 5], [1], [6, 0], [5], [1, 0, 0], [2, 5], [5, 0]]
    # print (test)
    # nullify(test, 3) # 0's added
    # print (test)
    # sortify(test, 3, 9)