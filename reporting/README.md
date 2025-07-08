```
PLAY [fail] *************************************************************************

TASK [Gathering Facts] **************************************************************
ok: [localhost]

TASK [include_role : {{ item }}] ****************************************************
included: fail1 for localhost => (item=fail1)
included: fail2 for localhost => (item=fail2)
included: fail3 for localhost => (item=fail3)

TASK [fail1 : fail1] ****************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "one"}
...ignoring

TASK [fail1 : set_fact] *************************************************************
ok: [localhost]

TASK [fail2 : fail2] ****************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "two"}
...ignoring

TASK [fail2 : set_fact] *************************************************************
ok: [localhost]

TASK [fail3 : fail3] ****************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "three"}
...ignoring

TASK [fail3 : set_fact] *************************************************************
ok: [localhost]

TASK [fail : fail] ******************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": ["one", "two", "three"]}

PLAY RECAP **************************************************************************
localhost : ok=10 changed=0 unreachable=0 failed=1 skipped=0 rescued=0 ignored=3
```
