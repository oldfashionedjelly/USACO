def find_majority_hay(N, hay_types):
    count = {}
    majority_types = set()

    for hay in hay_types:
        count[hay] = count.get(hay, 0) + 1
        if count[hay] > N // 2:
            majority_types.add(hay)

    if not majority_types:
        return -1

    return sorted(majority_types)

if __name__ == "__main__":
    with open("input1.txt", 'r') as file:
        T = int(file.readline().strip())

        for _ in range(T):
            N = int(file.readline().strip())
            hay_types = list(map(int, file.readline().split()))

            result = find_majority_hay(N, hay_types)

            if result != -1:
                print(" ".join(map(str, result)))
            else:
                print(-1)
