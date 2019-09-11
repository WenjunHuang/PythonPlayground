from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("mymodel1", ["simple.py"])
]

setup(
    name='MyProgram',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
