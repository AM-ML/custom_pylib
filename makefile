default:
	clear;python file.py
f:
	clear;python ${a}.py

mv:
	clear;mkdir ${a};mv *.py ${a};cp ${a}/lib.py .;cp makefile ${a};mv *.csv ${a};
	touch file.py data.csv; mv ${a} rsc;clear;ls rsc;ls rsc/${a}

git:
	git add --all; git commit -am "${a}" ; git push;git log --oneline;git status;echo '/033[1;92mTASK FINISHED!'
