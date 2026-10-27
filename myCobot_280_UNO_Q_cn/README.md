# myCobot 280 UNO Q(2023)
算法验证实践教学

核心文档
---

本文档包含从产品简介、详细的技术参数到用户须知和产品开发指导的全面信息。文档将深入介绍myCobot 280 UNO Q机械臂的基础功能，并提供软件开发指南，展示成功的应用案例，帮助您了解如何将myCobot 280 UNO Q有效整合进各种应用中。此外，我们还提供了丰富的支持与服务信息，确保您在遇到任何技术挑战时能够获得必要的帮助。


文档说明
---

根据您的需求以及myCobot 280 UNO Q应用程序开发的专业水平，您可以选择从头到尾遵循该顺序进行阅读，或将其用作独立参考。您可以随时使用左侧的侧边栏导航跳转到本文档的任何部分，全文共分为以下五大板块：

#### 产品信息
产品信息板块将为您提供机械臂的基本概述，包括主要功能、产品参数和电气特性等详细的技术规格，帮助您快速了解产品的基本特性和使用环境。此外，这一部分将详细介绍产品的应用实例和支持的扩展开发，为您提供必要的开发指南和资源。文末将给出相关购买链接和渠道，方便您进行购买。

#### 基础设置
本章节是使用本产品的每一位用户必须仔细阅读的重要部分。它涵盖了关于产品使用、运输、储存及维护的关键须知，旨在确保用户在操作产品时的安全性和效率。此外，本章节也详细说明了因未遵循这些指南而可能导致的产品故障或损害的责任划分。

#### 功能与应用
功能与应用板块详细介绍了机械臂的基础功能和软件使用方法，包括系统使用说明和固件功能。软件开发指南提供了基于不同开发环境的指导，如Python和ROS，支持技术开发者进行应用扩展。通过展示成功的应用案例和提供配套资源，为您提供实践参考和必要的支持材料，以便更深入地了解和使用产品。

#### 支持与服务
支持与服务板块将为您提供全面的故障排除指南和购买后的服务信息，如保修和服务条款，帮助您在遇到问题时能够快速解决，并确保您了解购买后的权利和义务。此外，'关于我们'部分加强了用户对myCobot 系列产品设计及制造商的了解，旨在建立信任和品牌忠诚。

#### 致谢
我们非常感谢您花时间阅读myCobot 280 UNO Q用户手册。我们希望本文档能够帮助您更好地了解并有效使用这款机器人，从而激发您的创造力。如果您有任何疑问或需要进一步帮助，请随时联系我们的客户支持团队。我们期待看到您使用 myCobot 280 UNO Q完成创新项目，并欢迎您加入我们快速发展的开发者社区。

文档目录  

---

# Summary
* [Introduction](README.md)
* 产品信息
    * [1. 产品简介](1-ProductInformation/1.ProductIntroduction/1-ProductIntroduction.md)
    * [2. 产品参数](1-ProductInformation/2.ProductParameter/2-ProductParameters.md)
* 基础设置
    * [3. 用户须知](2-BasicSettings/3.UserNotice/3-UserInstructions.md)
    * [4. 首次安装](2-BasicSettings/4.FirstTimeInstallation/4-FirstTimeInstallation.md)
        * [4.1 首次使用自查](4-SupportAndService/9.Troubleshooting/9.4-first-time-self-check.md)
        *  [4.2 软件问题](4-SupportAndService/9.Troubleshooting/9.2-software.md)
        *  [4.3 硬件问题](4-SupportAndService/9.Troubleshooting/9.3-hardware.md)
        *  [4.4 配件相关问题](4-SupportAndService/9.Troubleshooting/9.1-accessories.md)
        *  [4.5 其他](4-SupportAndService/9.Troubleshooting/9.0-other.md)

* 功能与应用
    * [5. 基础功能](3-FunctionsAndApplications/5.BasicFunction/README.md)
        * [5.1 机械臂系统使用介绍](3-FunctionsAndApplications/5.BasicFunction/5.1-Functionlnstruction/DevelopmEntenvironment.md)
        * [5.2 myStudio说明](3-FunctionsAndApplications/5.BasicFunction/5.2-Softwarelnstructions/README.md)
        * [5.3 硬件接口](3-FunctionsAndApplications/5.BasicFunction/5.3-FirmwareFunctionDescription/RoboticArmElectricalInterface.md)
        * [5.4 PID控制](3-FunctionsAndApplications/5.BasicFunction/5.4-RobotPrecisionControl/README.md)
    * [6. 软件开发指南](3-FunctionsAndApplications/6.DevelopmentGuide/README.md)
      * [6.1 基于Python 开发使用](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/README.md)
        * [6.1.1 环境与通信检查](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/6.1.1-Environment.md)
        * [6.1.2 API 使用说明](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/6.1.2-API.md)
        * [6.1.3 TCP Socket 远程控制](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/6.1.3-TCPSocket.md)
        * [6.1.4 RGB 控制](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/6.1.4-RGB.md)
        * [6.1.5 关节控制](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/6.1.5-JointControl.md)
        * [6.1.6 坐标控制](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/6.1.6-CoordinateControl.md)
        * [6.1.7 夹爪与吸泵控制](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/6.1.7-GripperPump.md)
        * [6.1.8 手柄控制](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/6.1.8-Joystick.md)
        * [6.1.9 综合演示案例](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/6.1.9-Examples.md)
        * [6.1.10 日志与故障排查](3-FunctionsAndApplications/6.DevelopmentGuide/6.1-python/Troubleshooting.md)

      * [6.2 基于 Arduino App Lab 开发使用](3-FunctionsAndApplications/6.DevelopmentGuide/6.2-applab/README.md)
        * [6.2.1 App Lab 基础使用](3-FunctionsAndApplications/6.DevelopmentGuide/6.2-applab/6.2.1-GettingStarted.md)
        * [6.2.2 手柄控制](3-FunctionsAndApplications/6.DevelopmentGuide/6.2-applab/6.2.2-Joystick.md)

     
    * [7. 成功案例](3-FunctionsAndApplications/7.SuccessfulCase/7-SuccessfulCases.md)
      * [机器人夹爪搬运木块案例](demo/280ar_gripper.md)
      * [280Arduino 手柄遥控案例](demo/280AR_joy.md)
      * [机器人吸泵搬运木块案例](demo/280ar_pump.md)
      * [Mega2560-夹爪搬运木块](demo/280ar_mega2560_gripper.md)
      * [树莓派4B-Stag码视觉跟踪](demo/280ar_raspi4B_camera_flange.md)
      * [Jetson Xavier NX-物品分类案例](demo/280ar_jetsonxavier_pump.md)
    * [8. 配套资源](3-FunctionsAndApplications/8.SupportingResources/README.md)
        * [8.1 产品资料](3-FunctionsAndApplications/8.SupportingResources/8.1-ProductInformation/README.md)
        * [8.2 产品图纸](3-FunctionsAndApplications/8.SupportingResources/8.2-ProductDrawings/README.md)
        * [8.3 软件资料及源码](3-FunctionsAndApplications/8.SupportingResources/8.3-SoftwareInformationAndSourceCode/README.md)
        * [8.4 系统资料](3-FunctionsAndApplications/8.SupportingResources/8.4-SystemInformation/README.md)
        * [8.5 宣传资料](3-FunctionsAndApplications/8.SupportingResources/8.5-PromotionalMaterials/README.md)
* 支持与服务
    * [ 联系我们](4-SupportAndService/11.AboutUs/11.AboutUs.md)
    * [机械臂相关配件](4-SupportAndService/Accessories/accessories.md)
       * [平面底座](4-SupportAndService/Accessories/Flatbase.md)
       * [G型底座](4-SupportAndService/Accessories/Gstands_2.0.md)
       * [自适应夹爪](4-SupportAndService/Accessories/AdaptiveGripper.md)
       * [平行夹爪](4-SupportAndService/Accessories/ParallelGripper.md)
       * [柔性夹爪-张脚式](4-SupportAndService/Accessories/flexible_gripper_2.md) 
       * [垂直吸泵](4-SupportAndService/Accessories/pump.md)
       * [双头吸泵](4-SupportAndService/Accessories/doublepump.md)
       * [一体式吸泵](4-SupportAndService/Accessories/IntegratedPump.md)
       * [笔夹持器](4-SupportAndService/Accessories/penHolder.md)
       * [手机夹持器](4-SupportAndService/Accessories/phoneHolder.md)
       * [灵巧手](4-SupportAndService/Accessories/Robothand.md)
       * [USB相机](4-SupportAndService/Accessories/USBcamera.md)
       * [春笋法兰](4-SupportAndService/Accessories/bamboo.md)  
    * [致谢](5-Acknowledgments/5-Acknowledgments.md)
