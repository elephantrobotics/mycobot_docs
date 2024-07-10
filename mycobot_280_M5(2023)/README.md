# myCobot 280 M5(2023版)
世界最小协作机器人    

核心文档
---

本文档包含从产品简介、详细的技术参数到用户须知和首次安装指导的全面信息。我们将深入解释myCobot 280 M5机械臂的基础功能，提供软件开发指南，并展示成功的应用案例，帮助您了解如何将myCobot 280 M5有效整合进各种应用中。此外，我们还提供了丰富的支持与服务信息，确保您在遇到任何技术挑战时能够获得必要的帮助。
### gitbook-en
英文版本: https://docs.elephantrobotics.com/docs/gitbook-en/2-serialproduct/2.1-280/2.1.1-M5.html
### gitbook-cn
中文版本:https://docs.elephantrobotics.com/docs/mycobot-m5-cn/2-serialproduct/2.1-280/2.1.6-M5-2023.html

文档说明
---

根据您的需求以及myCobot 280 M5应用程序开发的专业水平，您可以选择从头到尾遵循该顺序，或将其用作独立参考。您可以随时使用左侧的侧边栏导航跳转到任何部分，全文共分为以下五大板块：

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
* [产品信息](product-information/README.md)
    * [1. 产品简介](product-information/introduction.md)
        * [1.1 产品概述](product-information/overview.md)
        * [1.2 产品应用](product-information/application.md)
        * [1.3 支持的扩展开发](product-information/extended-development.md)
        * [1.4 购买地址](product-information/purchase.md)
    * [2. 产品参数](product-information/specifications.md)
        * [2.1 机器规格参数](product-information/machine-specs.md)
        * [2.2 控制核心参数](product-information/core-specs.md)
        * [2.3 结构尺寸参数](product-information/dimension-specs.md)
        * [2.4 电气特性参数](product-information/electrical-specs.md)
        * [2.5 笛卡尔坐标系](product-information/cartesian-coordinates.md)

* [基础设置](basic-settings/README.md)
    * [3. 用户须知](basic-settings/user-instructions.md)
        * [3.1 安全须知](basic-settings/safety-instructions.md)
        * [3.2 运输和储存](basic-settings/transport-storage.md)
        * [3.3 维护和保养](basic-settings/maintenance.md)
        * [3.4 常见问题解决](basic-settings/faq.md)
    * [4. 首次安装](basic-settings/initial-setup.md)
        * [4.1 产品标准清单](basic-settings/standard-list.md)
        * [4.2 产品开箱指南](basic-settings/unboxing-guide.md)
        * [4.3 开机检测指南](basic-settings/startup-check-guide.md)
        * [4.4 安装视频教程](basic-settings/installation-video.md)

* [功能与应用](features-applications/README.md)
    * [5. 基础功能](features-applications/basic-features.md)
        * [5.1 系统（功能）使用说明](features-applications/system-instructions.md)
        * [5.2 软件使用说明](features-applications/software-instructions.md)
        * [5.3 固件功能说明](features-applications/firmware-features.md)
    * [6. 软件开发指南](features-applications/development-guide.md)
        * [6.1 基于python开发使用](features-applications/python-development.md)
        * [6.2 基于ROS1 开发使用](features-applications/ros1-development.md)
        * [6.3 基于ROS2 开发使用](features-applications/ros2-development.md)
        * [6.8 基于通信协议包开发](features-applications/protocol-development.md)
    * [7. 成功案例](features-applications/success-stories.md)
    * [8. 配套资源](features-applications/supporting-resources.md)
        * [8.1 产品资料](features-applications/product-info.md)
        * [8.2 产品图纸](features-applications/product-drawings.md)
        * [8.3 软件资料及源码](features-applications/software-sources.md)
        * [8.4 系统资料](features-applications/system-info.md)
        * [8.5 宣传资料](features-applications/promotional-materials.md)

* [支持与服务](support-services/README.md)
    * [9. 故障排除](support-services/troubleshooting.md)
    * [10. 购买信息](support-services/purchasing-info.md)
    * [11. 关于我们](support-services/about-us.md)
        * [11.1 大象机器人](support-services/elephant-robotics.md)
        * [11.2 联系我们](support-services/contact-us.md)

* [致谢](acknowledgements.md)
