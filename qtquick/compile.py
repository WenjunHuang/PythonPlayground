from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("cpu", ["cpu_load.py"])
]

setup(
    name='cpu',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
