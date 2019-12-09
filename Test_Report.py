import unittest
import HtmlTestRunner
import os

from HtmlTestRunner import HTMLTestRunner
from Unit_test import Selenium_Test


class Selenium_Test_Report(unittest.TestCase):
    def test_report_generation(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Selenium_Test),

        ])
        direct = os.getcwd()

        outfile = open(direct + "\Rasa_test.html", "w")

        runner1 = HTMLTestRunner(
            stream=outfile,
            report_title='Test Report',
            descriptions='Chatbot_Test_Report'
        )

        runner1.run(smoke_test)


obj = Selenium_Test_Report()
obj.test_report_generation()