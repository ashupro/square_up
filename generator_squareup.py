def square_up(input_array):
    for ele in input_array:
        yield ele*ele

output = square_up([1,2,3,4,5])

for ele in output:
    print(ele)

# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))

