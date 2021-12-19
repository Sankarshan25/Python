def Heapsort(arr,n):
    
    for i in range(n//2-1,-1,-1):       #Building Max Heap
        MaxHeapify(arr,n,i)
    
    for i in range(n-1,0,-1):           #deleting elements from max heap and adding at end of array for sorting
        arr[i],arr[0]=arr[0],arr[i]
        MaxHeapify(arr,i,0)
    
def MaxHeapify(arr,n,i):
    largest=i
    left_child_index=2*i+1
    right_child_index=2*i+2
    
    if(left_child_index<n and arr[largest]<arr[left_child_index]):
        largest=left_child_index
        
    if(right_child_index<n and arr[largest]<arr[right_child_index]):
        largest=right_child_index
        
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        MaxHeapify(arr,n,largest)
        
if __name__=='__main__':
    arr=[70,10,20,17,5,15,30]
    Heapsort(arr,len(arr))
    print('Array after sorting in ascending order: ',arr)
    