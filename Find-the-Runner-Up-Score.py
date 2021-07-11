if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
arr = list(set(arr))

winner = max(arr)
arr.remove(winner)

runner_up = max(arr)

print(runner_up)
