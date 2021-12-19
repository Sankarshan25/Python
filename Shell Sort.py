def shell_sort(lst):
    gap=len(lst)//2
    while gap>0:
        for i in range(gap,len(lst)):
            anchor=lst[i]
            j=i
            while j>=gap and lst[j-gap]>anchor:
                lst[j]=lst[j-gap]
                j-=gap
            lst[j]=anchor
        gap=gap//2
        

if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]
    elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
    for elements in tests:
        shell_sort(elements)
        print(elements)