#-*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version


class TestWolf(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pyrsslocal", "pyrsslocal"],
                                        __file__, hide=True)

    def test_wolf(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.actuariat_python.data import wolf_xml
        temp = get_temp_folder(__file__, "temp_wolf")
        outfile = wolf_xml(fLOG=fLOG, temp_folder=temp)
        if isinstance(outfile, str):
            outfile = [outfile]
        for o in outfile:
            if not os.path.exists(o):
                raise FileNotFoundError(o)
        if os.stat(outfile[0]).st_size < 2000:
            raise Exception("small size")

    def test_enumerate_wolf_xml_row(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            from src.actuariat_python.data import enumerate_wolf_xml_row
            temp = get_temp_folder(__file__, "temp_enumerate_wolf_xml_row")
            data = os.path.join(temp, "..", "data", "sample.wolf.xml")
            rows = enumerate_wolf_xml_row(data, fLOG=fLOG, encoding=None)
            for row in rows:
                fLOG(type(row))

    def test_enumerate_wolf_synonyms(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            from src.actuariat_python.data import enumerate_wolf_synonyms
            temp = get_temp_folder(__file__, "temp_enumerate_wolf_xml_row")
            data = os.path.join(temp, "..", "data", "sample.wolf.xml")
            rows = enumerate_wolf_synonyms(data, fLOG=fLOG, encoding=None)
            for row in rows:
                fLOG(row)

    def test_enumerate_wolf_synonyms_big(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_enumerate_wolf_xml_row")
        data = os.path.join(temp, "..", "data", "wolf-1.0b4.xml")
        if os.path.exists(data):
            from src.actuariat_python.data import enumerate_wolf_synonyms
            rows = enumerate_wolf_synonyms(data, fLOG=fLOG)
            for i, row in enumerate(rows):
                fLOG(row)
                if i > 300:
                    break


if __name__ == "__main__":
    unittest.main()
