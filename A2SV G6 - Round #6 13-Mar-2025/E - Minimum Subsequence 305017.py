# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t = int(input())    
for _ in range(t):
    n = int(input())
    s = input()
    
    # Stacks to store subsequences
    zero_stack = []
    one_stack = []
    ans = [0] * n
    seq_count = 0
    
    for i in range(n):
        if s[i] == '0':
            if one_stack:
                seq_id = one_stack.pop()
            else:
                seq_count += 1
                seq_id = seq_count
            zero_stack.append(seq_id)
        else:  # s[i] == '1'
            if zero_stack:
                seq_id = zero_stack.pop()
            else:
                seq_count += 1
                seq_id = seq_count
            one_stack.append(seq_id)
        
        ans[i] = seq_id
    
    print(seq_count)
    print(*ans)