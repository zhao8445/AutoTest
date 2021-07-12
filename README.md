## 项目描述
- 基于vue-element-admin前端框架和Django服务框架实现的，面向团队内部的中后台管理系统，包括
 	- 热更新系统 
 	- 海外运营数据系统 
 	- 运营配置管理系统 
 	- 自动化工具


  
## 项目背景

 - 当一个App发布之后，突然发现了一个严重bug需要进行紧急修复，这时候公司各方就会忙得焦头烂额：重新打包App、测试、向各个应用市场和渠道换包、提示用户升级、用户下载、覆盖安装。重点是还会有原来的版本遗留，无论你怎么提示都有人不愿升级。

## 项目意义

 - 热更新系统的投入，提高了开发测试效率，实现了线上不停机快速紧急修复BUG
 - 运营管理及数据展示平台，满足了产品运营对用户登录，模块点击，用户在线数等打点数据掌握，以及游戏内邮件公告发送配置，游戏内轮播图配置，兑换码配置等相关需求

## 项目个人价值

 - 高效工作
	 - 前端开发经验不足的情况下，利用加班及个人时间，在没人指导的情况下通过查阅开源框架文档网络资料，独立解决开发中遇到的问题，保障开发质量同时未影响项目开发周期的前提下，从0到1完成了热更新系统的开发任务
 - 合作意识
	 - 在和其它组开发人员不熟的前提下，有效沟通，完成了开发任务，当在和其它开发在项目产生意见分歧时，会有效地进行沟通协商，会在一些非原则性问题，虽然增加自己工作量但是只要有利于项目也可作出退让
 - 工具平台的架构能力
	 - 根据团队实际需要进行平台所需用的技术栈和框架的调研和选型，会选择一些开发效率高功能组件成熟完善，更适合满足团队快速轻量级开发需求的技术框架，并可利用个人时间加班进行学习，实现将新技术新框架在项目中的应用
 - 自主学习能力强效率高
	 - 一个新的项目需要的新技术新框架，可快速短时间内学习掌握，并应用在项目

## 项目演示
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621140249669.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021062114011324.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
 - 老版本的管理平台系统，由于人力有限，存在着不同分辨率显示器，不同浏览器的兼容问题，历史遗留冗余代码较多，系统分层有待完善和优化等诸多问题

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621140148494.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621140148476.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)

 - 新版本系统，前段采用了一套较为成熟的当前比较热门的后台管理前端框架，vue-element-admin，提供了更为完善的组件和功能，基本可以满足大部分当前后台的需求，界面样式，浏览器及分辨率的兼容性，权限验证等诸多问题都得到了解决，系统分层设计更加合理，代码格式规范化得到加强。
 - [老版本自动化及运营管理平台演示](https://www.bilibili.com/video/BV1e5411K73T/)
 - [新框架自动化及运营管理平台演示](https://www.bilibili.com/video/BV1cy4y1g7wb/)
 - [热更新系统演示](https://www.bilibili.com/video/BV1fK4y137GA/)


## 项目技术

- #### 后端技术

 - Web开发框架Django，包含成熟完善的功能，如后台账号管理，系统注册登录等功能，满足面向团队内部快速轻量级管理平台的开发的需求

- #### 前端技术
 - Element UI
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621134812104.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
 - vue-element-admin
 ![](https://img-blog.csdnimg.cn/20210621135235183.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
 
 - vue-element-admin 是一个后台前端解决方案，它基于 vue 和 element-ui实现。它使用了最新的前端技术栈，内置了 i18 国际化解决方案，动态路由，权限验证，提炼了典型的业务模型，提供了丰富的功能组件，它可以帮助你快速搭建企业级中后台产品前端框架。
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210621141811806.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
 - GitPython 是一个 Python 库，用于与 git 存储库交互，高级如 git-porcelain，或低级如 git-plumbing。
## 新版框架项目代码结构
- #### 后端代码
![在这里插入图片描述](https://img-blog.csdnimg.cn/2021062410074266.png#pic_center)
- #### 前端代码
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210624100804573.png#pic_center)

## 新版本平台的权限验证
- 服务端采用了Django自动用户管理Auth模块
	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623220322366.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623220322375.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623220429991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
- 采用rest_framework_jwt第三方库进行密码校验并生成token，在Django项目中的settings文件按照jwt的文档进行配置

	```python
	REST_FRAMEWORK = {
	    'DEFAULT_PERMISSION_CLASSES': (
	        'rest_framework.permissions.IsAuthenticated',
	    ),
	
	    'DEFAULT_AUTHENTICATION_CLASSES': (
	        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
	        'rest_framework.authentication.SessionAuthentication',
	        'rest_framework.authentication.BasicAuthentication',
	    ),
	
	}
	```
- 客户端输入账号密码，服务端校验成功后返回一个token，接下来客户端每次请求时会带上这个token，服务端进行校验并根据token会返回用户信息
	![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623221743875.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623221743862.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)
- 前端在动态路由文件中，在roles参数中进行权限参数的配置即可实现系统的权限管理，例如在roles参数中配置"has_hotupdate'参数，则返回的用户信息json数据roles字段下有“has_hotupdate'参数的才可看到热更新的菜单栏
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210623221856270.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMxNzU5MjAz,size_16,color_FFFFFF,t_70#pic_center)


## 热更新系统设计思路

 - Git打包命令：
	 `git archive --format=zip -o path branch $(git diff --diff-filter=d revision_old revision_new --name-only)`
 - 通过GitPython库实现用Python语言调用git相关命令来进行相关的git操作
 - 将GitPython模块中Git().execute(command, shell)方法封装为git_cmd(working_dir, command)方法，调用该方法来执行"git clone"命令，克隆远程仓库代码到本地
	```python
    def clone_git(self, branch, url, to_path, username, password):
        """
        克隆远程git仓库代码到本地
        :param branch: 分支名
        :param url: 远程git仓库地址
        :param to_path: zip包输出路径
        :param username: git账号
        :param password: git账号密码
        :return: 克隆到本地的仓库路径
        """
        url = url.replace("http://", "")
        url = "http://" + 'root' + ":" + password + "@" + url
        respo_name = re.findall(r'\S+//\S+/\S+/(\S+).git', url).pop()
        to_path = to_path + '/' + username + '/' + time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
        
        if os.path.exists(to_path):
            shutil.rmtree(to_path, ignore_errors=True)
        os.makedirs(to_path)
        command = "git clone -b " + branch + " " + url
        self.git_cmd(to_path, command)

        path = to_path + "/" + respo_name
        return path
	        
    def git_cmd(self, working_dir, command):
        """
        执行git系统命令
        :param working_dir: 本地仓库路径
        :param command: 所需执行的git命令
        :return: 执行命令结果
        """
        exec_res = Git(working_dir).execute(command=command, shell=True)
        return exec_res

	```

 - 通过封装的git_cmd方法调用git archive命令将git仓库两次提交节点之间的差异文件打成zip包
	```python
    def git_package(self, app_version, create_time, to_path, revision_new, revision_old, output_path, package_name, branch):
        """
        调用git命令打出差异包
        :param app_version: app版本号
        :param create_time: 创建时间
        :param revision_new: git仓库新提交节点
        :param revision_old: git仓库老提交节点
        :param output_path: zip包输出路径
        :param package_name: zip差异包名
        :param branch: 打包git仓库分支
        :return: zip包名
        """
        if not os.path.exists(MEDIA_ROOT + output_path):
            os.mkdir(MEDIA_ROOT + output_path)
            
        package_name = package_name + "_" + create_time + "_" + app_version + "_" + "1" + "_" + "1" ".zip"
        command = "git archive --format=zip -o " + MEDIA_ROOT + output_path + package_name + " " + branch + " $(git diff --diff-filter=d " + revision_old + " " + revision_new + " --name-only)"
        self.git_cmd(self.working_dir, command)
        
        return package_name
	```

 - 将打出的差异包根据游戏ID和国家渠道等参数的配置传送给客户端

	




