n = int(input())
num = [1,2,3,4,5,6,7,8,9]
ans_list = []
count = 0
for i in range(0,n):
    ans = int(input())
    ans_list.append(ans)
    for i in num:
        
        if num[i] == ans_list[i]:
            count = count + 1
print(count)