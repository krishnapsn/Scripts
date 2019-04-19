import requests
import sys
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
print("REAL NAME :: "+JSON1.get('name'))
if(JSON1.get('location')==None):
	print("NO LOCATION")
else:
	print(JSON1.get('location'))
print("\t\t\tTHESE ARE THE REPOSITORIES BELONGING TO "+usern)
for i,j in enumerate(repoNames):
	print("\t\t"+j+"\n")
	if(repoJSON1[i].get('private')):
		print("\t\tTHE REPOSITORY IS PRIVATE\n")
	if(repoDesc[i]):
		print(repoDesc[i]+"\n")
print("\t\t\t\t\t\t\tFOLLOWERS")	
for i in repoFr:
	print("\t\t"+i+"\n")
print("\t\t\t\t\t\t\tFOLLOWING")
for i in repoFr:
	print("\t\t"+i+"\n")	
