def BinarySearch(array,low,high,key):
    mid=int((low+high) / 2)
    if high<low:
        return-1
    if array[mid]<key:
        return BinarySearch(arr,mid+1,high,key)
    elif array[mid]>key:
        return BinarySearch(arr,low,mid-1,key)
    else:
        return mid
arr=[1,2,3,5]
low=0
high=len(arr)-1
key=3
pos=BinarySearch(arr,low,high,key)
if pos==-1:
    print("the element is not present in arraes")
else:
    print("the element isfound at:",pos)