class InputError(Exception):pass
import requests as r
from bs4 import BeautifulSoup as bs
id_n=input("enter the id no:")
if len(id_n)>10:raise InputError("Please enter  valid credentials!!!")
sem=input("enter sem:")
dat={'__EVENTVALIDATION': '/wEWFQKj/sbfBgLnsLO+DQLIk+gdAsmT6B0CypPoHQLLk+gdAsyT6B0CzZPoHQLOk+gdAt+T6B0C0JPoHQLIk6geAsiTpB4CyJOgHgLIk5weAsiTmB4CyJOUHgKL+46CBgKM54rGBgK7q7GGCALWlM+bAsr6TbZa4e1ProM8biQQXbC9/wS2', 'txtreg':id_n, '__VIEWSTATEGENERATOR': '65B05190', '__VIEWSTATE': '/wEPDwULLTE3MTAzMDk3NzUPZBYCAgMPZBYCAgcPDxYCHgRUZXh0ZWRkZKKjA/8YeuWfLRpWAZ2J1Qp0eXCJ', 'Button1': 'Get Result',"cbosem":sem}
t=r.post("https://doeresults.gitam.edu/onlineresults/pages/Newgrdcrdinput1.aspx",data=dat)
s=bs(t.text,"html.parser")
try:
	r=s.findAll("span")
	res=[]
	for i in r:
		if i["id"]=="Label11":
			i["id"]="Exam"
			res.append(i["id"])
		elif i["id"].startswith("lbl"):
			res.append(i["id"].replace("lbl",""))
	r=[p.text for p in r]
	q=list(zip(res,r))
	for (i,j) in q:
		print("%s:\t%s"%(i,j))
except:InputError("entered invalid credentials!!!!")


