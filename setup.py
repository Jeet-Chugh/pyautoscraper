from setuptools import setup,find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='autoscraper',
    version='0.0.1',
    description="A lightweight module which automates webscraping with Python",
    long_description_content_type='text/markdown',
    long_description=open('README.md','r').read() + '\n\n' + open('changelog.txt','r').read(),
    url='https://github.com/Jeet-Chugh/pyautoscraper',
    author='Jeet Chugh',
    author_email='sunjeetchugh@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='pyautoscraper',
    package_dir={'pyautoscraper':'pyautoscraper'},
    packages=['pyautoscraper'],
    install_requires=['bs4','requests']
)
