def check_brackets(input_lines):
    results = []
    
    for line in input_lines:
        marks = [' '] * len(line)
        stack = []
        
        for i, ch in enumerate(line):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    marks[i] = '?'
        
        while stack:
            marks[stack.pop()] = 'x'
        
        results.append((line, ''.join(marks)))
    
    return results

if __name__ == "__main__":
    input_lines = [
        "bge)))))))))",
        "((IIII))))))",
        "()()()()(uuu",
        "))))UUUU((()"
    ]
    
    results = check_brackets(input_lines)
    
    for original, marks in results:
        print(original)
        print(marks)
