with open('C:/Users/torresv1/Desktop/product.py', 'r') as file1:
    with open('C:/Users/torresv1/Desktop/product_jose.py', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('/n')

with open('C:/Users/torresv1/Desktop/productfile_comparison.txt', 'w') as FO:
    for line in same:
        FO.write(line)