# Python environment and pip source settings

## **Python environment requirements**

ROS2, Myblockly, and AI Kits (Aikits) have slightly different requirements for Python environments. To avoid environment conflicts, it is recommended to configure the Python environment as follows:

**ROS2**:

- Usually working in the system environment, the required Python dependency packages also need to be installed in the system environment.

- It is recommended not to modify the Python dependency packages in the system environment to avoid affecting the normal operation of ROS2.

**Myblockly and Aikits**:

- To avoid conflicts with the system environment, it is recommended to enable independent virtual environments for Myblockly and Aikits.

- The virtual environment can isolate dependency packages to ensure compatibility between different software.

The following are the Python dependencies required by ROS2, Myblockly, and Aikits:

| Software | Python dependencies |
| :---------- | :------------------------------------------- |
| ROS Humble | pymycobot<=3.5.3 |
| Myblockly 1.5.8 | pymycobot== 3.6.8<br />opencv-python== 4.6.8.1<br />numpy==1.26.4 |
| Aikits | pymycobot== 3.6.8<br />opencv-python == 4.6.8.1<br />numpy== 1.26.4<br />pyqt5== 5.15.11<br />pyserial== 3.5 <br />gpiozero== 2.0.3<br />matplotlib==3.10.0 |

> [!NOTE]
>
> - If you use Python scripts to control the robot, the Python dependency package is the same as Myblockly.
> - For Python environment settings, refer to [Biabu OS Python User Guide](https://bianbu.spacemit.com/development/python)

## **Python Environment Settings**

### **ROS Humble**

ROS Humble usually works in the system environment, so the dependency packages need to be installed directly into the system environment. Use the following command to install:

```
pip install pymycobot==3.5.3 --break-system-packages
```

- `--break-system-packages`: This option allows Python packages to be installed in the system environment to avoid installation failures due to permission issues.

### Myblockly 1.5.8

Enable virtual environment:

```
sudo apt install python3-virtualenv
virtualenv myblockly-venv
source myblockly-venv/bin/activate
```

Install dependent packages:

```
pip3 install pymycobot==3.6.8
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple numpy==1.26.4
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple opencv-python==4.6.8.1
```

- `--index-url` : Specify to download precompiled python packages from the spacemit pip source.

### AiKits

Enable virtual environment:

```
sudo apt install python3-virtualenv
virtualenv aikits-venv
source aikits-venv/bin/activate
```

Install dependent packages:

```
sudo apt install libopenblas-dev

pip3 install pymycobot==3.6.8
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple numpy==1.26.4
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple opencv-python==4.6.8.1
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple pyqt5==5.15.11
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple pyserial==3.5
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple gpiozero==2.0.3
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple matplotlib==3.10.0
```

## Python pip source settings

### Temporarily specify pip source

When installing Python packages, you can temporarily specify the pip source of Spacemit through the `--index-url` parameter:

```Bash
pip install numpy -i https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
```
This will only work for the current `pip install` command. The default source (https://pypi.org/simple) will still be used next time you execute it.

### Modify the default pip source

If you need to permanently modify the default pip source, you can follow the steps below:

(1) Create or modify the pip configuration file

```Bash
mkdir -p ~/.config/pip # Make sure the directory exists
vim ~/.config/pip/pip.conf # Edit the pip configuration file
```

(2) Add the following content to the file

```TOML
[global]
index-url = https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
# You can also add other sources. When the spacemit source does not have it, get it from other sources
extra-index-url = https://pypi.tuna.tsinghua.edu.cn/simple # When the spacemit source does not have the target package, get it from the Tsinghua source
```

(3) Verify whether it works

```Bash
pip config list
```

The output should contain:

```bash
global.extra-index-url='https://pypi.tuna.tsinghua.edu.cn/simple'
global.index-url='https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple'
```