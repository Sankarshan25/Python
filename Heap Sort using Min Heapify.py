
def Heapsort(arr,n):
    
    for i in range(n//2-1,-1,-1):           #Build Min Heap
        MinHeapify(arr,n,i)
        
    for i in range(n-1,0,-1):               #Deleting from min heap and inserting at end of array to form
        arr[i],arr[0]=arr[0],arr[i]                                    #sorted array in descending order
        MinHeapify(arr,i,0)                                    
                                            
def MinHeapify(arr,n,i):            #building mean heap using Heapify method
    smallest=i
    left_child_index=2*i+1
    right_child_index=2*i+2
    
    if (left_child_index<n and arr[left_child_index]<arr[smallest]):
        smallest=left_child_index
        
    if (right_child_index<n and arr[right_child_index]<arr[smallest]):
        smallest=right_child_index
        
    if smallest!=i:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        MinHeapify(arr,n,smallest)
        
if __name__=='__main__':
    arr=[70,10,20,17,5,15,30]
    Heapsort(arr,len(arr))
    print('Array after sorting in descending order using HeapSort is: ',arr)
    