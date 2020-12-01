#Githin Kurian
#ID:1580561

# TODO: Write a selection_sort_descend_trace() function that 
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        mx = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[mx]:
                mx = j
        numbers[i], numbers[mx] = numbers[mx], numbers[i]
        for x in numbers:
            print(x,end=" ")
        print()
    return numbers

if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = [int(x) for x in input().split()] 
    selection_sort_descend_trace(numbers)
