sizes = [10*10, 20*20, 30*20, 50*50, 50*100, 100*100]
values = [0.13, 0.23, 0.25, 0.28, 0.32, 0.43, 0.48, 0.26, 0.39, 0.55, 0.68, 0.80, 1.1, 1.35, 0.38, 0.53, 0.95, 1.5]
for value in values:
    for size in sizes:
        size_value = size / 100
        print((size_value*value)*1.2+(size_value*.05)
