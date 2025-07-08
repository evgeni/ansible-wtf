```
PLAY [fail] *************************************************************************

TASK [Gathering Facts] **************************************************************
ok: [localhost]

TASK [fail : include_tasks] *********************************************************
included: /home/evgeni/Devel/ansible-wtf/reporting/roles/fail/tasks/include_role.yml for localhost => (item=fail1)
included: /home/evgeni/Devel/ansible-wtf/reporting/roles/fail/tasks/include_role.yml for localhost => (item=fail2)
included: /home/evgeni/Devel/ansible-wtf/reporting/roles/fail/tasks/include_role.yml for localhost => (item=fail3)

TASK [include_role : {{ item }}] ****************************************************
included: fail1 for localhost

TASK [fail1 : fail1] ****************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "one"}

TASK [fail : set_fact] **************************************************************
ok: [localhost]

TASK [include_role : {{ item }}] ****************************************************
included: fail2 for localhost

TASK [fail2 : fail2] ****************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "two"}

TASK [fail : set_fact] **************************************************************
ok: [localhost]

TASK [include_role : {{ item }}] ****************************************************
included: fail3 for localhost

TASK [fail3 : fail3] ****************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "three"}

TASK [fail : set_fact] **************************************************************
ok: [localhost]

TASK [fail : fail] ******************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": [{"changed": false, "failed": true, "msg": "one"}, {"changed": false, "failed": true, "msg": "two"}, {"changed": false, "failed": true, "msg": "three"}]}

PLAY RECAP **************************************************************************
localhost : ok=10 changed=0 unreachable=0 failed=1 skipped=0 rescued=3 ignored=0
```
