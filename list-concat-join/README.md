```
% ansible-playbook playbook.yml

PLAY [localhost] **************************************************************

TASK [set_fact] ***************************************************************
ok: [localhost]

TASK [show that both_lists is a list] *****************************************
ok: [localhost] => {
    "msg": [
        "a_something",
        "another_something"
    ]
}

TASK [show that you can add lists to a list, with parentheses] ****************
ok: [localhost] => {
    "msg": [
        "a_something",
        "another_something"
    ]
}

TASK [show that you can add lists to a list, WITHOUT parentheses] *************
ok: [localhost] => {
    "msg": [
        "a_something",
        "another_something"
    ]
}

TASK [join both_lists] ********************************************************
ok: [localhost] => {
    "msg": "a_something, another_something"
}

TASK [join with parentheses works] ********************************************
ok: [localhost] => {
    "msg": "a_something, another_something"
}

TASK [join without parentheses fails] *****************************************
fatal: [localhost]: FAILED! => {"msg": "Unexpected templating type error occurred on ({{ a_list + another_list | join(', ') }}): can only concatenate list (not \"str\") to list"}

PLAY RECAP ********************************************************************
localhost                  : ok=6    changed=0    unreachable=0    failed=1   
```
