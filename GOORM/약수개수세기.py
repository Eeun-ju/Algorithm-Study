# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
count = 0
for i in range(1,n+1):
	if n%i == 0:
		count +=1

if count%2 == 0:
	print('no')
else:
	print('yes')
#print ("Hello Goorm! Your input is " + user_input)