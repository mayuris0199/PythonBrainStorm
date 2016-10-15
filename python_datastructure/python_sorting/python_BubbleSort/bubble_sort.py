def bubble_sort(b_list):
    print b_list
    for i in range(len(b_list)):
        for j in range(len(b_list)-1-i):
            if b_list[j] > b_list[j+1]:
                b_list[j], b_list[j+1] = b_list[j+1], b_list[j]
                print b_list
