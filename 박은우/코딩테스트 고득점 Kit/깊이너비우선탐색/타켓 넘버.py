def solution(numbers, target):

    super_node = [0]

    for i in numbers:
        sub_node = []
        for j in super_node:
            sub_node.append(j + i)
            sub_node.append(j - i)
        super_node = sub_node

    print(super_node)

    return super_node.count(target)


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
