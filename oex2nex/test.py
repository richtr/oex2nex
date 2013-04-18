#!/usr/bin/env python

import unittest

from tests.api_finder import TestAPIFinder
from tests.browser_action import TestBrowserAction
from tests.norm_version import TestNormVersion
from tests.nex import TestNEX
from tests.manifest import TestManifest, TestManifestIconsFileName, TestManifestIconsAttr, TestManifestSpeedDialAttr
from tests.permissions import TestContextMenuPerms, TestCookiesPerms, TestTabsPerms, TestWebRequestPerms, TestSpeedDialPerms


def tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    suite.addTests(loader.loadTestsFromTestCase(TestAPIFinder))
    suite.addTests(loader.loadTestsFromTestCase(TestBrowserAction))
    suite.addTests(loader.loadTestsFromTestCase(TestNormVersion))
    suite.addTests(loader.loadTestsFromTestCase(TestNEX))
    suite.addTests(loader.loadTestsFromTestCase(TestManifest))
    suite.addTests(loader.loadTestsFromTestCase(TestManifestIconsFileName))
    suite.addTests(loader.loadTestsFromTestCase(TestManifestIconsAttr))
    suite.addTests(loader.loadTestsFromTestCase(TestManifestSpeedDialAttr))
    suite.addTests(loader.loadTestsFromTestCase(TestContextMenuPerms))
    suite.addTests(loader.loadTestsFromTestCase(TestCookiesPerms))
    suite.addTests(loader.loadTestsFromTestCase(TestTabsPerms))
    suite.addTests(loader.loadTestsFromTestCase(TestWebRequestPerms))
    suite.addTests(loader.loadTestsFromTestCase(TestSpeedDialPerms))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(tests())
