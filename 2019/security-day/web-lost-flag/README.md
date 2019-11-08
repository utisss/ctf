# Lost Flag
* **Event:** Security Day CTF
* **Problem Type:** Web

## Background
git is a popular version control system that lets you collaborate with others on code, and log and view the history of your code.

## Steps
One mistake that's done fairly frequently is serving the .git folder on a public site. The .git folder is used by git to keep track of changes. By navigating to /lost_flag/.git we can see that the .git folder is publicly viewable. 

We can use wget to download the entire .git folder recursively:
```
wget isss.ga/lost_flag/index.html
wget -r isss.ga/lost_flag/.git
```

Then navigate into the folder which we just downloaded, and use git commands to view the history:
```
git log
git checkout HEAD~
cat index.html
```