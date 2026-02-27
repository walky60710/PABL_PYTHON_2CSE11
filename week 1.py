#%% 1. Reverse the array; In place- cannot do what is done here(F)
arr = [1, 2, 3, 4, 5, 6, 7]

arr.reverse()
print(arr)



#%% 2. Find Min and max in a array(NH)

arr = [2, 3, 1, 4, 8, 6, 7]
a = arr[0]
b = arr[0]
for i in range(len(arr)):
    if a > arr[i]:
        a = arr[i]
    else:
        pass

    if b < arr[i]:
        b = arr[i]
    else:
        pass
print(a,b)

# print(min(arr))


## HW

#%% 3. Find the smallest array on the index given as 'k'; sort the array before (F)
# Use arr.sort(), Use QuickSort

arr = [3, 1, 4, 7, 9]
k = 3

arr_sort = sorted(arr)

print(arr_sort[k-1])


#%% 4.Union of two arrays; must be sorted(question says) (NH)

#Doesnt Handle Duplicates
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]  #using sorted array
c = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1

    elif a[i] > b[j]:
        c.append(b[j])
        j += 1

    else:
        c.append(a[i])
        i += 1
        j += 1

while i < len(a):
    c.append(a[i])
    i += 1
while j < len(b):
    c.append(b[j])
    j += 1

print(c)


#%% 5. Finding the max element
#Optimized method



#%% 6. Rotate the array clockwise (NH)
arr = [1, 2, 3, 4, 5]

last_element = arr.pop()
arr.insert(0, last_element)
print(arr)


#%% 7. Find the max subarray in a mixed array (NH-Memory)(DO Algorithm)

arr = [2, 3, -8, 7, -1, 2, 3]
cur = arr[0]

for i in range(1, len(arr)): #started from 1 as cur is essently 0 so we will be adding 2: 0 indexed and wasting time
    cur = cur + arr[i]
    cur = max(cur, arr[i])

print(cur)


#HW

#%% 8- Find a value's index in a given sorted array (O(logn)-Binary Search)(H)


def add_target(newlst, target):

    newlst.append(target)

    return newlst.index(target)




def lst_search(arr, k): #needs sorted array
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r)//2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            l = mid + 1
        else:
            r = mid - 1

    return add_target(arr, k)



lst = [1,3,6]
target_value = 5

print(lst_search(lst, target_value))

# for i in range(len(arr)) # O(n) non binary
#     if k == arr[i]:
#         print("Index",i)


#%% 9- Return the indices of the numbers that are adding up to the target value;
#Exactly one solution- no same element twice, and if i + j then not j + i (F- removed break)

nums = [2,7,11,15]
target = 13

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target and i != j:
            print(i,j)
        #break - we can remove that just start the 2nd loop from one ahead index



#%% 10- Every value jumps the index; the value is 2 so it  make jump of 2 index which lands on 4
# F

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

i = 0
while i < len(arr):
    print(arr[i])
    i += arr[i]

step = arr[0] #For loop doesnt updates range everytime
for i in range(0, len(arr), step):

    print(arr[i])
    step = arr[i]
