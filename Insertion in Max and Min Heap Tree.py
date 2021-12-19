
def MaxHeap(a,value):          #Inserting a value in given Max Heap
    a.append(value)
    i=len(a)-1
    
    while i>0:
        parent_index=(i-1)//2
        
        if(a[i]>a[parent_index]):
            a[i],a[parent_index]=a[parent_index],a[i]
            i=parent_index
            
    else:
        return a
       
def MinHeap(a,value):       #Inserting a value in given Min Heap
    a.append(value)
    i=len(a)-1
    
    while i>0:
        parent_index=(i-1)//2
        
        if(a[i]<a[parent_index]):
            a[i],a[parent_index]=a[parent_index],a[i]
            i=parent_index
            
    else:
        return a
        
if __name__=='__main__':
    arr_max_heap=[70,50,60,40,20]
    value1=int(input("Enter value to insert in Max Heap: "))
    print('Max Heap is: ',MaxHeap(arr_max_heap,value1))
    arr_min_heap=[20,30,40,50,60]
    value2=int(input("Enter value to insert in Min Heap: "))
    print('Min Heap is: ',MinHeap(arr_min_heap,value2))