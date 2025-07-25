# myCobot 280 For Arduino(2023)
Algorithm Verification Practice Teaching

Core Document
---

This document contains comprehensive information from product introduction, detailed technical parameters to user instructions and product development guidance. The document will introduce the basic functions of the myCobot 280 For Arduino robot arm in depth, provide a software development guide, and show successful application cases to help you understand how to effectively integrate myCobot 280 For Arduino into various applications. In addition, we also provide a wealth of support and service information to ensure that you can get the necessary help when you encounter any technical challenges.


Document Description
---

Depending on your needs and your level of expertise in myCobot 280 For Arduino application development, you can choose to follow this order from beginning to end or use it as a standalone reference. You can always use the sidebar navigation on the left to jump to any part of this document. The full text is divided into the following five sections:

#### Product Information
The product information section will provide you with a basic overview of the robot arm, including detailed technical specifications such as main functions, product parameters and electrical characteristics, to help you quickly understand the basic characteristics and usage environment of the product. In addition, this section will detail the application examples and supported extension development of the product, providing you with the necessary development guides and resources. At the end of the article, relevant purchase links and channels will be given to facilitate your purchase.

#### Basic Settings
This section is an important part that every user of this product must read carefully. It covers key information about product use, transportation, storage and maintenance, aiming to ensure the safety and efficiency of users when operating the product. In addition, this section also details the division of responsibilities for product failure or damage that may occur due to failure to follow these guidelines.

#### Functions and Applications
The Functions and Applications section details the basic functions of the robot arm and how to use the software, including system instructions and firmware functions. The Software Development Guide provides guidance based on different development environments, such as Python and ROS, to support technical developers to expand applications. By showing successful application cases and providing supporting resources, it provides you with practical references and necessary support materials for a deeper understanding and use of the product.

#### Support and Services
The Support and Services section will provide you with comprehensive troubleshooting guides and post-purchase service information, such as warranty and service terms, to help you quickly resolve problems when you encounter them, and ensure that you understand your rights and obligations after purchase. In addition, the 'About Us' section strengthens the user's understanding of the design and manufacturer of the myCobot series products, aiming to build trust and brand loyalty.

#### Acknowledgements
We really appreciate you taking the time to read the myCobot 280 For Arduino User Manual. We hope this document will help you better understand and effectively use this robot, thereby inspiring your creativity. If you have any questions or need further assistance, please feel free to contact our customer support team. We look forward to seeing your innovative projects using myCobot 280 For Arduino and welcome you to join our fast-growing developer community.

Document Directory

---

# Summary
* [Introduction](README.md)
* Product Information
   * [1. Product Introduction](1-ProductInformation/1.ProductIntroduction/1-ProductIntroduction.md)
   * [2. Product Parameters](1-ProductInformation/2.ProductParameter/2-ProductParameters.md)
* Basic Settings
   * [3. User Notice](2-BasicSettings/3.UserNotice/3-UserInstructions.md)
   * [4. First Time Installation](2-BasicSettings/4.FirstTimeInstallation/4-FirstTimeInstallation.md)
      * [4.1 First-time self-check](4-SupportAndService/9.Troubleshooting/9.4-first-time-self-check.md)
      * [4.2 Software issues](4-SupportAndService/9.Troubleshooting/9.2-software.md)
      * [4.3 Hardware issues](4-SupportAndService/9.Troubleshooting/9.3-hardware.md)
      * [4.4 Accessories issues](4-SupportAndService/9.Troubleshooting/9.1-accessories.md)
      * [4.5 Others](4-SupportAndService/9.Troubleshooting/9.0-other.md)
* Functions and applications
   * [5. Basic functions](3-FunctionsAndApplications/5.BasicFunction/README.md)
     * [5.1 Introduction to the use of the robotic arm system](3-FunctionsAndApplications/5.BasicFunction/5.1-Functionlnstruction/DevelopmEntenvironment.md)
     * [5.2 myStudio instructions](3-FunctionsAndApplications/5.BasicFunction/5.2-Softwarelnstructions/README.md)
     * [5.3 Hardware Interface](3-FunctionsAndApplications/5.BasicFunction/5.3-FirmwareFunctionDescription/
     RoboticArmElectricalInterface.md)
     * [5.4 PID control](3-FunctionsAndApplications/5.BasicFunction/5.4-RobotPrecisionControl/README.md)
   * [6. Software Development Guide](3-FunctionsAndApplications/6.developmentGuide/README.md)
     * [6.1 Development and Use Based on Arduino](3-FunctionsAndApplications/6.developmentGuide/Arduino/README.md)
       * [6.1.1 Environment Construction](3-FunctionsAndApplications/6.developmentGuide/Arduino/10.1-arduino_download.md)
       * [6.1.2 Simple Use](3-FunctionsAndApplications/6.developmentGuide/Arduino/10.2-arduino_use.md)
       * [6.1.3 API description](3-FunctionsAndApplications/6.developmentGuide/Arduino/10.3-api.md)
     * [6.2 Development and use based on Python](3-FunctionsAndApplications/6.developmentGuide/python/README.md)
       * [6.2.1 Environment construction](3-FunctionsAndApplications/6.developmentGuide/python/1_download.md)
       * [6.2.2 API description](3-FunctionsAndApplications/6.developmentGuide/python/2_API.md)
       * [6.2.3 Joint control](3-FunctionsAndApplications/6.developmentGuide/python/3_angle.md)
       * [6.2.4 Coordinate Control](3-FunctionsAndApplications/6.developmentGuide/python/4_coord.md)
       * [6.2.5 IO Control](3-FunctionsAndApplications/6.developmentGuide/python/5_IO.md)
       * [6.2.6 Gripper Control](3-FunctionsAndApplications/6.developmentGuide/python/6_gripper.md)
       * [6.2.7 Handle Control](3-FunctionsAndApplications/6.developmentGuide/python/9_HandleControl.md)
       * [6.2.8 Drawing Patterns](3-FunctionsAndApplications/6.developmentGuide/python/15_280_gcode_draw.md)
       * [6.2.9 Demonstration Code and Video](3-FunctionsAndApplications/6.developmentGuide/python/8_example.md)
     * [6.3 Development and Use Based on ROS1](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.1-Introduction.md)
       * [6.3.1 ROS1 Environment Building](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.2-EnvironmentBuilding.md)
       * [6.3.2 ROS1 Basics](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.3-ROS_Basics.md)
       * [6.3.3 rivz Introduction and Use](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.4-rivzIntroductionAndUse/README.md)
       * [6.3.4 Moveit Introduction and Use](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.5-Moveit/README.md)
     * [6.4 Development and Use Based on ROS2](3-FunctionsAndApplications/6.developmentGuide/ROS/12.2-ROS2/12.2.3-ROS2Introduction.md)
       * [6.4.1 ROS2 environment installation](3-FunctionsAndApplications/6.developmentGuide/ROS/12.2-ROS2/12.2.1-InstallationOfROS2.md)
       * [6.4.2 ROS2 basics](3-FunctionsAndApplications/6.developmentGuide/ROS/12.2-ROS2/12.2.2-BasicTutorial.md)
       * [6.4.3 rivz introduction and use](3-FunctionsAndApplications/6.developmentGuide/ROS/12.2-ROS2/12.2.4-rivzIntroductionAndUse/README.md)
       * [6.4.4 Moveit2 Introduction and Use](3-FunctionsAndApplications/6.developmentGuide/ROS/12.2-ROS2/12.2.5-Moveit2/README.md)
     * [6.5 Development and use based on Blockly](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/README.md)
       * [6.5.1 Initial use of myBlockly](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.1-myBlocklyFirstUse.md)
       * [6.5.2 Control RGB light board](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.2-ControlRGB.md)
       * [6.5.3 Control the robotic arm to return to the origin](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.3-ControlRoboticArmBackZero.md)
       * [6.5.4 Control single joint motion](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.4-ControlSingleJoint.md)
       * [6.5.5 Control multiple joints](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.5-ControlSinglesJoint.md)
       * [6.5.6 Control the left and right swing of the robotic arm](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.6-ControlRoboticSwingLeft&Right.md)
       * [6.5.7 Control Robotic Arm Dance](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.7-ControlRoboticArmDance.md)
       * [6.5.8 Gripper Usage](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.8-GripperUse.md)
       * [6.5.9 Pump Usage](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.9-PumpUse.md)
       * [6.5.10 Gripper Test](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.13-gripperTest.md)
       * [6.5.11 IO Test](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.14-ioTest.md)
       * [6.5.12Q&A](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.10Q&A.md)
     * [6.6 Development and use based on serial communication protocol](3-FunctionsAndApplications/6.developmentGuide/CommunicationProtocolPackage/18-communication.md)
   * [7. Successful Cases](3-FunctionsAndApplications/7.SuccessfulCase/7-SuccessfulCases.md)
     * [Robot gripper carrying wooden block example](demo-en/280ar_gripper.md)
     * [280Arduino handle remote control box](./demo-en/280AR_joy_EN.md)
     * [Robot suction pump to carry wooden blocks](demo-en/280ar_pump.md)
     * [Mega2560-gripper to carry wood blocks](demo/280ar_mega2560_gripper.md)
     * [Raspberry Pi 4B-Stag code visual tracking](demo/280ar_raspi4B_camera_flange.md)
     * [Jetson Xavier NX-item classification example](demo/280ar_jetsonxavier_pump.md)
   * [8. Supporting Resources](3-FunctionsAndApplications/8.SupportingResources/README.md)
     * [8.1 Product Information](3-FunctionsAndApplications/8.SupportingResources/8.1-ProductInformation/README.md)
     * [8.2 Product Drawings](3-FunctionsAndApplications/8.SupportingResources/8.2-ProductDrawings/README.md)
     * [8.3 Software Information and Source Code](3-FunctionsAndApplications/8.SupportingResources/8.3-SoftwareInformationAndSourceCode/README.md)
     * [8.4 System Information](3-FunctionsAndApplications/8.SupportingResources/8.4-SystemInformation/README.md)
     * [8.5 Promotional Materials](3-FunctionsAndApplications/8.SupportingResources/8.5-PromotionalMaterials/README.md)
* Support and Service
   * [ Contact Us](4-SupportAndService/11.AboutUs/11.AboutUs.md)
   * [Robot Arm Accessories](4-SupportAndService/Accessories/accessories.md)
     * [Flat Base](4-SupportAndService/Accessories/Flatbase.md)
     * [G-Stand](4-SupportAndService/Accessories/Gstands_2.0.md)
     * [Adaptive Gripper](4-SupportAndService/Accessories/AdaptiveGripper.md)
     * [Parallel Gripper](4-SupportAndService/Accessories/ParallelGripper.md)
     * [Flexible Gripper - Open Leg Type](4-SupportAndService/Accessories/flexible_gripper_2.md)
     * [Vertical Suction Pump](4-SupportAndService/Accessories/pump.md)
     * [Double-head suction pump](4-SupportAndService/Accessories/doublepump.md)
     * [Integrated suction pump](4-SupportAndService/Accessories/IntegratedPump.md)
     * [Pen holder](4-SupportAndService/Accessories/penHolder.md)
     * [Phone holder](4-SupportAndService/Accessories/phoneHolder.md)
     * [Dexterous hand](4-SupportAndService/Accessories/Robothand.md)
     * [USB camera](4-SupportAndService/Accessories/USBcamera.md)
     * [Bamboo flange](4-SupportAndService/Accessories/bamboo.md)
   * [Acknowledgments](5-Acknowledgments/5-Acknowledgments.md)