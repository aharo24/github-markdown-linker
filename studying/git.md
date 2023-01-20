
## [Git Tutorial Link](https://www.youtube.com/watch?v=tRZGeaHPoaw&ab_channel=KevinStratvert)

# Overview

![](aharo24%202023-01-14%20at%207.09.20%20PM.png)




## config help

```git
git config -h
```





# Tracking
### git status tracking

![](aharo24%202023-01-14%20at%206.21.12%20PM.png)



## rm

![](aharo24%202023-01-14%20at%206.22.28%20PM.png)



![](aharo24%202023-01-14%20at%206.25.45%20PM.png)


## add

both will add everything in `pwd`
``` git 
git add --all   

git add .
```


## diff

shows the difference between old and new modification of files/dir.
 ``` git
git diff   
```



---
---




# Commit

its taking a snapchat of the current workflow.
That also implies we can go back and forth between commits.





## restore

![](aharo24%202023-01-14%20at%207.04.21%20PM.png)



normally after a commit
![](aharo24%202023-01-14%20at%207.09.20%20PM%201.png)



# log


view detailed logs 
``` git
git log -p 
```



.
.
.
.
# rebase
 ``` git
git rebase -i --root  
```


.
.
.
.
# branch

## creating
``` git 
git branch (name)
```
![](aharo24%202023-01-14%20at%209.08.20%20PM.png)

### faster way 
``` git
git switch -c (branch_name)
```  
![](aharo24%202023-01-14%20at%209.27.37%20PM.png)
.
.
### most people do it this way
#important/git/checkout
```python3
git checkout -b (branch_name)
```

whatever branch you are in, it will clone it
.
.
## merge
![](aharo24%202023-01-14%20at%209.21.43%20PM.png)
.
.
![](aharo24%202023-01-14%20at%209.23.03%20PM.png)
.
.
## delete
![](aharo24%202023-01-14%20at%209.25.10%20PM.png)


.
.
.
.
# Pushing

![](aharo24%202023-01-14%20at%2010.22.10%20PM.png)

![](aharo24%202023-01-14%20at%2010.23.44%20PM.png)


when pushing to 

		git push (remote) (branch)

git default 
		git push origin main



```git
git push --all origin
```

or 

```git
git push origin [branch_name]
```
^^^recommended 

ie...
![](aharo24%202023-01-17%20at%2010.28.23%20PM.png)




.
.
.
.
# Pull Request

# [Source This video for Request stuff](https://www.youtube.com/watch?v=rgbCcBNZcdQ&ab_channel=JakeVanderplas)
![](aharo24%202023-01-14%20at%2010.55.44%20PM.png)









# GPT
![](aharo24%202023-01-14%20at%209.13.16%20PM.png)


![](aharo24%202023-01-14%20at%2010.39.35%20PM.png)









## revert
choose the snapchat you want to revert into 

check -> [Commit](#Commit)
![](aharo24%202023-01-16%20at%2010.43.41%20PM.png)







# Attempt to restructure OpenSource 

setting up branches for environmental set up
![](aharo24%202023-01-17%20at%2010.10.54%20PM.png)






## fetch

### branch up to date?

	do `git fetch`
![](aharo24%202023-01-17%20at%2010.21.19%20PM.png)

if nothing returns we are up to date 










# Origin (more than One branch)

## delete

``` git
git push origin --delete [branch-name]
```

ie...
![](aharo24%202023-01-17%20at%2010.52.30%20PM.png)


## pull

pulling from a specific branch 
 ``` git
git pull origin [branch] 
```






![](aharo24%202023-01-17%20at%2011.43.40%20PM.png)






## branch info

```python 
git branch -v 
```

```python 
git branch -a 
```


ie...

![](aharo24%202023-01-17%20at%2011.58.03%20PM.png)



## revert a pull

#git/revert
if you pulled a origin by acident just follow it up with a rever
```git
 git revert 
```



## abbort

``` git
git merge --abort
```

``` git
git rebase --abbort
```

## cherry-picking 

![](aharo24%202023-01-18%20at%2012.29.28%20AM.png)




---
---
.
.
.
# gitignore



### creating

vim/nvim/emacs

``` vim
vim .ignore
```

mac 
``` macOS
touch .ignore
```


`*`

```git
# ignore all txt filex

*.txt
```



### config
```.gitignore
tools/

linkFixer.py

dev/

image_fixer.py

link_fixer.py

z.py

test.py

tester.py

  

# Ignore the ".obsidian" folder

/.obsidian

  

# Ignore .DS_Store files (macOs)

.DS_Store

  

# ignore obsidian ".trash" directory

/.trash
```


