def day3(file_name):
    with open(file_name, 'r') as f:
        day3_input = f.readlines()
        str_arr = []
        for input in day3_input:
            str_arr.extend(list(set([c for c in input[0:len(input)//2] if c in input[len(input)//2:]])))
        print(sol(str_arr))
        day3_input = [x.strip() for x in day3_input]
        day3_2_input = [day3_input[x:x+3] for x in range(0,len(day3_input),3)]
        str_arr = [list(set(c for c in i[0] if c in i[1] if c in i[2])) for i in day3_2_input]
        str_arr = [item for sublist in str_arr for item in sublist]
        print(sol(str_arr))

def sol(str_arr):
    ans = 0
    for input in str_arr:
        if input.isupper():
            ans += ord(input) - 65 + 27
        else:
            ans += ord(input) - 97 + 1
    return ans

if __name__ == "__main__":
    day3('day3_1.txt')
    day3('day3.txt')
