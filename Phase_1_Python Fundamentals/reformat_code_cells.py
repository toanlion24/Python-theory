import json
import re

# Read the notebook
with open('Python_Basics_Quiz_Advanced_100_Questions.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Define properly formatted code for each question
formatted_code = {
    1: ["x = [1, 2, 3]", "y = x", "y.append(4)", "print(x)"],
    2: ["a = [1, 2]", "b = a.copy()", "b.append(3)", "print(a, b)"],
    3: ["def f(x=[]):", "    x.append(1)", "    return x", "print(f(), f())"],
    4: ["x = 10", "def f():", "    global x", "    x = 20", "f()", "print(x)"],
    5: ["try:", "    a, b, c = [1, 2, 3, 4]", "    print(a, b, c)", "except Exception as e:", "    print('Error')"],
    6: ["a, *b, c = [1, 2, 3, 4, 5]", "print(a, b, c)"],
    7: ["x = [1, 2, 3]", "y = x[:]", "y[0] = 10", "print(x, y)"],
    8: ["a = [1, [2, 3]]", "b = a.copy()", "b[1][0] = 10", "print(a)"],
    9: ["x = 5", "y = x", "x = 10", "print(y)"],
    10: ["def outer():", "    x = 10", "    def inner():", "        nonlocal x", "        x = 20", "    inner()", "    return x", "print(outer())"],
    11: ["a = [[0]*3]*3", "a[0][0] = 1", "print(a)"],
    12: ["x = (1, 2, [3, 4])", "x[2].append(5)", "print(x)"],
    13: ["a = {1: 'a', 2: 'b'}", "b = a", "b[3] = 'c'", "print(a)"],
    14: ["x = {1, 2, 3}", "y = x", "y.add(4)", "print(x)"],
    15: ["def func(x, y=[]):", "    y.append(x)", "    return y", "print(func(1), func(2), func(3))"],
    16: ["a = [1, 2]", "b = a[:]", "print(a is b)"],
    17: ["x = 'hello'", "y = 'hello'", "print(x is y)"],
    18: ["a = 256", "b = 256", "print(a is b)"],
    19: ["a = 257", "b = 257", "print(a is b)"],
    20: ["def f(x, y, z):", "    return x+y+z", "print(f(1, z=3, y=2))"],
    21: ["s = 'Python'", "print(s[1:4:2])"],
    22: ["print('hello'[::2])"],
    23: ["s = 'Python'", "print(s[-1:-4:-1])"],
    24: ["print('Python'.split('h'))"],
    25: ["print('hello'.replace('l', 'L', 1))"],
    26: ["try:", "    s = 'Python'", "    s[0] = 'J'", "    print(s)", "except Exception as e:", "    print('Error')"],
    27: ["print('Python'.partition('th'))"],
    28: ["print('ab' * 3 + 'cd')"],
    29: ["print('Python'.center(10, '*'))"],
    30: ["print('hello world'.rsplit(' ', 1))"],
    31: ["print('Python'.zfill(10))"],
    32: ["print('hello'.endswith(('lo', 'la')))"],
    33: ["print('hello'.index('l', 3))"],
    34: ["print('Python'.ljust(10, '*'))"],
    35: ["print('hello'.find('x'))"],
    36: ["print('Python Programming'.rfind('m'))"],
    37: ["print('  hello  '.lstrip() + '|')"],
    38: ["print('Python'[1::2])"],
    39: ["print('Python'[::-2])"],
    40: ["print('Hello World'.swapcase())"],
    41: ["print(0 or [] or {} or 5)"],
    42: ["print(True and False or True)"],
    43: ["print(not (5 > 3 and 10 < 20))"],
    44: ["x = 5", "print('Big' if x > 10 else 'Medium' if x > 5 else 'Small')"],
    45: ["x = []", "y = x or 'default'", "print(y)"],
    46: ["print(1 < 2 < 3 < 4)"],
    47: ["print('a' in 'abc' and 'x' not in 'abc')"],
    48: ["x = None", "y = x if x else 'default'", "print(y)"],
    49: ["print(all([1, 2, 0, 4]))"],
    50: ["print(any([0, '', [], None]))"],
    51: ["x = 5", "print(10 if x == 5 else 20 if x == 10 else 30)"],
    52: ["print((5 < 10) + (10 < 5))"],
    53: ["x = 5", "y = 10", "print(x < y < 15)"],
    54: ["result = [] if False else [1, 2, 3]", "print(result)"],
    55: ["x = [1, 2, 3]", "print(x is not None and len(x) > 0)"],
    56: ["x = 0", "y = 1", "print(x or y)"],
    57: ["x = ''", "print(x or 'empty')"],
    58: ["x = 5", "y = 3", "(x, y) = (y, x)", "print(x, y)"],
    59: ["x = 10", "print(not (x > 5 and x < 20))"],
    60: ["x = [1]", "y = [2]", "z = [x, y]", "x.append(3)", "print(z)"],
    61: ["print([i for i in range(5) if i % 2 == 0])"],
    62: ["print([x*y for x in [1,2] for y in [3,4]])"],
    63: ["print([x for x in range(10) if x % 2 == 0 if x % 3 == 0])"],
    64: ["print([x if x > 5 else 0 for x in range(10)])"],
    65: ["print({x: x**2 for x in range(5)})"],
    66: ["print([x for x in 'hello' if x not in 'aeiou'])"],
    67: ["print({x for x in [1, 2, 2, 3, 3, 3]})"],
    68: ["for i in range(3):", "    pass", "else:", "    print('Done')"],
    69: ["for i in range(3):", "    break", "else:", "    print('Done')"],
    70: ["result = []", "[result.append(i) if i%2==0 else result.append(i*2) for i in range(5)]", "print(result)"],
    71: ["print([[i*j for j in range(3)] for i in range(2)])"],
    72: ["for i, v in enumerate(['a', 'b'], start=10):", "    print(i, v)"],
    73: ["print([x for x in range(10) if x % 2 == 0][:3])"],
    74: ["print(sum([i for i in range(5)]))"],
    75: ["print([(x, y) for x in [1, 2] for y in [3, 4] if x != y])"],
    76: ["print({i: i**2 for i in range(5) if i % 2 == 0})"],
    77: ["x = iter([1, 2, 3])", "next(x)", "print(next(x))"],
    78: ["result = []", "[result.extend([i, i*2]) for i in [1, 2]]", "print(result)"],
    79: ["print([i for i in range(5) if i > 2])"],
    80: ["print(list(zip([1, 2], [3, 4, 5])))"],
    81: ["def f(a, b, *args):", "    return len(args)", "print(f(1, 2, 3, 4, 5))"],
    82: ["def f(**kwargs):", "    return kwargs", "print(f(a=1, b=2))"],
    83: ["print((lambda x, y: x + y)(3, 4))"],
    84: ["def outer(x):", "    return lambda y: x + y", "f = outer(10)", "print(f(5))"],
    85: ["try:", "    1/0", "except:", "    pass", "finally:", "    print('Done')"],
    86: ["try:", "    int('abc')", "except ValueError as e:", "    print(type(e).__name__)"],
    87: ["print(sorted([3, 1, 2], reverse=True))"],
    88: ["print(list(map(lambda x: x*2, [1, 2, 3])))"],
    89: ["print(list(filter(lambda x: x > 3, [1, 2, 3, 4, 5])))"],
    90: ["def f(x=[]):", "    x.append(1)", "    return len(x)", "print(f(), f())"],
    91: ["print(isinstance([1, 2, 3], (list, tuple)))"],
    92: ["print({'a': 1, 'b': 2}.pop('c', 'default'))"],
    93: ["d = {'a': 1}", "d.setdefault('b', 2)", "d.setdefault('a', 3)", "print(d)"],
    94: ["s1 = {1, 2, 3}", "s2 = {3, 4, 5}", "print(s1 & s2)"],
    95: ["s1 = {1, 2}", "s2 = {2, 3}", "print(s1 | s2)"],
    96: ["s1 = {1, 2, 3}", "s2 = {2, 3}", "print(s1 - s2)"],
    97: ["s1 = {1, 2}", "s2 = {2, 3}", "print(s1 ^ s2)"],
    98: ["print(dict.fromkeys(['a', 'b', 'c'], 0))"],
    99: ["print([1, 2, 3].count(2))"],
    100: ["print('hello world'.split(maxsplit=1))"],
    101: ["import copy", "a = [1, [2, 3]]", "b = copy.deepcopy(a)", "b[1][0] = 10", "print(a)"]
}

# Process all cells
new_cells = []
question_num = 0

for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown':
        # Check if it's a question cell
        source = ''.join(cell['source'])
        if '## Question' in source:
            match = re.search(r'## Question (\d+)', source)
            if match:
                question_num = int(match.group(1))
        new_cells.append(cell)
    elif cell['cell_type'] == 'code':
        # Replace with properly formatted code
        if question_num in formatted_code:
            code_lines = formatted_code[question_num]
            cell['source'] = [line + '\n' for line in code_lines[:-1]] + [code_lines[-1]]
        new_cells.append(cell)
    else:
        new_cells.append(cell)

# Update notebook
notebook['cells'] = new_cells

# Write back
with open('Python_Basics_Quiz_Advanced_100_Questions.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print(f"Reformatted code cells - split single lines into multiple lines!")
