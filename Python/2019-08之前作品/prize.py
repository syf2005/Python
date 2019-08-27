#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#以下是编程中各个赋值的含义：
#n 参与活动总人数
#p 总奖项数量
#a,b 便于大while循环赋值
#c 便于小while循环赋值
#luck 中奖序号
#num 当前奖项中奖人数

import random

print('欢迎进入天猫精灵济宁同城抽奖程序!')

prize = ['一','二','三','四','五','六','七']
n = int(input('请输入参与活动的总人数：'))
p = int(input('请输入本次总奖项数量：'))

a = 1
b = 0

while a <= p:
	print()
	num = int(input('请输入%s等奖的中奖人数：' % prize[b]))
	c = 1
	while c <= num:
		luck = random.randint(1,n)
		print('%s等奖抽奖结果揭晓：%s' % (prize[b],luck))
		c = c + 1
	a = a + 1
	b = a - 1

print('\n备注：重复中奖则顺延给下一序号\n')
x = input('按下回车以退出：')