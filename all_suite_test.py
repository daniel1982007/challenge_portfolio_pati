import unittest
from unittest import makeSuite
from test_cases.login_to_system import LoginPageTest
from test_cases.logout_from_system import LogoutTest
from test_cases.add_a_player import AddPlayerTest

def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(LoginPageTest))
    test_suite.addTest(makeSuite(LogoutTest))
    test_suite.addTest(makeSuite(AddPlayerTest))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())