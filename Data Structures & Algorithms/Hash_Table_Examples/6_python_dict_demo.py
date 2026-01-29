"""
Demo sử dụng Dictionary trong Python (Hash Table)
So sánh hiệu suất với List
"""

import time


def demo_dict_basic():
    """Demo các thao tác cơ bản với dict"""
    print("=" * 60)
    print("1. Các thao tác cơ bản với Dictionary (Hash Table)")
    print("=" * 60)
    
    # Tạo dictionary
    my_dict = {
        "apple": 100,
        "banana": 200,
        "cherry": 300
    }
    
    # Thêm phần tử
    print("Thêm phần tử:")
    my_dict["date"] = 400
    print(my_dict)
    
    # Truy xuất
    print("\nTruy xuất:")
    print(f"apple: {my_dict['apple']}")
    print(f"banana: {my_dict.get('banana')}")
    print(f"grape: {my_dict.get('grape', 'Not found')}")
    
    # Kiểm tra tồn tại
    print("\nKiểm tra tồn tại:")
    print(f"'apple' in my_dict: {'apple' in my_dict}")
    
    # Xóa phần tử
    print("\nXóa phần tử:")
    del my_dict["banana"]
    print(my_dict)


def compare_performance():
    """So sánh hiệu suất giữa Hash Table (dict) và List"""
    print("\n" + "=" * 60)
    print("2. So sánh hiệu suất: Hash Table (dict) vs List")
    print("=" * 60)
    
    # Tạo dữ liệu lớn
    large_dict = {i: i*2 for i in range(100000)}
    large_list = list(range(100000))
    
    # So sánh tốc độ tìm kiếm
    target = 99999
    
    # Hash table (dict) - O(1)
    start = time.time()
    _ = large_dict[target]
    dict_time = time.time() - start
    
    # List - O(n)
    start = time.time()
    _ = large_list.index(target)
    list_time = time.time() - start
    
    print(f"\nTìm kiếm phần tử {target} trong 100,000 phần tử:")
    print(f"Hash Table (dict): {dict_time*1000:.4f} ms (O(1))")
    print(f"List: {list_time*1000:.4f} ms (O(n))")
    if dict_time > 0:
        speedup = list_time / dict_time
        print(f"Hash Table nhanh hơn {speedup:.1f} lần!")


def demo_dict_features():
    """Demo các tính năng đặc biệt của dict"""
    print("\n" + "=" * 60)
    print("3. Các tính năng đặc biệt của Dictionary")
    print("=" * 60)
    
    # Dict comprehension
    squares = {x: x**2 for x in range(1, 6)}
    print(f"Dict comprehension: {squares}")
    
    # Nested dict
    nested = {
        "person1": {"name": "An", "age": 20},
        "person2": {"name": "Bình", "age": 25}
    }
    print(f"Nested dict: {nested}")
    
    # Default dict behavior
    counter = {}
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    print(f"Đếm từ: {counter}")


if __name__ == "__main__":
    demo_dict_basic()
    compare_performance()
    demo_dict_features()
