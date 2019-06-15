from django.shortcuts import render
import csv
import os
# Create your views here.

def data_first(request):
	dic={}
	if request.method=='POST':
		data=request.POST
		dic['name']=data['name']
		dic['empid']=data['empid']
		
		
		info=request.POST
		if not os.path.isfile("Employee_info.csv"): isNew=True
		with open("Employee_info.csv",'a') as ecsv:
			fieldnames=('name','empid')
			writer=csv.DictWriter(ecsv,fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow(dic)
		return render(request,'main.html')
	else:
		return render(request,'main.html')
def second(request):
	dic={}
	with open("Employee_info.csv",'r') as escv:
		reader=csv.reader(escv)
		for line in reader:
			if line==[]:
				continue
			else:
				dic[line[0]]=line[1]
	return render(request,'second.html',{'details':dic})

