Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
phone={"darshan":9016860875,"papa":9825923092,"mom":9979205830}
phone
{'darshan': 9016860875, 'papa': 9825923092, 'mom': 9979205830}
phone["papa"]
9825923092
phone["himali"]=9998887771
phone
{'darshan': 9016860875, 'papa': 9825923092, 'mom': 9979205830, 'himali': 9998887771}
phone["himali"
      ]
9998887771
del phone["himali"
          ]
phone
{'darshan': 9016860875, 'papa': 9825923092, 'mom': 9979205830}
# how we can know if the person is there in dictionary or not
papa in phone
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    papa in phone
NameError: name 'papa' is not defined
>>> "papa" in phone
True
>>> 'himali" in phone
SyntaxError: unterminated string literal (detected at line 1)
>>> "himali" in phone
False
>>> phone.clear
<built-in method clear of dict object at 0x0000019FA9FE3280>
>>> phone
{'darshan': 9016860875, 'papa': 9825923092, 'mom': 9979205830}
>>> phone.clear()
>>> phone
{}
>>> # we can delete full dictionary with the help of cler keywprd
>>> #now lets talk about tuple
>>> #tuple having a bracetes like this ()
>>> point=(6,12)
>>> point[1]
12
>>> #here list and tuple  are different because list is mutable and tuple is inmutable . secoud reason is that list is homogeneous all the values of list having the same meaning while in tuple is hetrogeneous all the values or element of tuple having the differnt meaning.
>>> #we cannot use list if we have to represent the corrdinatnes if x axis and y axis
