#encoding:utf-8
from gconf import userfile,logfile
import json



def get_users():
	try:
		with open(userfile,'r') as f:
			users = json.loads(f.read())
			return users
	except:
		return []

def get_user(username):
	for user in get_users():
		if user['username'] == username:
			return user
	return False

def login_vilidate(name,passwd):
	if not name or not passwd:
		return False, u'用户名和密码不能为空'
	if not get_user(name):
		return False, u'用户名不存在'
	else:
		user = get_user(name)
		print user
		if user['passwd'] == passwd:
			return True, u'用户%s登录成功'%name
		else:
			return False, u'用户名或密码错误'

def signup_vilidate(name,passwd,age,job):
	if not name :
		return False, u'用户名不能为空'
	elif not passwd :
		return False, u'密码不能为空'
	elif not age :
		return False, u'年龄不能为空'
	elif not job :
		return False, u'职位不能为空'
	elif get_user(name):
		return False, u'用户名已存在'
	else:
		user = {'username':name,'passwd':passwd,'age':age,'job':job}
		users = get_users()
		users.append(user)
		if savefile(users):
			return True, u'用户%s注册成功'%name
		else:
			return False, u'用户注册失败'

def update_vilidate(name,passwd,age,job):
	users = get_users()
	user = get_user(name)
	new_user = {'username':name,'passwd':passwd,'age':age,'job':job}
	if not passwd :
		return False, u'密码不能为空'
	elif not age :
		return False, u'年龄不能为空'
	elif not job :
		return False, u'职位不能为空'
	else:
		users.remove(user)
		users.append(new_user)
		if savefile(users):
			return True, u'用户%s更新成功'%name
		else:
			return False, u'用户更新失败'

def delet_vilidate(name):
	users = get_users()
	users.remove(get_user(name))
	savefile(users)
	return True, u'%s删除成功'%name

		


def savefile(users):
	try:
		with open(userfile,'w') as f:
			f.write(json.dumps(users))
			return True
	except:
		return False
		


def loglist(n):
	logdict = {}
	loglist = []
	toplist = []
	with open(logfile,'r') as f:
		while True:
			logline = f.readline()
			if not logline:
				break
			else:
				(IP,URL,Status) = (logline.split()[0],logline.split()[6],logline.split()[8])
				logdict[(IP,URL,Status)] = logdict.get((IP,URL,Status),0)+1
		loglist = logdict.items()
		toplist = sorted(loglist, key = lambda x:x[1], reverse = True)[:n]
		return toplist













if __name__ == '__main__':
	#print get_users()
	#print get_user('nick')
	#login_vilidate('jim','12345')
	#update_vilidate('jim',123456,26,'Editor')
	#print get_user('jim')
	#print login_vilidate('jim',123456)
	#delet_vilidate('WW')
	print loglist(10)

