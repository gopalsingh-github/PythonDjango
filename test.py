import numpy as np
import pandas as pd
# pd = np.array([[[1,2,3,4],[5,6,7,8], [10,11,12,13]]])
# print(pd)
# print(pd.ndim)
# print(pd.size)
# print(pd.shape)
# print(pd.dtype)

# pd = np.ones(5)
# print(pd)
# pd = np.ones((3,4), dtype=int)
# print(pd)

# pd = np.zeros((3,4), dtype=int)
# print(pd)


# arange

# arr = np.arange(1,13)
# print(arr)
# print(arr.reshape(3,4))

# arr = np.arange(1,13)
# # print(arr)
# arr1 = arr.reshape(2,3,2)
# # print(arr1)
#
# reval = arr1.ravel()
# print(arr.transpose())


# arr1 = np.arange(1,10).reshape(3,3)
# arr2 = np.arange(1,10).reshape(3,3)
# print(arr1)
# print(arr2)
# arr = arr1+arr2
# print(arr1.max(axis=1))

#pandas
# ser = pd.Series([1,2,3,4, np.nan,6,7])
# df = pd.DataFrame(np.random.randn(6,4), columns=list('ABCD'))
# print(df)



student = {"Name":['Gopal', 'priyanka', 'Jitendra', "Rohit"], "LastName":['Singh', 'Singh', "verma", "Sharma"],
           "marks":[120,100,80,90]}
df = pd.DataFrame(student)
# print(df)
# print(df.index)
# print(df.T)
# print(df)

# print(df[['marks', 'LastName']])
# print(df[['marks']])
# print(df[1:4])
# print(df.loc[0:2, ['marks','Name']])
# print(df[df['marks']>=100])
# print(df.set_index('Name', inplace=True))
# print(df.reset_index(inplace=True))
# df1 =df.loc[2, 'Name']=['Jitendra' ]
# print(df1)
# print(df.append({'Name':'Raj', "LastName":'Sharma', 'marks':98}, ignore_index=True, ))
# print(df.drop(columns='LastName'))

# df1 = df.to_csv('test')
# print(pd.read_csv('test'))

# df = pd.read_csv('F:\\Book1.csv')
# df = pd.DataFrame(df)
# print(df)


# for i in range(0,6):
#     for k in range(0, 6 - i):
#         print(" ", end="")
#     for j in (0, (2*i-1)):
#         print("*" * j, end="")
#     print('\n')


# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# 
# t = fact(6)
# print(t)

#pickle and unpickle

# import pickle
#
# class Student:
#     def __init__(self, name, roll, address):
#         self.name = name
#         self.roll = roll
#         self.address = address
#     def display(self):
#         print('name', self.name)
#         print('roll', self.roll)
#         print('address', self.address)
#
# n = int(input('Enter a value:'))
# with open('student.dat', 'wb') as f:
#     for i in range(0,n):
#         name = input('Enter the Name:')
#         roll = input('Enter the Roll:')
#         address = input('Enter the address:')
#         obj = Student(name, roll, address)
#         pickle.dump(obj, f)
#
# with open('student.dat', 'rb') as f:
#     while True:
#         try:
#             obj = pickle.load(f)
#             data = obj.display()
#         except Exception as e:
#             print('done')
#             break


#generator
# def show(a, b):
#     while a<=b:
#         yield a
#         a+=1
# result = show(1,5)
# print(result)
# print(next(result))
# # print(next(result))
# print(list(result))

# tup = (x*x for x in range(1,20))
# for index, i in enumerate(tup):
#         if index ==5:
#             break
#         else:
#             print(next(tup))

# tup = (x*x for x in range(1,20))
# while tup:
#     try:
#         print(next(tup))
#     except Exception as e:
#         print('done iterator')
#         break

# def func(func):
#     def inner(*args, **kwargs):
#         result1 = func(*args, **kwargs)
#         return result1
#
#     return inner
#
# @func
# def main(a, b):
#     return a+b
# result = main(5,10)
# print(result)
#
# def test(a, b):
#     return a-b
# result = test(5,10)
# print(result)

# list_1 = [4,6,2,8,3,5,4,2,9,1,10,3]
# list_2 = [*set(list_1)]
# print(list_2)
#
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def __init__(self, name, count):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.count = count
#         print('This is init method called')
#
#     def run(self):
#         print("Start threading", self.name)
#         i = 0
#         while i < self.count:
#             display(self.name, i)
#             time.sleep(3)
#             i += 1
#
# def display(threaname, i):
#     print("Thread_name", threaname, " ", i)
#
# thread1 = MyThread('One', 5)
# thread12 = MyThread('Two',6)
# thread1.start()
# thread12.start()
# thread1.join()
# thread12.join()
# print('exist thread')






