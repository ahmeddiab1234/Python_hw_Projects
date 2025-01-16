# HW - For Loop - 3 - Medium To Hard -Find all quadruples

cnt =0

for a in range(1,201):
    for b in range(1,201):
        for c in range(1,201):
            if 1 <= a+b-c <= 200 :
                cnt +=1
print(cnt) # 5333400


