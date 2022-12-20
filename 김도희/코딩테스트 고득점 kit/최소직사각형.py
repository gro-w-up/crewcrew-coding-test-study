def solution(sizes):
    sizes = [sorted(size, reverse=True) for size in sizes]

    width = max([size[0] for size in sizes])
    height = max([size[1] for size in sizes])

    return width * height

