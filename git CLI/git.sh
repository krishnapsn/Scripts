#!/usr/bin/bash
clear && cat 2.txt

read usern

python git.py $usern

if [ $? -ne 0 ] 
then
	echo "ERROR"
else
	setopt shwordsplit
	for i in $(python git2.py $usern) 
	do
		echo "id :: $i"
		curl -o $i.jpg https://avatars0.githubusercontent.com/u/"$i"
	done
	echo "RANDOM DAD JOKE FOR YOU XD"
	curl -H "Accept: text/plain" https://icanhazdadjoke.com/
	echo "\n"
	cat 1.txt
	read repo

	echo "ENTER DIRECTORY TO CLONE INTO"
	tree -d ~ -L 1
	read dir
	cd $dir
	git clone https://github.com/$usern/$repo.git
	if  [ $? -ne 0 ] 
	then
	    echo "ERROR"
	else
		echo "Cloned"
	fi
fi
