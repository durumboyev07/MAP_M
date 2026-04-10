# 1
roy = [2, 4, 6, 8]
print(list(map(lambda x: x + 1, roy)))

# 2
roy = ["a", "b", "c"]
print(list(map(lambda x: x * 3, roy)))

# 3
roy = [7, 14, 21]
print(list(map(lambda x: x / 7, roy)))

# 4
roy = ["Python", "Java", "C++"]
print(list(map(lambda x: x.lower(), roy)))

# 5
roy = [1, 2, 3, 4]
print(list(map(lambda x: "son: " + str(x), roy)))
