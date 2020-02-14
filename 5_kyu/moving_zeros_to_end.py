# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    new_array  =[] 
    zeros_found =[]
    
    for i in range(len(array)):
        if array[i] == 0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros_found.append(array[i])
            else:
                new_array.append(array[i])
        else:
            new_array.append(array[i])
    return new_array + zeros_found
