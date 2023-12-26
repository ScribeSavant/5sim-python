from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='5sim-python',
    version='1.0.4',
    description='A simple Python API for 5sim.net',
    long_description=open('README.md').read() + '\n\n',
    long_description_content_type='text/markdown',
    url='https://github.com/scribesavant/5sim-python',
    author='scribesavant',
    author_email='scribesavant@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='api 5sim',
    packages=find_packages(),
    install_requires=['requests']
)
