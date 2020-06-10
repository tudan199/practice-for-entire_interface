import unittest
from utils.HTMLTestRunner import HTMLTestRunner
testsuite1=unittest.TestSuite()
testcases=unittest.defaultTestLoader.discover("C:/Users/eagle/Desktop/practise/practice for entire_interface/structure1_unittest/testcases","test*.py")
testsuite1.addTests(testcases)

filepath='C:/Users/eagle/Desktop/practise/practice for entire_interface/structure1_unittest/report/report.html'
filename='testreport'
title='testtitle'
desc='reportdesc'
with open(filepath,'wb') as f:
    runner= HTMLTestRunner(stream=f,title=title,description=desc)
    runner.run(testsuite1)
