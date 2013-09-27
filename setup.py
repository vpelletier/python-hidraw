from setuptools import setup, find_packages

setup(
    name='hidraw-pure',
    description='Pure-python linux hidraw bindings',
    keywords='linux human interface device HID hidraw',
    version='1.1',
    author='Vincent Pelletier',
    author_email='plr.vincent@gmail.com',
    url='http://github.com/vpelletier/python-hidraw',
    license='GPL 2+',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
    ],
    install_requires=[
        'ioctl-opt',
    ],
)
