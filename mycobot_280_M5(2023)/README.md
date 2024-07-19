# myCobot 280 M5(2023版)
世界最小协作机器人    

核心文档
---

本文档包含从产品简介、详细的技术参数到用户须知和产品开发指导的全面信息。文档将深入介绍myCobot 280 M5机械臂的基础功能，并提供软件开发指南，展示成功的应用案例，帮助您了解如何将myCobot 280 M5有效整合进各种应用中。此外，我们还提供了丰富的支持与服务信息，确保您在遇到任何技术挑战时能够获得必要的帮助。
### gitbook-en
英文版本: https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.1-280/2.1.1-M5.html
### gitbook-cn
中文版本:https://docs.elephantrobotics.com/docs/mycobot-m5-cn/2-serialproduct/2.1-280/2.1.6-M5-2023.html

文档说明
---

根据您的需求以及myCobot 280 M5应用程序开发的专业水平，您可以选择从头到尾遵循该顺序进行阅读，或将其用作独立参考。您可以随时使用左侧的侧边栏导航跳转到本文档的任何部分，全文共分为以下五大板块：

#### 产品信息
产品信息板块将为您提供机械臂的基本概述，包括主要功能、产品参数和电气特性等详细的技术规格，帮助您快速了解产品的基本特性和使用环境。此外，这一部分将详细介绍产品的应用实例和支持的扩展开发，为您提供必要的开发指南和资源。文末将给出相关购买链接和渠道，方便您进行购买。

#### 基础设置
本章节是使用本产品的每一位用户必须仔细阅读的重要部分。它涵盖了关于产品使用、运输、储存及维护的关键须知，旨在确保用户在操作产品时的安全性和效率。此外，本章节也详细说明了因未遵循这些指南而可能导致的产品故障或损害的责任划分。

#### 功能与应用
功能与应用板块详细介绍了机械臂的基础功能和软件使用方法，包括系统使用说明和固件功能。软件开发指南提供了基于不同开发环境的指导，如Python和ROS，支持技术开发者进行应用扩展。通过展示成功的应用案例和提供配套资源，为您提供实践参考和必要的支持材料，以便更深入地了解和使用产品。

#### 支持与服务
支持与服务板块将为您提供全面的故障排除指南和购买后的服务信息，如保修和服务条款，帮助您在遇到问题时能够快速解决，并确保您了解购买后的权利和义务。此外，'关于我们'部分加强了用户对myCobot 系列产品设计及制造商的了解，旨在建立信任和品牌忠诚。

#### 致谢
我们非常感谢您花时间阅读myCobot 280 M5 用户手册。我们希望本文档能够帮助您更好地了解并有效使用这款机器人，从而激发您的创造力。如果您有任何疑问或需要进一步帮助，请随时联系我们的客户支持团队。我们期待看到您使用 myCobot 280 M5完成创新项目，并欢迎您加入我们快速发展的开发者社区。


文档目录  

---

# Summary
* * 产品信息
    * [1. 产品简介](1-ProductInformation/1.ProductIntroduction/1-ProductIntroduction.md)

    * [2. 产品参数](1-ProductInformation/2.ProductParameter/2-ProductParameters.md)

* 基础设置
    * [3. 用户须知](2-BasicSettings/3.UserNotice/3-UserInstructions.md)

    * [4. 首次安装](2-BasicSettings/4.FirstTimeInstallation/4-FirstTimeInstallation.md)

* 功能与应用
    * [5. 基础功能](3-FunctionsAndApplications/5.BasicFunction/README.md)
        * [5.1 系统（功能）使用说明](3-FunctionsAndApplications/5.BasicFunction/5.1-Functionlnstruction/README.md)
        * [5.2 软件使用说明](3-FunctionsAndApplications/5.BasicFunction/5.2-Softwarelnstructions/README.md)
        * [5.3 固件功能说明](3-FunctionsAndApplications/5.BasicFunction/5.3-FirmwareFunctionDescription/README.md)
    * [6. 软件开发指南](3-FunctionsAndApplications/6.developmentGuide/README.md)
        * [6.1 基于python开发使用](3-FunctionsAndApplications/6.developmentGuide/python/README.md)
        * [6.2 基于ROS1 开发使用](3-FunctionsAndApplications/6.developmentGuide/ROS/README.md)
        * [6.3 基于ROS2 开发使用](3-FunctionsAndApplications/6.developmentGuide/ROS/README.md)
        * [6.4 基于Blockly 开发使用](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/README.md)
        * [6.5 基于C++ 开发使用](3-FunctionsAndApplications/6.developmentGuide/C++/README.md)
        * [6.6 基于C# 开发使用](3-FunctionsAndApplications/6.developmentGuide/C#/README.md)
        * [6.7 基于Arduino 开发使用](3-FunctionsAndApplications/6.developmentGuide/Arduino/README.md)
        * [6.8 基于JavaScript开发使用](3-FunctionsAndApplications/6.developmentGuide/JavaScript/README.md)
        * [6.9 基于串口通信协议开发使用](3-FunctionsAndApplications/6.developmentGuide/CommunicationProtocolPackage/18-communication.md)
    * [7. 成功案例](3-FunctionsAndApplications/7.SuccessfulCase/7-SuccessfulCases.md)
    * [8. 配套资源](3-FunctionsAndApplications/8.SupportingResources/README.md)
        * [8.1 产品资料](3-FunctionsAndApplications/8.SupportingResources/8.1-ProductInformation/README.md)
        * [8.2 产品图纸](3-FunctionsAndApplications/8.SupportingResources/8.2-ProductDrawings/README.md)
        * [8.3 软件资料及源码](3-FunctionsAndApplications/8.SupportingResources/8.3-SoftwareInformationAndSourceCode/README.md)
        * [8.4 系统资料](3-FunctionsAndApplications\8.SupportingResources\8.4-SystemInformation/README.md)
        * [8.5 宣传资料](3-FunctionsAndApplications\8.SupportingResources\8.5-PromotionalMaterials/README.md)

* 支持与服务
       * [联系我们](4-SupportAndService/11.AboutUs/11.AboutUs.md)
* [致谢](5-Acknowledgments/5-Acknowledgments.md)
