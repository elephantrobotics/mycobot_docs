# myCobot 280 JN (2023)
The world's smallest collaborative robot

Core Document
---
This document contains comprehensive information from product introduction, detailed technical parameters to user instructions and product development guidance. The document will introduce the basic functions of the myCobot 280 JN robot arm in depth, provide software development guidelines, and show successful application cases to help you understand how to effectively integrate myCobot 280 JN into various applications. In addition, we also provide a wealth of support and service information to ensure that you can get the necessary help when you encounter any technical challenges.

Document Description
---

Depending on your needs and your level of expertise in myCobot 280 JN application development, you can choose to follow this order from beginning to end or use it as a standalone reference. You can always use the sidebar navigation on the left to jump to any part of this document. The full text is divided into the following five sections:

#### Product Information
The product information section will provide you with a basic overview of the robot arm, including detailed technical specifications such as main functions, product parameters and electrical characteristics, to help you quickly understand the basic characteristics and usage environment of the product. In addition, this section will detail the product's application examples and supported extension development, providing you with the necessary development guides and resources. At the end of the article, relevant purchase links and channels will be given to facilitate your purchase.

#### Basic Settings
This section is an important part that every user of this product must read carefully. It covers key information about product use, transportation, storage and maintenance, aiming to ensure the safety and efficiency of users when operating the product. In addition, this section also details the division of responsibilities for product failure or damage that may occur due to failure to follow these guidelines.

#### Functions and Applications
The Functions and Applications section details the basic functions of the robot arm and how to use the software, including system instructions and firmware functions. The Software Development Guide provides guidance based on different development environments, such as Python and ROS, to support technical developers to expand applications. By showing successful application cases and providing supporting resources, it provides you with practical references and necessary support materials for a deeper understanding and use of the product.

#### Support and Services
The Support and Services section will provide you with comprehensive troubleshooting guides and post-purchase service information, such as warranty and service terms, to help you quickly resolve problems when you encounter them, and ensure that you understand your rights and obligations after purchase. In addition, the 'About Us' section strengthens the user's understanding of the design and manufacturer of the myCobot series products, aiming to build trust and brand loyalty.

#### Acknowledgements
We appreciate your taking the time to read the myCobot 280 JN User Manual. We hope this document will help you better understand and effectively use this robot, thereby inspiring your creativity. If you have any questions or need further assistance, please feel free to contact our customer support team. We look forward to seeing the innovative projects you complete with myCobot 280 JN and welcome you to join our fast-growing developer community.

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
      * [5.1 Introduction to the use of the robotic arm system](3-FunctionsAndApplications/5.BasicFunction/5.1-Functionlnstruction/README.md)
      * [5.2 System basic function description](3-FunctionsAndApplications/5.BasicFunction/5.2-Softwarelnstructions/3.5.2-SW-detail-description.md)
      * [5.3 Firmware Function Description](3-FunctionsAndApplications/5.BasicFunction/5.3-FirmwareFunctionDescription/3.5.3-HW-description-JN.md)
      * [5.4 myStudio Introduction](3-FunctionsAndApplications/5.BasicFunction/5.2-Softwarelnstructions/README.md)
      * [5.5 TF card replacement tutorial and burning image](3-FunctionsAndApplications/5.BasicFunction/5.4-TFcard/tfcard.md)
   * [6. Software Development Guide](3-FunctionsAndApplications/6.developmentGuide/README.md)
      * [6.1 Development  based on python](3-FunctionsAndApplications/6.developmentGuide/python/README.md)
        * [6.1.1 Environment Construction](3-FunctionsAndApplications/6.developmentGuide/python/1_download.md)
        * [6.1.2 API Description](3-FunctionsAndApplications/6.developmentGuide/python/2_API.md)
        * [6.1.3 Joint Control](3-FunctionsAndApplications/6.developmentGuide/python/3_angle.md)
        * [6.1.4 Coordinate Control](3-FunctionsAndApplications/6.developmentGuide/python/4_coord.md)
        * [6.1.5 IO Control](3-FunctionsAndApplications/6.developmentGuide/python/5_IO.md)
        * [6.1.6 Gripper Control](3-FunctionsAndApplications/6.developmentGuide/python/6_gripper.md)
        * [6.1.7 TCP&IP](3-FunctionsAndApplications/6.developmentGuide/python/7_TCPIP.md)
        * [6.1.8 Handle Control](3-FunctionsAndApplications/6.developmentGuide/python/9_HandleControl.md)
        * [6.1.9 Drawing Patterns](3-FunctionsAndApplications/6.developmentGuide/python/15_280_gcode_draw.md)
        * [6.1.10 Demonstration Code](3-FunctionsAndApplications/6.developmentGuide/python/8_example.md)
      * [6.2 Development  Based on ROS1](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.1-Introduction.md)
        * [6.2.1 ROS1 Environment Building](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.2-EnvironmentBuilding.md)
        * [6.2.2 ROS1 Basics](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.3-ROS_Basics.md)
        * [6.2.3 rivz Introduction and Use](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.4-rivzIntroductionAndUse/README.md)
        * [6.2.4 Moveit Introduction and Use](3-FunctionsAndApplications/6.developmentGuide/ROS/12.1-ROS1/12.1.5-Moveit/README.md)
      * [6.3 Development  based on ROS2](3-FunctionsAndApplications/6.developmentGuide/ROS/12.2-ROS2/12.2.3-ROS2Introduction.md)
        * [6.3.1 ROS2 environment construction](3-FunctionsAndApplications/6.developmentGuide/ROS/12.2-ROS2/12.2.1-InstallationOfROS2.md)
        * [6.3.2 ROS2 basics](3-FunctionsAndApplications/6.developmentGuide/ROS/12.2-ROS2/12.2.2-BasicTutorial.md)
        * [6.3.3 rivz Introduction and Use](3-FunctionsAndApplications/6.developmentGuide/ROS/12.2-ROS2/12.2.4-rivzIntroductionAndUse/README.md)
      * [6.4 Development  Based on Blockly](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/README.md)
        * [6.4.1 Initial Use of myBlockly](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.1-myBlocklyFirstUse.md)
        * [6.4.2 Control RGB Light Board](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.2-ControlRGB.md)
        * [6.4.3 Control the robot arm back to the origin](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.3-ControlRoboticArmBackZero.md)
        * [6.4.4 Control single joint motion](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.4-ControlSingleJoint.md)
        * [6.4.5 Control multiple joints](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.5-ControlSinglesJoint.md)
        * [6.4.6 Control the robot arm to swing left and right](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.6-ControlRoboticSwingLeft&Right.md)
        * [6.4.7 Control the robot arm to dance](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.7-ControlRoboticArmDance.md)
        * [6.4.8 Use of gripper](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.8-GripperUse.md)
        * [6.4.9 Pump Usage](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.9-PumpUse.md)
        * [6.4.10 Gripper Test](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.13-gripperTest.md)
        * [6.4.11 IO test](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.14-ioTest.md)
        * [6.4.12Q&A](3-FunctionsAndApplications/6.developmentGuide/myBlocklyAndUlFlow/myblocklyTutorials/5.1.10Q&A.md)
     * [6.5 Development based on serial communication protocol](3-FunctionsAndApplications/6.developmentGuide/CommunicationProtocolPackage/18-communication.md)
   * [7. Successful case](3-FunctionsAndApplications/7.SuccessfulCase/7-SuccessfulCases.md)
   * [8. Supporting Resources](3-FunctionsAndApplications/8.SupportingResources/README.md)
     * [8.1 Product Information](3-FunctionsAndApplications/8.SupportingResources/8.1-ProductInformation/README.md)
     * [8.2 Product Drawings](3-FunctionsAndApplications/8.SupportingResources/8.2-ProductDrawings/README.md)
     * [8.3 Software Information and Source Code](3-FunctionsAndApplications/8.SupportingResources/8.3-SoftwareInformationAndSourceCode/README.md)
     * [8.4 System Information](3-FunctionsAndApplications/8.SupportingResources/8.4-SystemInformation/README.md)
     * [8.5 Promotional Materials](3-FunctionsAndApplications/8.SupportingResources/8.5-PromotionalMaterials/README.md)
* Support and Services
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
   * [ Acknowledgments](5-Acknowledgments/5-Acknowledgments.md)