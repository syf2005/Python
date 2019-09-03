#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello, please write down your name now, thanks!')

name = input()

print('Hello,',name,'!','Now, please tell me your age, thanks.')

age = int(input())
if age >= 18:
  print('You are an adult.')

elif age >=12:
  print('You are a teenager.')

else:
  print('Hey, little kid! Do not play the computer!')

print('''This is my first program which is made by myself.
Made on January 24, 2019, 
To commemorate. ''')

print(  )

x = input('按下回车以退出')