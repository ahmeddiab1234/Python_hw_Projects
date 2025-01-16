# HW - For Loop - 2 - Medium To Hard - Find Special Pairs

cnt = 0
for x in range(50,301):
    for y in range(70,401):
        if x<y:
            if (x+y)%7==0:
                cnt+=1
print(cnt) # 8040


###############################################333

cnt =0
for x in range(50,301):
    max_y = max(70,1+x)
    for y in range(max_y,401):
        if (x+y)%7==0:
            cnt+=1
print(cnt)




