# python3

def read_input():
    input_type = input().rstrip()
    if input_type == 'F':
        with open("test/06") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        pattern = input().rstrip()
        text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 1000000007
    x = 1 
    m = len(pattern)
    n = len(text) 
    patternh = sum(ord(pattern[i]) * pow(x, i, p) for i in range(m)) % p
    texth = sum(ord(text[i]) * pow(x, i, p) for i in range(m)) % p
    position = []
    for i in range(n - m + 1):
        if patternh == texth:
            if pattern == text[i:i+m]:
                position.append(i)
        if i < n - m:
            texth = ((texth - ord(text[i]) * pow(x, m-1, p)) * x + ord(text[i+m])) % p
    return position

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
