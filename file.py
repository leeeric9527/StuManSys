#-*-encoding=utf-8-*-
file_name={
	'html/login.html':'login',
	'html/style.css':'style',
	'html/user_not_exist.html':'user_not_exist',
	'html/password_incorrect.html':'password_incorrect',
	'html/verification_success.html':'verification_success',
	'html/student.html':'student',
	'html/abandoned.html':'abandoned'
}

files={}
for key,value in file_name.items():
	#with open(key,'r') as f:
	with open(key,'r',encoding='utf-8') as f:
		data=f.read()
		#data=data.decode('utf-8').encode('utf-8')
		files[value]=data