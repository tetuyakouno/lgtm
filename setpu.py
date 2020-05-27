from setuptools import find_packages, setup

setup(
    name='lgtm',
    version='1.0.0',
    packages=find_packages(exclude=('test' ,)),
    install_requires=[
        'Click~=7.0',
        'Pilow~=6.2.0',
        'requests~=2.22.0',
    ],
    entry_points={
        'console_scripts': [
            'ltgm=ltgm_exe.core:cli'
        ]
    }
)
