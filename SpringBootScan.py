#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Author：BetterDefender
Version：1.0.1
'''

import requests


##为url传递参数
#url_params = {'q':'python'}    #字典传递参数，如果值为None的键不会被添加到URL中
#r = requests.get('https://www.baidu.com',params=url_params)
#r.encoding = 'utf-8'
#print(r.url)
#print(r.text)
print('测试中，请耐心等待...\n')
report = open('report.txt','w')
#通过for循环拼接拿到所有请求url
for line1 in open('url.txt'):
    for line2 in open('path.txt'):
        #print(line1.replace('\n','')+line2,end='')
        url = line1.replace('\n','')+line2.replace('\n','')
        r = requests.get(url)
        if "swagger" in r.url and r.status_code==200:
            #print(url,'存在springboot信息泄漏')
            #report.write(url+'\n')
            if "select_baseUrl" in r.text:
                print(url,'疑似存在springboot信息泄漏，请自行确认')
                report.write(url+'\n')
        elif "OSS" in r.text:
                print(url,'疑似存在阿里云OSS密钥信息泄漏，请自行确认')
                report.write(url+'\n')
print('\n测试结束，请查看report.txt文本')