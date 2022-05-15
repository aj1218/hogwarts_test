from decimal import Decimal

import pytest
import yaml

#
# with open(r"D:\pythonProject\hogwarts_test\python\testing\datas\add.yaml") as f:
from Testcase.testcode import Dome1

file = yaml.safe_load(open(r"D:\pythonProject\hogwarts_test\python\testing\datas\add.yaml"))
print(file)


def steps():
    with open(r"D:\pythonProject\hogwarts_test\python\testing\datas\test.yaml") as f:
        return yaml.safe_load(f)

class Test:
    @pytest.mark.parametrize("data1,data2,expect1", file)
    def test_divide(self, data1, data2, expect1):
        steps1 = steps()
        dome=Dome1()
        print(f"step=====>,{steps1}")
        for step in steps1:
            if 'add' == step:
                print(step)
                result = dome.add(data1, data2)
            elif 'dev' == step:
                print(step)
                result = dome.dev(data1, data2)
            print(result)
        assert expect1 == result


