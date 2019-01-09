import allure
import pytest

'''使用pytest+allure实现美观的测试报告

1. 安装allure，离线下载安装包，xxx/bin添加环境变量。(也可安装Windows PowerShell、Scoop在线安装allure)
    https://github.com/allure-framework/allure2/releases
2. 安装pytest-allure-adaptor。会连带安装pytest(建议自行安装pytest-3.10.x版本，与allure-2.8.1适用)
    pip install pytest-allure-adaptor
3. allure-commandline离线安装包，可不装，直接使用allure生成html测试报告
    https://github.com/allure-framework/allure1/releases/download/allure-core-1.5.2/allure-commandline.zip
4. 使用allure生成测试报告步骤：
  4.1 > pytest apytest.py -s -q --alluredir ./report/xml
  4.2 > allure generate ./report/xml -o ./report/html
    也可以使用allure-commandline生成html测试报告，个人感觉没有allure生成的好用，包括图表和中文支持。
  4.3 D:\Program Files\allure-commandline\bin> allure generate 已生成的xml路径 -o 待生成的html路径
5. 参考博客文章：
    https://www.cnblogs.com/hao2018/p/9915044.html
    https://www.cnblogs.com/xiaoxi-3-/p/9492534.html
    https://www.cnblogs.com/yrxns/p/8386267.html

定制报告：
    Feature: 标注主要功能模块
    Story: 标注Features功能模块下的分支功能
    Severity: 标注测试用例的重要级别
    Step: 标注测试用例的重要步骤
    Issue和TestCase: 标注Issue、Case，可加入URL

'''

@allure.feature('test_module_01')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 0


@allure.feature('test_module_02')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


@allure.feature('test_module_03')
def test_case_03():
    """
    用例描述：Test case 02
    """
    assert 1 == 2


if __name__ == "__main__":
    pytest.main()

