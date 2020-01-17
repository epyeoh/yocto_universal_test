import unittest
import os, sys
script_path = os.path.dirname(os.path.realpath(__file__))
lib_path = script_path + '/../../lib'
sys.path = sys.path + [lib_path]
print('PATH=%s' % sys.path)
from utils.targets.localhosttarget import LocalHostTarget
from bblayers.metaintel.lib.oeqa.runtime.miutils.tests.squeezenet_model_download_test import SqueezenetModelDownloadTest
from bblayers.metaintel.lib.oeqa.runtime.miutils.tests.dldt_model_optimizer_test import DldtModelOptimizerTest

class ModelOptimizerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sqn_download = SqueezenetModelDownloadTest(LocalHostTarget(), '/tmp/mo/md')
        cls.sqn_download.setup()
        cls.dldt_mo = DldtModelOptimizerTest(LocalHostTarget(), '/tmp/mo/ir')
        cls.dldt_mo.setup()
    
    # Comment temporary for showcase the test outcome
    # @classmethod
    # def tearDownClass(cls):
    #     cls.dldt_mo.tear_down()
    #     cls.sqn_download.tear_down()

    def test_mo_can_create_ir(self):
        proxy_port = 'proxy.png.intel.com:911'
        (status, output) = self.sqn_download.test_can_download_squeezenet_model(proxy_port)
        self.assertEqual(status, 0, msg='status and output: %s and %s' % (status, output))
        (status, output) = self.sqn_download.test_can_download_squeezenet_prototxt(proxy_port)
        self.assertEqual(status, 0, msg='status and output: %s and %s' % (status, output))

        mo_exe_dir = '/opt/intel/openvino_2019.3.376/deployment_tools/model_optimizer/'
        mo_files_dir = self.sqn_download.work_dir
        (status, output) = self.dldt_mo.test_dldt_mo_can_create_ir(mo_exe_dir, mo_files_dir)
        self.assertEqual(status, 0, msg='status and output: %s and %s' % (status, output))

