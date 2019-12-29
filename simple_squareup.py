def square_up(input_array):
    x=[]
    for ele in input_array:
        num = ele*ele
        x.append(num)
    return x

output = square_up([1,2,3,4,5])
print(output)
