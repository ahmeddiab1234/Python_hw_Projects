# HW - 4 - Easy - While Loop - Special Average

num = int(input())
even_avg,odd_avg,cnt=0,0,1
while cnt <= num:
    if(cnt%2==0):
        even_n = int(input())
        even_avg+= even_n
    else:
        odd_n = int(input())
        odd_avg+= odd_n
    cnt+=1
print(odd_avg/(num/2),even_avg/(num/2))
        

