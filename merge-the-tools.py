def merge_the_tools(string, k):
    # your code goes here
    i =0
    while i < len(string):
        sub_s = string[i: i+k]
        sub_s2 = ''
        for j in sub_s:
            if j not in sub_s2:
                sub_s2 += j
        print(sub_s2)
        i += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
