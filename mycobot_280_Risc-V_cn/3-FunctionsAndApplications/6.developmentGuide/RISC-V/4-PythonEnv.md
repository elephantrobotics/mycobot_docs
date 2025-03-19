# Python环境和pip源设置

## **Python环境需求说明**

ROS2、Myblockly 和人工智能套件（Aikits）对 Python 环境的需求略有不同。为了避免环境冲突，建议按照以下方式配置 Python 环境：

**ROS2**：

- 通常工作在系统环境下，所需的 Python 依赖包也需要安装在系统环境中。
- 建议不要修改系统环境中的 Python 依赖包，以免影响 ROS2 的正常运行。

**Myblockly 和 Aikits**：

- 为了避免与系统环境冲突，建议为 Myblockly 和 Aikits 启用独立的虚拟环境。
- 虚拟环境可以隔离依赖包，确保不同软件之间的兼容性。

以下是 ROS2、Myblockly 和 Aikits 所需的 Python 依赖包：

| 软件            | Python依赖包                                                 |
| :-------------- | :----------------------------------------------------------- |
| ROS Humble      | pymycobot<=3.5.3                                             |
| Myblockly 1.5.8 | pymycobot== 3.6.8<br />opencv-python== 4.6.8.1<br />numpy==1.26.4 |
| Aikits          | pymycobot== 3.6.8<br />opencv-python == 4.6.8.1<br />numpy== 1.26.4<br />pyqt5== 5.15.11<br />pyserial== 3.5 <br />gpiozero== 2.0.3<br />matplotlib==3.10.0 |

> [!NOTE]
>
> - 如果使用基于Python脚本来控制机械臂，Python依赖包与Myblockly保持一致。
> - Python环境设置可参考 [Biabu OS Python用户指南](https://bianbu.spacemit.com/development/python)

## **Python环境设置**

### **ROS Humble**

ROS Humble 通常工作在系统环境下，因此需要将依赖包直接安装到系统环境中。使用以下命令安装 ：

```
pip install pymycobot==3.5.3 --break-system-packages
```

- `--break-system-packages`：该选项允许在系统环境中安装 Python 包，避免因权限问题导致的安装失败。

### Myblockly 1.5.8

启用虚拟环境：

```
sudo apt install python3-virtualenv 
virtualenv myblockly-venv
source myblockly-venv/bin/activate
```

安装依赖包：

```
pip3 install pymycobot==3.6.8
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple numpy==1.26.4
pip install --index-url https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple opencv-python==4.6.8.1
```

-  `--index-url` ：指定从spacemit pip源下载预编译好的python包。

### AiKits

启用虚拟环境：

```
sudo apt install python3-virtualenv 
virtualenv aikits-venv
source aikits-venv/bin/activate
```

安装依赖包：

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

## Python pip源设置

### 临时指定pip源

在安装 Python 包时，可以通过 `--index-url` 参数临时指定 Spacemit 的 pip 源：

```Bash
pip install numpy -i https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
```

这样只对当前的 `pip install` 命令生效，下次执行仍然会使用默认源（https://pypi.org/simple）。

### 修改默认pip源

如果需要永久修改默认 pip 源，可以按照以下步骤操作：

（1）创建或修改 pip 配置文件

```Bash
mkdir -p ~/.config/pip  # 确保目录存在
vim ~/.config/pip/pip.conf  # 编辑 pip 配置文件
```

（2）在文件中添加如下内容

```TOML
[global]
index-url = https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple
# 也可以添加其他源，当spacemit源没有时，从其他源获取
extra-index-url = https://pypi.tuna.tsinghua.edu.cn/simple  # spacemit源没有目标包时，从清华源获取
```

（3）验证是否生效

```Bash
pip config list
```

输出应该包含： 

```Plain
global.extra-index-url='https://pypi.tuna.tsinghua.edu.cn/simple'
global.index-url='https://git.spacemit.com/api/v4/projects/33/packages/pypi/simple'
```
