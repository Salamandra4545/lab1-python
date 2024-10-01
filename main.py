def find_oldest_parallel(students):
    for i in range(len(students)-1, -1, -1): 
        if students[i] > 120:
            return 5 + i  
    return None  
# Пример использования:
students = [90, 100, 130, 150, 110, 125, 140]  
print(find_oldest_parallel(students)) 


#2 задание
def insert_zero_columns(matrix, k):
    
    for row in matrix:
        row.insert(k, 0)
   
    for row in matrix:
        row.insert(k + 1, 0)
    return matrix

# Пример использования:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
result = insert_zero_columns(matrix, k)
for row in result:
    print(row)


#3 задание
def swap_min_max(lst):
    min_idx = lst.index(min(lst))
    max_idx = lst.index(max(lst))
    lst[min_idx], lst[max_idx] = lst[max_idx], lst[min_idx]
    return lst

# Пример использования:
lst = [3, 5, 1, 9, 2]
print(swap_min_max(lst))  


#4 задание
def to_set(data):
    result_set = set(data)
    return result_set, len(result_set)

# Пример использования:
data = [1, 2, 2, 3, 4]
print(to_set(data)) 

data_str = "abcabc"
print(to_set(data_str)) 

#5 задание
def sales_statistics(sales_data):
    customer_data = {}

    for line in sales_data:
        customer, product, quantity = line.split()
        quantity = int(quantity)

        if customer not in customer_data:
            customer_data[customer] = {}
        
        if product not in customer_data[customer]:
            customer_data[customer][product] = 0
        
        customer_data[customer][product] += quantity

    for customer in sorted(customer_data.keys()):
        print(f"Покупатель: {customer}")
        for product in sorted(customer_data[customer].keys()):
            print(f"  {product}: {customer_data[customer][product]}")

# Пример использования:
sales_data = [
    "Alice phone 2",
    "Alice laptop 1",
    "Bob phone 1",
    "Bob tablet 3",
    "Alice phone 1"
]

sales_statistics(sales_data)


