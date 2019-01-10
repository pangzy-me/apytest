import allure
import pytest

'''使用pytest+allure实现美观的测试报告

安装步骤：
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

定制测试报告参数说明：
    @allure.feature     # 用于定义被测试的功能，被测产品的需求点
    @allure.story       # 用于定义被测功能的用户场景，即子功能点
    @allure.severity    # 标注测试用例的重要级别
    @allure.step        # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
    @allure.issue
    @allure.testcase    # 标注Issue、TestCase，可加入URL链接

    with allure.step    # 用于将一个测试用例，分成几个步骤在报告中输出
    allure.attach       # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
    allure.environment  # 用于向测试报告中添加环境信息，可随意加


severity定制详解：
    Allure中对严重级别的定义：
    1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
    2、 Critical级别：临界缺陷（ 功能点缺失）
    3、 Normal级别：普通缺陷（数值计算错误）
    4、 Minor级别：次要缺陷（界面错误与UI需求不符）
    5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）


attach定制详解：
    file = open('../test.png', 'rb').read()
    allure.attach('test_img', file, allure.attach_type.PNG)
        在报告中增加附件：allure.attach(’arg1’,’arg2’,’arg3’)：
        arg1：是在报告中显示的附件名称
        arg2：表示添加附件的内容
        arg3：表示添加的类型(支持:HTML,JPG,PNG,JSON,OTHER,TEXTXML)

'''


@allure.feature('功能模块module_01')
@allure.story('模块module_01下子功能story01')
@allure.severity('critical')
# @allure.step('测试步骤一：')
@allure.issue('BUG编号：89757')
@allure.testcase('用例名称：主模块1')
def test_case_01():
    """
    用例描述：此段为测试用例的描述
    :return:
    """
    allure.environment(host='127.0.0.1')  # 测试报告中展示environment配置的环境变量，随意命名
    host_name = "my.host.local"
    allure.environment(hostname=host_name)
    allure.environment(report='Allure report', browser=u'Я.Браузер')
    allure.environment(alibaba='杭州阿里巴巴集团')

    with allure.step("第一步：浏览商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中
        allure.attach('商品1', '康师傅')  # attach可以向测试报告中输入一些附加的信息
        allure.attach('商品2', '冰红茶')
        allure.attach('商品3', '酒鬼花生')
    with allure.step("第二步：点击商品"):  # 将一个测试用例分成几个步骤，将步骤打印到测试报告中
        file = open('./藏狐.jpg', 'rb').read()    # attach向测试报告中输入图片附件信息
        allure.attach('test_img', file, allure.attach_type.JPG)
        allure.attach('test_img', file, allure.attach_type.JPG)
        pass
    with allure.step("第三步：校验结果"):
        allure.attach('期望结果', '添加商品列表成功')
        allure.attach('实际结果', '添加商品列表失败')
        assert 'success' == 'failed'


@allure.feature('功能模块module_01')
@allure.story('模块module_01下子功能story02')
@allure.severity('critical')
def test_case_02():
    """
    用例描述：此段为测试用例的描述
    """
    assert 0 == 0


@allure.feature('功能模块module_02')
@allure.severity('minor')
def test_case_03():
    """
    用例描述：此段为测试用例的描述
    """
    assert 2 == 2


@allure.feature('功能模块module_03')
@allure.severity('minor')
def test_case_04():
    """
    用例描述：此段为测试用例的描述
    """
    assert 2 == 2


if __name__ == "__main__":
    pytest.main()

