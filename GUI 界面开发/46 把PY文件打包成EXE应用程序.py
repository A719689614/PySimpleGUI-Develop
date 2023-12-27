"""
要将 Python 文件打包成可执行的 .exe 格式，可以使用第三方工具 pyinstaller。pyinstaller 可以将 Python 脚本及其所有依赖项打包为独立的可执行文件，使其可以在没有安装 Python 解释器的系统上运行。

下面是使用 pyinstaller 打包 Python 文件的一般步骤：

首先，确保你已经安装了 pyinstaller,你可以使用以下命令来安装它：

pip install pyinstaller
在命令行中切换到你的 Python 文件所在的目录。

使用以下命令将 Python 文件打包成可执行文件（.exe):

pyinstaller your_script.py
其中,your_script.py 是你要打包的 Python 文件的名称。

pyinstaller 将在当前目录下创建一个新的目录，其中包含打包后的可执行文件及其所有依赖项。可执行文件位于 dist 子目录中。

请注意,pyinstaller 会创建一个独立的可执行文件，该文件可能比 Python 脚本本身更大，因为它包含了 Python 解释器和所有依赖项。此外，打包过程可能因为脚本中使用的特定库或模块而稍有不同，你可能需要根据你的实际需求对 pyinstaller 的参数进行调整。

希望这可以帮助你将 Python 文件打包成可执行的 .exe 格式。"""





"""
在PyCharm中的终端输入:
第一步、安装打包组件：
pip3 install pysimplegui-exemaker
第二、起动打包程序：
python -m pysimplegui-exemaker.pysimplegui-exemaker
已完成！"""