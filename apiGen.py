# -*- coding: utf-8 -*-
import os
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def apisplit(inpu):
	apistr=inpu
	apitemp=[]
	apilist=[]
	j=0
	if  apistr[0]!='(' and apistr[0]!=')':
		apitemp.append(apistr[0])
	for i in range(1,len(apistr)):
		if apistr[i]!='&' and apistr[i]!='|'and apistr[i]!='(' and apistr[i]!=')':
			apitemp.append(apistr[i])
		elif apistr[i-1]!='&' and apistr[i-1]!='|' and apistr[i-1]!='(' and apistr[i-1]!=')':
			apilist.append(''.join(apitemp))
			#apistr.replace(str(apilist[-1]),str(j))
			#j=j+1
			apitemp=[]
	if len(apitemp)>0:		
		apilist.append(''.join(apitemp))
	#print apistr
	for i in apilist:
		#print (str(i)==apistr[apistr.find(i):apistr.find(i)+len(i)])
		#a=list(i)
		apistr=apistr.replace(i,str(j),1)
		j=j+1
	return apilist,apistr


dict={}
data=xlrd.open_workbook('apilist.xlsx')
table = data.sheet_by_name(u'Sheet2')
output = open ('zhiboapp.ldb','w+')
for i in range(table.nrows):
	#dict[table.cell(i,0).value]=table.cell(i,1).value
	apilist=[]
	apilist,string=apisplit(table.cell(i,1).value)
	output.write(str(table.cell(i,0).value)+';'+'Target:0;'+string)
	for i in apilist:
		output.write(';'+str(i.encode('hex'))+'::i')
	#output.write(table.cell(i,1).value.encode('hex')+"::i")
	output.write("\n")
output.close()
