# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = str(input())
for i in range(len(n)):
	if n[-i-1] == '0':
		continue
	else:
		print(int(n[-i-1]),end='')