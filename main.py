def test(input1: list[int], target: int):

    output = []

    for i in input1:

        for j in input1:

            if i + j == target and input1.index(i) != input1.index(j):

                output.append(input1.index(i))

                output.append(input1.index(j))

                return output
    

print(test(input1=[-1, 15, -3, -4, 5, 20, 34, 56, -40, -10, -56, 41, 88], target=-50))
print(test(input1=[-1, 15, -3, -4, 5, 20, 34, 56, -40, -10, 11, 34, -68, 32, -2], target=25))

