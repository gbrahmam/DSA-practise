# your code goes here                                               Approach1 = 83.3%(TLE)
# def hcf(a,b):
# 	if (a%b==0):
# 		return b
# 	else:
# 		return hcf(b,a%b)

# def lcm(a,b):
# 	HCF = hcf(a,b)
# 	return ((a*b)//HCF)

# n = int(input())
# arr = [int(bell) for bell in input().split()]
# if n==1:
# 	print(arr[0])
# else:
# 	m,p = arr[0],arr[1]
# 	LCM = lcm(m,p)
# 	for idx in range(2,n):
# 		LCM = lcm(LCM,arr[idx])
# 	print(LCM)                               


                                                                           #Approach2



def LCM(a,b):
    if a==b:
        return a
    if b==1:
        return a
    if a>b:
        a,b = b,a
    val = b
    while True:
        if val%a==0 and val%b==0:
            return val
        val+=b

tot_bells = int(input())                            #1 1
times = [int(bell) for bell in input().split()]     #1 n
res = times[0]                                      #1 1
for i in range(1,tot_bells):                        #n 1
    res = LCM(res,times[i])                         #n 1
print(res)