## 项目描述

 - 一款基于Airtest和Unittest，并融合了百度OCR文字识别技术，面向游戏的自动化测试框架

## 项目背景
 - 在测试流程中为了避免版本迭代时代码的改动导致其他模块出现问题，存在着一些重复性强的回归测试，或者靠人工操作比较繁琐的测试用例，占用了大量的人力和工期，导致测试的效率降低，削弱了测试人员去发现版本迭代中逻辑性较强的功能性BUG的时间和精力，降低了产品线上质量的保证
 
## 项目意义
 - 总功 = 有用功+无用功
 - 效率 = 有用功/总功
 - 增加（分子）有用功 =>
 将测试流程中重复性强，可回归，耗时长人工不易操作的测试用例自动化
 - 减少（分母）无用功=>
	将人力释放出来去发现更多版本迭代中逻辑性强的功能性BUG，从而在一定程度上		提升产品的线上质量


## 项目演示
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021062322011178.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)

[自动化测试框架演示](https://www.bilibili.com/video/BV1Mw411o76g/)


## 项目个人价值

 - 探索性解决问题
	 - 在使用过程中发现存在图像识别结果不能百分百准的问题，如将5识别成S，0识别成O，经过调研决定放弃之前的图像识别插件Teserract，改用百度ocr文字识别技术，有效提升了文字识别的准确率
 - 框架的整体架构设计能力
	 - 挖掘在测试工作流程中影响测试效率的痛点，并通过阅读公众号及技术博客相关文章，借鉴互联网大厂在自动化测试框架上面的实践经验，结合自身团队内部的实际情况提炼出相关框架的需求，并根据需求进行测试框架系统的分层设计，各接口业务逻辑之间的关系，以及技术栈框架的选型，从而从无到有独立设计开发出一款实用性强，易维护的自动化框架

## 项目技术

 - #### AirTest自动化测试框架
	Airtest：是一个跨平台的、基于图像识别的UI自动化测试框架，适用于游戏和App，支持平台有Windows、Android和iOS
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621153657985.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)

 - #### Unittest单元测试框架
	该unittest单元测试框架最初是由JUnit的启发，也有类似的味道在其他语言主要单元测试框架。它支持测试自动化，自动化测试case的批量管理和执行，并生成聚合报告
 - #### 百度OCR文字识别技术
 	* 官方网站
	![在这里插入图片描述](https://img-blog.csdnimg.cn/2021062115430727.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
	* 在这里我们采取调用百度文字识别API接口的形式来进行识别图片上的文字
		![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621154539444.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
*	 调用百度OCR文字识别接口方法
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621163136235.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)

	* 百度智能云控制台会展示百度OCR文字识别接口调用情况
	![在这里插入图片描述](https://img-blog.csdnimg.cn/2021062115472914.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)


## 框架设计思路
- #### 框架整体分层设计
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621155355895.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)

- #### base_view层
	BaseView基类封装了一些公共方法
	```python
	def partial_screenshot(x_start, y_start, x_end, y_end, filename):
	    """
	    局部截图
	    :param x_start: 起始x坐标
	    :param y_start: 起始y坐标
	    :param x_end: 终止x坐标
	    :param y_end: 终止y坐标
	    :param filename: 保存的文件名
	    :return:
	    """
	    auto_setup(__file__)
	    screen = G.DEVICE.snapshot(quality=99)
	
	    # 局部截图
	    local = aircv.crop_image(screen, (x_start, y_start, x_end, y_end))
	
	    # 保存局部截图到测试结果集文件夹中
	    pil_image = cv2_2_pil(local).convert()
	    save_path = PROJECT_ROOT_PATH + '/test_result_imgs/' + filename
	    pil_image.save(save_path, quality=99, optimize=True)
	
	    return save_path
	
	def click_close_btn():
	    """
	    点击关闭按钮
	    :return:
	    """
	    try:
	        position = wait(Template(PROJECT_ROOT_PATH + r"/imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
	                                 resolution=(2232, 1080)), timeout=5, interval=1)
	        while position:
	            touch(position)
	            position = wait(Template(PROJECT_ROOT_PATH + r"/imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
	                                     resolution=(2232, 1080)), timeout=5, interval=1)
	    except TargetNotFoundError:
	        pass
	```
- #### config层
	系统配置文件
	

	```python
	import os
	
	params = {
	    "package_name": "com.ccmt.augupoker",
	    "project_root_path": os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/'),
	}
	```

- #### imgs层
	imgs层存放UI定位的图像元素		![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621160540899.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)

- #### reports层
	reports层存放测试报告
	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621160926640.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621160926615.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)

- #### test_view层
	存放业务逻辑代码，例如测试登陆的业务逻辑代码login_view
	```python
	# -*- encoding=utf8 -*-
	
	__author__ = "zhaobl01"
	
	from base_view.base_view import *
	
	PACKAGE_NAME = params["package_name"]
	
	class LoginView:
	    def __init__(self):
	        # 启动APP
	        start_app(PACKAGE_NAME)
	
	    def login_as_guest(self):
	        """
	        访客登陆
	        :return:
	        """
	        try:
	            position = wait(Template(
	                PROJECT_ROOT_PATH + r"/imgs/login/continue_as_guest.png", record_pos=(0.002, 0.196),
	                resolution=(1280, 800), threshold=0.7), timeout=20, interval=1)
	            touch(position)
	        except TargetNotFoundError:
	            # print("Login as Guest Button Not Found")
	            pass
	
	    def close_tap(self):
	        """
	        关闭签到登陆等tab页
	        :return:
	        """
	        try:
	            position = wait(Template(PROJECT_ROOT_PATH + r"/imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
	                                     resolution=(2232, 1080), threshold=0.8), timeout=10, interval=1)
	            while position:
	                touch(position)
	                position = wait(Template(PROJECT_ROOT_PATH + r"/imgs/icon/close_tag_icon.png", record_pos=(0.382, -0.217),
	                                         resolution=(2232, 1080), threshold=0.8), timeout=5, interval=1)
	        except TargetNotFoundError:
	            # print("Tag Close Button Not Found")
	            pass
	
	    def check_logined(self):
	        """
	        检测是否登陆成功
	        :return:
	        """
	        try:
	            assert_exists(Template(PROJECT_ROOT_PATH + r"/imgs/login/play_now_btn.png", record_pos=(-0.001, 0.205),
	                                   resolution=(2232, 1080), threshold=0.7), "通过PLAY_NOW按钮判断是否登陆")
	            return True
	        except AssertionError:
	            return False
	
	    def logout(self):
	        """
	        退出游戏并清理缓存
	        :return:
	        """
	        sleep(5)
	        clear_app(PACKAGE_NAME)
	        stop_app(PACKAGE_NAME)
	
	```

- #### test_case层
	按业务划分测试case，例如测试访客登陆的测试case如下：
	```python
	from base_view.base_unit import *
	from test_view.login_view.login_view import LoginView
	import unittest
	
	
	class TestLogin(StartEnd):
	    def test_login_as_guest(self):
	        """
	        访客登陆测试用例
	        """
	        l = LoginView()
	        l.login_as_guest()
	```

## 项目难点
 - ##### 如何自动识别校验游戏内的数据，例如玩家持有的金币数？
 	* 将游戏内玩家持有金币数的界面元素进行部分截图，并存放于test_result_imgs目录下
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021062116231856.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
	* 将待识别的图片通过POST请求提交至百度智能云提供的文字识别OCR接口

		```python
		def img_ocr(img_path):
		    """
		    百度OCR文字识别
		    """
		    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
		
		    # 二进制方式打开图片文件
		    f = open(img_path, 'rb')
		    img = base64.b64encode(f.read())
		
		    params = {"image": img}
		    access_token = get_token()
		    request_url = request_url + "?access_token=" + access_token
		    headers = {'content-type': 'application/x-www-form-urlencoded'}
		    response = requests.post(request_url, data=params, headers=headers)
		    if response:
		        response = response.json()
		        words = response["words_result"][0]["words"]
		        print(response)
		        print(words)
		        f.close()
		        return words
		
		    f.close()
		    return ""
		```
	* 请求返回识别结果如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621162817468.jpg#pic_center)


 	
