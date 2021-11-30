from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    callback: qr
    type: aggregate
    short_description: display play stats as a QR code
    requirements:
      - qrcode
'''

import io
import json
import qrcode

from ansible.plugins.callback import CallbackBase


class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'qr'
    CALLBACK_NEEDS_ENABLED = True
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self, display=None):
        super(CallbackModule, self).__init__(display=display)

    def v2_playbook_on_stats(self, stats):
        self._display.banner("PLAY RECAP QR")

        hosts = sorted(stats.processed.keys())
        result = {h: stats.summarize(h) for h in hosts}

        qr_result = qrcode.QRCode()
        qr_result.add_data(json.dumps(result))
        file_result = io.StringIO()
        qr_result.print_ascii(out=file_result)
        file_result.seek(0)

        self._display.display("", screen_only=True)
        self._display.display(file_result.read())
        self._display.display("", screen_only=True)
