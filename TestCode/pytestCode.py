import sys
import pytest

print("路劲为:", sys.path)
sys.path.append(r"D:\pythonProject\hogwarts_test")
from Testcase.testcode import Dome1

class Test_pytest_Dome:
    @pytest.mark.run(order=2)
    def test_pytest_dome(self):
        self.dome = Dome1()
        result = self.dome.add(1, 2)
        print("result的结果为:",result)
        assert 3 == result

    @pytest.mark.add
    def test_dev(self):
        self.dome = Dome1()
        result = self.dome.dev(4, 1)
        print("test_dev的结果为 :",result)
        assert 3 == result

    @pytest.mark.run(order=1)
    def test_dev1(self):
        self.dome = Dome1()
        result = self.dome.dev(4, 1)
        print("test_dev的结果为 :",result)
        assert 3 == result


if __name__ == '__main__':
    pytest.main(['-vs', r'D:\pythonProject\hogwarts_test\TestCode\pytestCode.py::Test_pytest_Dome::test_dev'])
