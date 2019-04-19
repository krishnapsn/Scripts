cls && cat 2.txt
read usern
if (python git.py $usern) then
	cat 1.txt
	read repo
	if ! (git clone https://github.com/$usern/$repo.git) then
		echo "FAIL"
	else
	    echo "REPO CLONED"
	fi
else
	echo "ERROR"
fi
