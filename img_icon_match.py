n = int(input())
img_pix = []
icon_pix=[]
for i in range(n):
    img_pix.append(int(input()))
m = int(input())
if m == 0:
    print(0)
elif m == 1:
    icon_pix =[int(input())]
    count = 0
    for each in img_pix:
        if each == icon_pix[0]:
            count+=1
    print(count)
elif m>1:
    for i in range(m):
        icon_pix.append(int(input()))
    count = 0
    for i in range(1,n):
        if img_pix[i]==icon_pix[1] and img_pix[i-1]==icon_pix[0]:
            count+=1
    print(count)