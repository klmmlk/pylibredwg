from setuptools import setup, Extension
import os

# 指定编译输出路径
build_dir = "build"

# 配置扩展模块
ext_modules = [
    Extension(
        name="libredwg",
        sources=[os.path.join(build_dir, "src/libredwg.c")],
        include_dirs=[os.path.join(build_dir, "include")],
        library_dirs=[os.path.join(build_dir, "lib")],
        libraries=["redwg"],
    )
]

setup(
    name="libredwg",
    version="0.1.0",
    ext_modules=ext_modules,
)
