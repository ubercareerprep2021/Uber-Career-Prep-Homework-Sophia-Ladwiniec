# runtime: O(N) we only pass through the N times, N being the number of elements in the array 
# I used a set for constant lookup time 
# space complexity: O(N) added a set to hold the differences to get the targetSum
def pairsThatEqualSum(inputArray, targetSum):
    differences = set()
    pairs = []
    for i in range(len(inputArray)): 
        value = targetSum - inputArray[i]
        if(value in differences):
            pairs.append([value, inputArray[i]])
        else:
            differences.add(inputArray[i])
    return pairs

def main():
    pairs = pairsThatEqualSum([1, 2, 3, 4, 5], 5)
    print("Input Array: [1, 2, 3, 4, 5] Target Sum: 5")
    print("Pairs:", pairs)

    pairs = pairsThatEqualSum([1, 2, 3, 4, 5], 1)
    print("Input Array: [1, 2, 3, 4, 5] Target Sum: 1")
    print("Pairs:", pairs)

    pairs = pairsThatEqualSum([1, 2, 3, 4, 5], 7)
    print("Input Array: [1, 2, 3, 4, 5] Target Sum: 7")
    print("Pairs:", pairs)


main()
