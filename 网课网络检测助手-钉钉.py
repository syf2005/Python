# -*- coding: utf-8 -*-
 
import subprocess
import re

def get_ping_result(ip_address):
    p = subprocess.Popen(["ping.exe", ip_address], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    out = p.stdout.read().decode('gbk')
    
    reg_receive = '已接收 = \d'
    match_receive = re.search(reg_receive, out)
    
    receive_count = -1
    
    if match_receive:
        receive_count = int(match_receive.group()[6:])
    
    if receive_count > 0:    #接受到的反馈大于0，表示网络通
        reg_min_time = '最短 = \d+ms'
        reg_max_time = '最长 = \d+ms'
        reg_avg_time = '平均 = \d+ms'
        
        match_min_time = re.search(reg_min_time, out)
        min_time = int(match_min_time.group()[5:-2])
        
        match_max_time = re.search(reg_max_time, out)
        max_time = int(match_max_time.group()[5:-2])
        
        match_avg_time = re.search(reg_avg_time, out)
        avg_time = int(match_avg_time.group()[5:-2])
        if avg_time < 50 and max_time <100:
            return [receive_count, min_time, max_time, avg_time,'你的网络良好，卡顿的话是老师的原因']
        else:
            return [receive_count, min_time, max_time, avg_time,'你的网络延迟过大，赶快处理，认真上课']

    else:
        return ['你的网络彻底出问题啦，赶快处理，认真上课']
        
print('“究竟是谁出了问题”网课网络检测程序（钉钉版）已启动！')
print('程序作者Yaofeng，个人网站:www.syf.ink')
if __name__ == '__main__':
    while(True):
        ping_result = get_ping_result('dingtalk.com')
        print(ping_result)