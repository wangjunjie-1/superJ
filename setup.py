from setuptools import setup, find_packages

# 使用__version__变量来管理版本号，通常在package内部定义
from superJ import __version__

setup(
    # 包的名称
    name='superJ',

    # 包的版本号
    version=__version__,
    
    # 包的作者
    author='Wang junjie',

    # 作者的联系邮箱
    author_email='wangjunjie@visionular.com',

    # 包的简短描述
    description='A set of common tools used in daily work.',

    # 长描述，通常从README.md文件读取
    long_description=open('README.md').read(),
    
    # 包的URL
    url='https://github.com/yourusername/mypackage',

    # 包的许可证
    license='MIT',

    # 包支持的Python版本
    python_requires='>=3.8',

    install_requires=[
        'click>=8.1.1',
        'onnx>=1.16.2',
        'onnx-simplifier>=0.4.20',
        'onnxruntime>=1.16.1',
        # 'onnxruntime-gpu>=1.16.1',
    ],
    # 包含的包和模块
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'show=superJ.onnx.onnxkit:onnx_show',
            'check=superJ.onnx.onnxkit:onnx_check',
        ],
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],


)