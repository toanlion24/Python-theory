# MỤC LỤC - TÀI LIỆU HỌC PYTHON

## Tổng quan

Tài liệu này bao gồm 9 bài học về Python, từ cú pháp cơ bản đến các kiểu dữ liệu, xử lý ngoại lệ, hàm và danh sách.

---

## 📚 Danh sách bài học

### [Bài 1: Cú Pháp Cơ Bản Python](./01_Basic_Python_Syntax.ipynb)
**Nội dung chính:**
- Comments (Ghi chú)
- Variables (Biến)
- Indentation (Thụt lề)
- Print Statement (Câu lệnh in)
- Input Statement (Câu lệnh nhập)
- Data Types (Kiểu dữ liệu)
- Operators (Toán tử)
- String Operations (Thao tác với chuỗi)
- Conditional Statements (Câu lệnh điều kiện)
- Loops (Vòng lặp)
- Functions (Hàm - Cơ bản)
- Scope (Phạm vi biến)
- Error Handling (Xử lý lỗi - Cơ bản)

---

### [Bài 2: Biến và Kiểu Dữ Liệu](./02_Variables_and_Data_Types.ipynb)
**Nội dung chính:**
- Variables (Biến)
  - Khai báo và sử dụng biến
  - Quy tắc đặt tên biến
  - Multiple Assignment
- Data Types (Kiểu dữ liệu)
  - Numeric Types: int, float, complex
  - String (str)
  - List (Danh sách)
  - Tuple (Bộ dữ liệu)
  - Dictionary (dict - Từ điển)
  - Set (Tập hợp)
  - Boolean (bool)
- Kiểm tra và chuyển đổi kiểu dữ liệu
- Mutable vs Immutable

---

### [Bài 3: Làm Việc Với Chuỗi](./03_Working_with_Strings.ipynb)
**Nội dung chính:**
- Tạo Chuỗi (String Creation)
- Nối Chuỗi (String Concatenation)
- Truy Cập Ký Tự và Cắt Chuỗi (Indexing & Slicing)
- Các Phương Thức Chuỗi Phổ Biến
  - upper(), lower(), title(), capitalize()
  - strip(), lstrip(), rstrip()
  - find(), index(), count()
  - replace()
  - split(), join()
  - isdigit(), isalpha(), isalnum()
- Định Dạng Chuỗi (String Formatting)
  - F-strings (Formatted String Literals)
  - format() method
  - % formatting
- Escape Sequences (Ký Tự Đặc Biệt)
- Raw Strings (Chuỗi Thô)
- Multiline Strings (Chuỗi Nhiều Dòng)
- String Immutability (Tính Bất Biến Của Chuỗi)
- Ví Dụ Ứng Dụng Thực Tế

---

### [Bài 4: Câu Lệnh Điều Kiện](./04_Conditional_Statements.ipynb)
**Nội dung chính:**
- Giới thiệu về Câu lệnh Điều kiện
- Câu lệnh IF đơn giản
- Câu lệnh IF-ELSE
- Câu lệnh IF-ELIF-ELSE
- Các Toán tử So sánh
  - ==, !=, <, >, <=, >=
  - is, is not
  - in, not in
- Các Toán tử Logic
  - and, or, not
- Câu lệnh Điều kiện Lồng nhau (Nested Conditionals)
- Toán tử Ternary (Toán tử 3 ngôi)
- Giá trị Truthy và Falsy
- So sánh Chuỗi (String Comparison)
- Các Ví dụ Thực tế
  - Máy tính BMI
  - Kiểm tra năm nhuận
  - Máy tính đơn giản
  - Kiểm tra mật khẩu
- Lưu ý và Best Practices
- Bài tập Thực hành

---

### [Bài 5: Vòng Lặp](./05_Loops.ipynb)
**Nội dung chính:**
- Giới thiệu về Vòng lặp (Loops)
- Vòng lặp FOR
  - Lặp qua danh sách, chuỗi
  - Tính tổng các số
- Hàm RANGE()
  - range(stop)
  - range(start, stop)
  - range(start, stop, step)
- Vòng lặp FOR với enumerate()
- Vòng lặp FOR với Dictionary
- Vòng lặp WHILE
- So sánh FOR và WHILE
- Vòng lặp Lồng nhau (Nested Loops)
  - Bảng cửu chương
  - Vẽ hình tam giác, chữ nhật
- Câu lệnh BREAK
- Câu lệnh CONTINUE
- Câu lệnh ELSE với Vòng lặp
- Vòng lặp với List Comprehension
- Các Ví dụ Thực tế
  - Tính trung bình điểm số
  - Đếm số lần xuất hiện của ký tự
  - Tìm số lớn nhất và nhỏ nhất
  - Kiểm tra chuỗi đối xứng (palindrome)
  - Tính dãy Fibonacci
- Lưu ý và Best Practices
  - Tránh Vòng lặp Vô hạn
  - Sử dụng biến tạm thời đúng cách
  - Tránh sửa đổi danh sách trong khi lặp
  - Sử dụng enumerate() thay vì range(len())
  - Chọn FOR hay WHILE?
  - Tối ưu hiệu suất
- Bài tập Thực hành

---

### [Bài 6: Typecasting (Ép Kiểu Dữ Liệu)](./06_Typecasting.ipynb)
**Nội dung chính:**
- Khái niệm Typecasting
- Ép kiểu ngầm định (Implicit Type Casting)
- Ép kiểu tường minh (Explicit Type Casting)
- Chuyển đổi sang int, float, str, bool
- Chuyển đổi giữa các kiểu dữ liệu collection
- Các lưu ý và best practices

---

### [Bài 7: Exceptions (Xử lý Ngoại lệ)](./07_Exceptions.ipynb)
**Nội dung chính:**
- Khái niệm về Exceptions
- Các loại Exception phổ biến
  - SyntaxError, TypeError, ValueError
  - IndexError, KeyError, ZeroDivisionError
  - FileNotFoundError, AttributeError, NameError
- Xử lý Exceptions với try-except
- try-except-else
- try-except-finally
- Xử lý nhiều loại exception
- Nested try-except
- Raise exceptions
- Custom exceptions
- Best practices

---

### [Bài 8: Functions và Built-in Functions](./08_Functions_and_builtin_functions.ipynb)
**Nội dung chính:**
- Khái niệm về Functions
- Định nghĩa và gọi Function
- Các loại tham số
  - Positional Arguments
  - Keyword Arguments
  - Default Arguments
  - Variable-length Arguments (*args, **kwargs)
- Return values
- Scope và Namespace
- Lambda functions
- Built-in Functions
  - print(), input(), len()
  - type(), isinstance()
  - min(), max(), sum()
  - sorted(), reversed()
  - range(), enumerate(), zip()
  - map(), filter(), reduce()
- Decorators (Cơ bản)
- Recursion (Đệ quy)
- Best practices

---

### [Bài 9: Lists (Danh sách) trong Python](./09_Lists_in_Python.ipynb)
**Nội dung chính:**
- Khái niệm về Lists
- Tạo Lists (rỗng, có phần tử, từ các kiểu dữ liệu khác)
- Truy cập phần tử (index dương/âm, slicing)
- Thay đổi và cập nhật phần tử
- Thêm phần tử (append, extend, insert)
- Xóa phần tử (remove, pop, del, clear)
- Các phương thức quan trọng
  - len(), count(), index()
  - sort(), sorted(), reverse()
  - copy()
- Kiểm tra phần tử (in, not in)
- Duyệt qua List (iteration)
- List Comprehension
  - Cơ bản
  - Với điều kiện
  - Với if-else
  - Lồng nhau
- Nested Lists (List lồng nhau)
- Các hàm built-in hữu ích (min, max, sum, all, any)
- So sánh Lists
- Ứng dụng thực tế
- Lưu ý quan trọng (tham chiếu vs sao chép, shallow copy vs deep copy)
- Performance và Best Practices

---

## 📖 Thứ tự học tập được khuyến nghị

1. **Bắt đầu với Bài 1** - Nắm vững cú pháp cơ bản của Python
2. **Tiếp tục với Bài 2** - Hiểu về biến và các kiểu dữ liệu
3. **Học Bài 3** - Làm quen với thao tác chuỗi
4. **Chuyển sang Bài 4** - Học cách sử dụng câu lệnh điều kiện
5. **Học Bài 5** - Nắm vững vòng lặp và các kỹ thuật lặp
6. **Học Bài 6** - Hiểu về ép kiểu dữ liệu
7. **Học Bài 7** - Xử lý ngoại lệ và lỗi
8. **Học Bài 8** - Làm việc với hàm và built-in functions
9. **Học Bài 9** - Nắm vững Lists và các thao tác với danh sách

---

## 💡 Lưu ý

- Mỗi bài đều có ví dụ code thực tế và bài tập thực hành
- Nên làm bài tập sau mỗi bài để củng cố kiến thức
- Thực hành nhiều để thành thạo Python
- Các file notebook (.ipynb) có thể mở bằng Jupyter Notebook hoặc VS Code

---


