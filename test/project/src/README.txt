### Git global setup:    // 项目所有人

git config --global user.name "Administrator"
git config --global user.email "admin@local.host"

####Create Repository     //   创建项目

mkdir gitlab-tutorials
cd gitlab-tutorials
git init
touch README
git add README
git commit -m 'first commit'
git remote add origin 'http://192.168.1.1/huohang/iot2015proj.git
git push -u origin master

### Existing Git Repo?     // 导入已有的项目

cd existing_git_repo
git remote add origin 'http://192.168.1.1/huohang/iot2015proj.git
git push -u origin master


#####多人协作
上面是项目的建立，然后是是项目的多人协作

克隆晚项目后

developer可以创建分支
  $ git checkout -b dev
    Switched to a new branch 'dev'
    git checkout命令加上-b参数表示创建并切换，相当于以下两条命令：
    
    $ git branch dev
    $ git checkout dev
    Switched to branch 'dev
  
然后，用git branch命令查看当前分支：
  $ git branch
      * dev
      master
      
git branch命令会列出所有分支，当前分支前面会标一个*号。

 然后，我们就可以在dev分支上正常提交，比如对readme.txt做个修改，加上一行：

    Creating a new branch is quick.

然后提交：

    $ git add readme.txt
    $ git commit -m "branch test"
    [dev fec145a] branch test
    1 file changed, 1 insertion(+)

现在，dev分支的工作完成，我们就可以切换回master分支：

    $ git checkout master
    Switched to branch 'master'

切换回master分支后，再查看一个readme.txt文件，刚才添加的内容不见了！因为那个提交是在dev分支上，而master分支此刻的提交点并没有变：

co-master
现在，我们把dev分支的工作成果合并到master分支上：

    $ git merge dev
    Updating d17efd8..fec145a
    Fast-forward
    readme.txt | 1 +
    1 file changed, 1 insertion(+)

git merge命令用于合并指定分支到当前分支。合并后，再查看readme.txt的内容，就可以看到，和dev分支的最新提交是完全一样的。

注意到上面的Fast-forward信息，Git告诉我们，这次合并是“快进模式”，也就是直接把master指向dev的当前提交，所以合并速度非常快。

当然，也不是每次合并都能Fast-forward，我们后面会将其他方式的合并。

合并完成后，就可以放心地删除dev分支了：

    $ git branch -d dev
    Deleted branch dev (was fec145a).

删除后，查看branch，就只剩下master分支了：

    $ git branch
    * master

因为创建、合并和删除分支非常快，所以Git鼓励你使用分支完成某个任务，合并后再删掉分支，这和直接在master分支上工作效果是一样的，
但过程更安全。

小结
Git鼓励大量使用分支：
查看分支：git branch
创建分支：git branch name
切换分支：git checkout name
创建+切换分支：git checkout -b name
合并某分支到当前分支：git merge name
删除分支：git branch -d name  


最后：：：：：
 顺便列出解决中文目录支持问题：

1、ls不能显示中文目录

解决办法：在git/etc/git-completion.bash中增加一行：

  alias ls='ls --show-control-chars --color=auto'

2、git commit不能提交中文注释

解决办法：修改git/etc/inputrc中对应的行：

  set output-meta on
  set convert-meta off 

3、git log无法显示中文注释

解决办法：在git/etc/profile中增加一行：

  export LESSCHARSET=iso8859



$ git config http.postBuffer 52428800 

原因：默认 Git 设置 http post 的缓存为 1MB，上述代码将其设置为 50MB~