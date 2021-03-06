from setuptools import setup
import re


def extract_version(filename):
    contents = open(filename).read()
    match = re.search('^__version__\s+=\s+[\'"](.*)[\'"]\s*$', contents, re.MULTILINE)
    if match is not None:
        return match.group(1)

setup(
    name="bigsuds",
    version=extract_version('bigsuds.py'),
    description='Library for F5 Networks iControl API',
    license='https://devcentral.f5.com/resources/devcentral-eula',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='f5 icontrol',
    author='F5 Networks, Inc.',
    author_email='devcentral@f5.com',
    url='http://devcentral.f5.com',
    install_requires=['suds-jurko>=0.4'],
    py_modules=['bigsuds'],
    test_suite='nose.collector',
    tests_require=['nose', 'mock', 'mox'],
)
