### Git global setup:    // ��Ŀ������

git config --global user.name "Administrator"
git config --global user.email "admin@local.host"

####Create Repository     //   ������Ŀ

mkdir gitlab-tutorials
cd gitlab-tutorials
git init
touch README
git add README
git commit -m 'first commit'
git remote add origin 'http://192.168.1.1/huohang/iot2015proj.git
git push -u origin master

### Existing Git Repo?     // �������е���Ŀ

cd existing_git_repo
git remote add origin 'http://192.168.1.1/huohang/iot2015proj.git
git push -u origin master


#####����Э��
��������Ŀ�Ľ�����Ȼ��������Ŀ�Ķ���Э��

��¡����Ŀ��

developer���Դ�����֧
  $ git checkout -b dev
    Switched to a new branch 'dev'
    git checkout�������-b������ʾ�������л����൱�������������
    
    $ git branch dev
    $ git checkout dev
    Switched to branch 'dev
  
Ȼ����git branch����鿴��ǰ��֧��
  $ git branch
      * dev
      master
      
git branch������г����з�֧����ǰ��֧ǰ����һ��*�š�

 Ȼ�����ǾͿ�����dev��֧�������ύ�������readme.txt�����޸ģ�����һ�У�

    Creating a new branch is quick.

Ȼ���ύ��

    $ git add readme.txt
    $ git commit -m "branch test"
    [dev fec145a] branch test
    1 file changed, 1 insertion(+)

���ڣ�dev��֧�Ĺ�����ɣ����ǾͿ����л���master��֧��

    $ git checkout master
    Switched to branch 'master'

�л���master��֧���ٲ鿴һ��readme.txt�ļ����ղ���ӵ����ݲ����ˣ���Ϊ�Ǹ��ύ����dev��֧�ϣ���master��֧�˿̵��ύ�㲢û�б䣺

co-master
���ڣ����ǰ�dev��֧�Ĺ����ɹ��ϲ���master��֧�ϣ�

    $ git merge dev
    Updating d17efd8..fec145a
    Fast-forward
    readme.txt | 1 +
    1 file changed, 1 insertion(+)

git merge�������ںϲ�ָ����֧����ǰ��֧���ϲ����ٲ鿴readme.txt�����ݣ��Ϳ��Կ�������dev��֧�������ύ����ȫһ���ġ�

ע�⵽�����Fast-forward��Ϣ��Git�������ǣ���κϲ��ǡ����ģʽ����Ҳ����ֱ�Ӱ�masterָ��dev�ĵ�ǰ�ύ�����Ժϲ��ٶȷǳ��졣

��Ȼ��Ҳ����ÿ�κϲ�����Fast-forward�����Ǻ���Ὣ������ʽ�ĺϲ���

�ϲ���ɺ󣬾Ϳ��Է��ĵ�ɾ��dev��֧�ˣ�

    $ git branch -d dev
    Deleted branch dev (was fec145a).

ɾ���󣬲鿴branch����ֻʣ��master��֧�ˣ�

    $ git branch
    * master

��Ϊ�������ϲ���ɾ����֧�ǳ��죬����Git������ʹ�÷�֧���ĳ�����񣬺ϲ�����ɾ����֧�����ֱ����master��֧�Ϲ���Ч����һ���ģ�
�����̸���ȫ��

С��
Git��������ʹ�÷�֧��
�鿴��֧��git branch
������֧��git branch name
�л���֧��git checkout name
����+�л���֧��git checkout -b name
�ϲ�ĳ��֧����ǰ��֧��git merge name
ɾ����֧��git branch -d name  


��󣺣�������
 ˳���г��������Ŀ¼֧�����⣺

1��ls������ʾ����Ŀ¼

����취����git/etc/git-completion.bash������һ�У�

  alias ls='ls --show-control-chars --color=auto'

2��git commit�����ύ����ע��

����취���޸�git/etc/inputrc�ж�Ӧ���У�

  set output-meta on
  set convert-meta off 

3��git log�޷���ʾ����ע��

����취����git/etc/profile������һ�У�

  export LESSCHARSET=iso8859



$ git config http.postBuffer 52428800 

ԭ��Ĭ�� Git ���� http post �Ļ���Ϊ 1MB���������뽫������Ϊ 50MB~