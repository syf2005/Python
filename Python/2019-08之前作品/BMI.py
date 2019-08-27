#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('''你好，欢迎使用BMI简易计算程序！
现在，请输入你的名字，然后按下回车，谢谢！''')

name = input()

print('你好,',name,'!','现在已经进入BMI计算流程！')

print('请留意，下列操作中请注意单位，输入阿拉伯数字，否则会计算失败，谢谢！')

a = input('1.请输入你的身高（米）：')

b = input('2.请输入你的体重（千克）：')

a1 = float(a)

b1 = float(b)

c1 = b1/(a1*a1)

print(  )

print('结果揭晓，',name,'，您的BMI指数为：',c1)

print(  )

print('下面是您的BMI指数分析')

c = float(c1)

if c > 32:
  	print('您的BMI指数已经超过了32，属于非常肥胖人群，身体因超重会面临心脏病、高血压等风险，请注意控制饮食，保持健康！')

elif c > 28:
  	print('您的BMI指数超过了28，属于肥胖人群，请注意保持健康！')

elif c > 24:
	print('您的BMI指数超过了24，比正常标准稍高，请多加锻炼哦！')

elif c > 18.5:
	print('您的体重在正常范围（18.5-24.9）内，非常好！注意保持呦！')

else:
    print('Hey,',name,'！你的BMI指数小于18.5，太瘦了，多吃点吧！')

print(  )

print('''Tips:本分析采取国际BMI标准计算，不同地区会有所差异
Tips:BMI标准范围为18.5-24.9，最理想BMI指数为22''')

print(  )

print(name,'，祝您生活愉快，身体健康哦！')

print(  )

print('''程序作者：苏耀峰，制作于2019年1月24日，最后更新于2019年1月24日 
持续更新，感谢使用! ''')

print(  )

x = input('按下回车以退出')