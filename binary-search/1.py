def binary_search(array, item):
    low = 0
    high = len(array) -1 # 10
    counter = 0

    while low <= high:
        mid = (low + high) // 2 # 5
        print(low, mid, high)
        guess = array[mid] #on 1st 5
        if guess == item:
            return mid, counter #on 1st 5
        elif guess > item:
            high = mid - 1 # 5 - 1 = 4
            counter += 1
        else: 
            low = mid + 1 #Beacuse if it isnt 5 on 1st guess, we set low to the 5 guess + 1 beacuse we know it isnt 5 !!!
            counter += 1
    return None


example_array = [i for i in range(1,11)] #1,2,3,4,5,6,7,9,10 (11 upper bound)
#print(len(example_array))
print(binary_search(example_array, 1))
#print( (0 + 10) // 2)