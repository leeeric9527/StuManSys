#-*-encoding=utf-8-*-
file_name={
	'html/login.html':'login',
	'html/style.css':'style'
}

files={}
for key,value in file_name.items():
	with open(key,'r') as f:
		data=f.read()
		data=data.decode('utf-8').encode('utf-8')
		files[value]=data