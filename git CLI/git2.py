import requests
import sys
import os
URL='https://api.github.com/users/'
s=[]
usern=sys.argv[1]
user=requests.get(URL+usern)
JSON1=user.json()
s.append(str(JSON1.get('id')))
rfr = requests.get(URL+usern+'/followers')
repoJSON2=rfr.json()
repoFr=[repoJSON2[i].get('id') for i in range(len(repoJSON2))]
for id in repoFr:
	s.append(str(id))
s=" ".join(s)
print(s)

