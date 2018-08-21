#Q.1-REVERSE THE LIST.
list_1=[1,2,3,4,5,6,7]
list_1.reverse()
print(list_1)

#Q.2-EXTRACT ALL THE UPPERCASE LETTERS FROM STRING.
a=input("enter string")
b=" "
for i in a:
    if i.isupper():
        b=b+i+','
print(b)

#Q.3-SPLIT AND STORETHE VALUES AFTER TYPECASTING.
s=[]
p=[]
d=input()
s=d.split(',')
for i in range (len(s)):
    p.append(int(s[i]))
print(type(p[0]))
print(p)

#Q.4-CHECK FOR PALLINDROME.
number=(input('enter a number'))
rev=number
rem=number[::-1]
if(rev==rem):
    print(" it is a pallindrome")
else:
    print("it is not a pallindrome")
#Q.5-UNDERSTAND DEEP AND SHALLOW COPY.

#shallow copy
import copy as c
lst_1=[1,2,[3,4],5]
lst_2=c.copy(lst_1)
lst_1[2][0]='gogluu'
print(lst_1)
print(lst_2)

#deep copy
import copy as a
lst_1=[1,2,[3,4],5]
lst_2=a.deepcopy(lst_1)
lst_1[2][1]='gogluu'
print(lst_1)
print(lst_2)


