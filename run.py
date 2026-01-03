import shutil
import pytest
import os
import webbrowser
from datetime import datetime
from conf.setting import REPORT_TYPE

if __name__ == '__main__':
    if REPORT_TYPE == 'allure':
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_dir = f'./report/easyjava_{timestamp}'
        
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        
        pytest.main(
            ['-s', '-v', f'--alluredir={report_dir}', './testcase/easyjava_test/test_user.py',
             '--junitxml=./report/results.xml'])

        shutil.copy('./environment.xml', report_dir)
        os.system(f'allure serve {report_dir}')

    elif REPORT_TYPE == 'tm':
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_dir = f'./report/tmreport/easyjava_{timestamp}'
        
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        
        pytest.main(['-vs', '--pytest-tmreport-name=testReport.html', f'--pytest-tmreport-path={report_dir}', './testcase/taobao'])
        webbrowser.open_new_tab(os.path.join(os.getcwd(), report_dir, 'testReport.html'))
