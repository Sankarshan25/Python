def search(lst,i):
    pos=0
    m=0
    found=False
    for m in range(len(lst)):
        if lst[m]==i:
            found=True
            print(i,"found at index ",m)
            break
    
    if not found:    
        print("Not found")

if __name__=='__main__':
    lst=[10,4,6,20,7,35,8]
    i=int(input("Enter element to search: "))
    search(lst,i)
    
