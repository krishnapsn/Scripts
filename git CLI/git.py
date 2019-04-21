import requests
import sys
import os
os.system('clear')
URL='https://api.github.com/users/'
usern=sys.argv[1]
user=requests.get(URL+usern)
ru = requests.get(URL+usern+'/repos')
rfr = requests.get(URL+usern+'/followers')
rfl = requests.get(URL+usern+'/following')
JSON1=user.json()
repoJSON1=ru.json()
repoJSON2=rfr.json()
repoJSON3=rfl.json()
repoNames=[repoJSON1[i].get('name') for i in range(len(repoJSON1))]
repoDesc=[repoJSON1[i].get('description') for i in range(len(repoJSON1))]
repoFr=[repoJSON2[i].get('login') for i in range(len(repoJSON2))]
repoFl=[repoJSON3[i].get('login') for i in range(len(repoJSON3))]
if(JSON1.get('name')==None):
	print("REAL NAME NOT AVAILABLE\n")
else:
	print("REAL NAME :: "+JSON1.get('name')+"\n")
if(JSON1.get('location')==None):
	print("NO LOCATION\n")
else:
	print(JSON1.get('location')+"\n")
print("\t\t\tTHESE ARE THE REPOSITORIES BELONGING TO "+usern+"\n\n")
for i,j in enumerate(repoNames):
	print("\tREPO NAME:\t"+j+"\n")
	if(repoJSON1[i].get('private')):
		print("\t\tTHE REPOSITORY IS PRIVATE\n")
	if(repoDesc[i]):
		print("\t"+repoDesc[i]+"\n")
print("\t\t\t\t\t\t\tFOLLOWERS")	
for i in repoFr:
	print("\t\t"+i+"\n")
print("\t\t\t\t\t\t\tFOLLOWING")
for i in repoFr:
	print("\t\t"+i+"\n")	
