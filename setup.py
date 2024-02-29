from setuptools import setup

setup(
    name='virgul',
    version=1,
    packages=['src/virgul'],
    setup_requires=['cffi'],
    cffi_modules=['build.py:ffibuilder'],
    install_requires=['cffi'],
    extras_require={ 'dev': [ 'pytest' ] }
)
