from setuptools import setup, Extension
import os

# 配置扩展模块
ext_modules = [
    Extension(
        name="libredwg",
        sources=["bindings/python/swig_python.c"],  # 修改为实际路径
        include_dirs=["include"],  # 头文件目录
        library_dirs=["lib"],  # 库文件目录
        libraries=["redwg"],  # 依赖的库
    )
]

setup(
    name="libredwg",
    version="0.1.0",
    ext_modules=ext_modules,
)
