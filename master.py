import os

while True:
    os.system("cd ../covid19/ ; python covid19.py ; cd ../qjhong.github.io ")
    os.system("cp ../covid19/DailyNewCases.png .")
    os.system("sed '/Last/d' index.html > tmp; mv tmp index.html")
    os.system("echo Last updated: >> index.html")
    os.system("date >> index.html")
    os.system("git add DailyNewCases.png index.html")
    os.system("git commit -m 'update'")
    os.system("git push -u origin master")
    os.system("sleep 3600")
