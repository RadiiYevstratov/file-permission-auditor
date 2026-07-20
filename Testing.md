testing/test1/deploy.sh              777                   WW                            Typ A
testing/test1/test11                     600                   ZN                              ZN
testing/test1/test12                    604                   ZN                              ZN
testing/test1/test13                    004                   ZN                              ZN
testing/test2/test21                   700                   ZN                              ZN
testing/test2/test22                  744                   ZN                              ZN
testing/test2/test23                  444                   ZN                              ZN
testing/test2/test24                  521                    ZN                              ZN
testing/test3/test31                   377                   WW                            Typ A
testing/test3/test32                  601                    ZN                              ZN
testing/test3/test33                  711                     ZN                              ZN
testing/test3/test34                  222                  WW                            Typ A
testing/test4/test41                   555                  ZN                               ZN
testing/test4/test42                  576                  WW                            Typ A
testing/test4/test43                  676                  WW                            Typ A
testing/test4/test44                  707                  WW                            Typ A
testing/.ssh/id_test                        644                 UK                              Typ B
testing/.ssh/id_test2                      600                 ZN                              ZN
testing/.ssh/id_test3                      466                 UK                               Typ B
testing/.ssh/id_test4                      604                 UK                              Typ B
testing/.ssh/id_test5                      640                 UK                              Typ B
testing/ww_466                                      466                 WW                           Typ A
testing/not_allowed                       000                 skipped                   missing permission
testing/permission_644  644  ZN  ZN

## Error handling testy
python3 auditor.py /neexistujuca/cesta        —    hláška + exit 1    error test: neexistujúca cesta
python3 auditor.py testing/ww_466             —    hláška + exit 1    error test: súbor namiesto adresára

7 - WW
4 - UK