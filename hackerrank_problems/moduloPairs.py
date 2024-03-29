def divisibleSumPairs(n, k, ar):
    rem = [0] * k
    count = 0
    for num in ar:
        count += rem[(k - num %k) % k]
        rem[num%k] += 1
    return count

n, k = 5, 2
ar = [5, 9, 10, 7, 4]

n, k = 100, 40
ar = list(map(int , "13 91 5 100 5 12 5 79 99 87 59 65 62 73 93 73 63 65 59 46 67 35 22 55 50 53 38 79 75 44 95 53 5 73 44 94 95 21 60 2 32 48 72 13 91 74 79 99 17 31 53 20 88 17 54 47 56 79 23 49 95 81 9 50 12 20 45 82 44 82 93 15 73 51 65 96 4 77 37 41 30 11 65 100 62 51 64 48 12 11 68 81 46 37 10 46 75 82 21 23".split()))

print(divisibleSumPairs(n, k, ar))