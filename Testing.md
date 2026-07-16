testing/test1/deploy.sh                  777                   WW                            Typ A
testing/test1/test11.sh                     600                   ZN                              ZN
testing/test1/test12.sh                    604                   ZN                              ZN
testing/test1/test13.sh                    004                   ZN                              ZN
testing/test2/test21.sh                   700                   ZN                              ZN
testing/test2/test22.sh                  744                   ZN                              ZN
testing/test2/test23.sh                  444                   ZN                              ZN
testing/test2/test24.sh                  521                    ZN                              ZN
testing/test3/test31.sh                   377                   WW                            Typ A
testing/test3/test32.sh                  601                    ZN                              ZN
testing/test3/test33.sh                  711                     ZN                              ZN
testing/test3/test34.sh                  222                  WW                            Typ A
testing/test4/test41.sh                   555                  ZN                               ZN
testing/test4/test42.sh                  576                  WW                            Typ A
testing/test4/test43.sh                  676                  WW                            Typ A
testing/test4/test44.sh                  707                  WW                            Typ A
testing/.ssh/id_test                        644                 UK                              Typ B
testing/.ssh/id_test2                      600                 ZN                              ZN
testing/.ssh/id_test3                      466                 UK + WW                  Typ B + Typ A
testing/.ssh/id_test4                      640                 ZN                              ZN
testing/.ssh/id_test5                      604                 ZN                              ZN
testing/cisty                                      466                 WW                           Typ A
testing/not_allowed                       000                 skipped                   missing permission



1. lenovo@LAPTOP-QAGBIF50:~/file-permission-auditor$ pwd
/home/lenovo/file-permission-auditor
lenovo@LAPTOP-QAGBIF50:~/file-permission-auditor$ git remote -v
origin  git@github.com:RadiiYevstratov/file-permission-auditor.git (fetch)
origin  git@github.com:RadiiYevstratov/file-permission-auditor.git (push)

2. Bol to omyl. 
lenovo@LAPTOP-QAGBIF50:~/file-permission-auditor$ ls -la ~/file-permission-auditor
total 20
drwxr-xr-x  3 lenovo lenovo 4096 Jul 16 23:12 .
drwxr-x--- 14 lenovo lenovo 4096 Jul 16 23:16 ..
drwxr-xr-x  7 lenovo lenovo 4096 Jul 16 23:10 .git
-rw-r--r--  1 lenovo lenovo   26 Jul 16 18:30 README.md
-rw-r--r--  1 lenovo lenovo 1818 Jul 16 23:10 Testing.md
-rw-r--r--  1 lenovo lenovo    0 Jul 16 23:10 main.py

4. V zadani je jasne napisane. Pod nalez typu a spada hociaky subor pri kotorom pravo w maju ostatni.
lenovo@LAPTOP-QAGBIF50:~$ ls -lRa testing/
testing/:
total 32
drwxr-xr-x  8 lenovo lenovo 4096 Jul 16 23:26 .
drwxr-x--- 14 lenovo lenovo 4096 Jul 16 23:16 ..
drwxr-xr-x  2 lenovo lenovo 4096 Jul 16 23:22 .ssh
-r--rw-rw-  1 lenovo lenovo    0 Jul 16 19:27 cisty
d---------  2 lenovo lenovo 4096 Jul 16 23:26 not_allowed
drwxr-xr-x  2 lenovo lenovo 4096 Jul 16 19:03 test1
drwxr-xr-x  2 lenovo lenovo 4096 Jul 16 19:05 test2
drwxr-xr-x  2 lenovo lenovo 4096 Jul 16 19:07 test3
drwxr-xr-x  2 lenovo lenovo 4096 Jul 16 19:08 test4
ls: cannot open directory 'testing/not_allowed': Permission denied

testing/.ssh:
total 16
drwxr-xr-x 2 lenovo lenovo 4096 Jul 16 23:22 .
drwxr-xr-x 8 lenovo lenovo 4096 Jul 16 23:26 ..
-rw-r--r-- 1 lenovo lenovo    8 Jul 16 18:51 id_test
-rw------- 1 lenovo lenovo   10 Jul 16 18:52 id_test2
-r--rw-rw- 1 lenovo lenovo    0 Jul 16 19:26 id_test3
-rw----r-- 1 lenovo lenovo    0 Jul 16 23:21 id_test4
-rw-r--r-- 1 lenovo lenovo    0 Jul 16 23:22 id_test5

testing/test1:
total 16
drwxr-xr-x 2 lenovo lenovo 4096 Jul 16 19:03 .
drwxr-xr-x 8 lenovo lenovo 4096 Jul 16 23:26 ..
-rwxrwxrwx 1 lenovo lenovo    5 Jul 16 18:49 deploy.sh
-rw------- 1 lenovo lenovo    1 Jul 16 19:00 test11
-rw----r-- 1 lenovo lenovo    0 Jul 16 19:03 test12
-------r-- 1 lenovo lenovo    0 Jul 16 19:03 test13

testing/test2:
total 8
drwxr-xr-x 2 lenovo lenovo 4096 Jul 16 19:05 .
drwxr-xr-x 8 lenovo lenovo 4096 Jul 16 23:26 ..
-rwx------ 1 lenovo lenovo    0 Jul 16 19:04 test21
-rwxr--r-- 1 lenovo lenovo    0 Jul 16 19:04 test22
-r--r--r-- 1 lenovo lenovo    0 Jul 16 19:04 test23
-r-x-w---x 1 lenovo lenovo    0 Jul 16 19:05 test24

testing/test3:
total 12
drwxr-xr-x 2 lenovo lenovo 4096 Jul 16 19:07 .
drwxr-xr-x 8 lenovo lenovo 4096 Jul 16 23:26 ..
--wxrwxrwx 1 lenovo lenovo    0 Jul 16 19:06 test31
-rw------x 1 lenovo lenovo    1 Jul 16 19:06 test32
-rwx--x--x 1 lenovo lenovo    0 Jul 16 19:06 test33
--w--w--w- 1 lenovo lenovo    0 Jul 16 19:07 test34

testing/test4:
total 8
drwxr-xr-x 2 lenovo lenovo 4096 Jul 16 19:08 .
drwxr-xr-x 8 lenovo lenovo 4096 Jul 16 23:26 ..
-r-xr-xr-x 1 lenovo lenovo    0 Jul 16 19:07 test41
-r-xrwxrw- 1 lenovo lenovo    0 Jul 16 19:07 test42
-rw-rwxrw- 1 lenovo lenovo    0 Jul 16 19:08 test43
-rwx---rwx 1 lenovo lenovo    0 Jul 16 19:08 test44

5. Typ B lebo bude to mat vacsiu hodnotu a lahsie bude vsimnut
