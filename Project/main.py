# import ortools
# from ortools.graph import pywrapgraph
import xlrd
import xlwt

# between each pair. For instance, the arc from node 0 to node 1 has acapacity of 15 and a unit cost of 4.

a = []
# 表示每一笔交易的交易量
b = []
# 表示每一笔交易的费用
c = []
# 表示每一个平台的最大交易量

m = 10
n = 50

test = xlrd.open_workbook('test1.xls');
sheet1_content1 = test.sheet_by_index(0);

for i in range(1, n + 1):
    a.append(sheet1_content1.cell(i, 1).value)
for i in range(1, n + 1):
    b.append(sheet1_content1.cell(i, 2).value)

print(a)
print(b)

c.append(100)
c.append(200)
c.append(300)
c.append(400)
c.append(500)
c.append(500)
c.append(600)
c.append(700)
c.append(800)
c.append(900)

left = 0
for x in b:
    left += x
print(left)
right = left * 10
mid = 0
money = 0
for i in range(0, 40):
    mid = (left + right) / 2
    mid = int(mid)
    print("left  ", end='')
    print(left)
    print("right  ", end='')
    print(right)
    print("mid  ", end='')
    print(mid)
    if left>right:
        print("运行结束！");
        break
    money = mid
    a=[]
    b=[]
    c=[]
    for j in range(1, n + 1):
        a.append(sheet1_content1.cell(j, 1).value)
    for j in range(1, n + 1):
        b.append(sheet1_content1.cell(j, 2).value)
    c.append(100)
    c.append(200)
    c.append(300)
    c.append(400)
    c.append(500)
    c.append(500)
    c.append(600)
    c.append(700)
    c.append(800)
    c.append(900)
    for j in range(0, n):
        for k in range(0, m):
            sorted(c)
            flag = 1
            if a[j] < c[k]:
                money -= b[j]
                c[k] -= a[j]
                a[j] = 0
                flag = 0
                break
            if a[j]>c[m-1]:
                money -= b[j]
                a[j] -= c[m - 1]
                c[m - 1] = 0
                j -= 1
                break
        moneySum = 0
        for k in range(0, n):
            if a[k] > 0:
                moneySum += b[k]
        if moneySum > money:
            left = mid + 1
            left = int(left)
            break
    if money > 0:
        right = mid - 1
        right = int(right)