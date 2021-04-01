def isStringPermutation(s1, s2):
    if(len(s1) != len(s2)):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    if(s1 == s2):
        return True 
    return False

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
    print("Pairs that equal sum: ")
    pairs = pairsThatEqualSum([1, 2, 3, 4, 5], 5)
    print("Input Array: [1, 2, 3, 4, 5] Target Sum: 5")
    print("Pairs:", pairs)
    print("\n")

    pairs = pairsThatEqualSum([1, 2, 3, 4, 5], 1)
    print("Input Array: [1, 2, 3, 4, 5] Target Sum: 1")
    print("Pairs:", pairs)
    print("\n")

    pairs = pairsThatEqualSum([1, 2, 3, 4, 5], 7)
    print("Input Array: [1, 2, 3, 4, 5] Target Sum: 7")
    print("Pairs:", pairs)

    print("\n")
    print("Is string permutation: ")

    print("s1: asdf s2: fsda")
    print("Permutation:", isStringPermutation("asdf", "fsda"))
    print("\n")

    print("s1: asdf s2: fsa")
    print("Permutation:", isStringPermutation("asdf", "fsa"))
    print("\n")

    print("s1: asdf s2: fsax")
    print("Permutation:",isStringPermutation("asdf", "fsax"))

main()
