# encoding: utf-8
from setuptools import setup, find_packages
from os import path

HERE = path.abspath(path.dirname(__file__))

__version__ = "0.1.0"
PACKAGE_NAME = "arxan_isign"

setup(
    name=PACKAGE_NAME,
    version=__version__,
    description='Re-signing iOS apps without Apple tools',
    url='https://github.com/saucelabs/{}'.format(PACKAGE_NAME),
    download_url='https://github.com/saucelabs/{}/tarball/v{}'.format(PACKAGE_NAME, __version__),
    author='Sauce Labs',
    author_email='dev@saucelabs.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=['ios', 'app', 'signature', 'codesign', 'sign', 'resign'],
    packages=find_packages(),
    install_requires=[
        'biplist==1.0.3',
        'construct==2.9.45',
        'memoizer==0.0.1',
        'pyOpenSSL==18.0.0',
    ],
    package_data={
        'isign': ['apple_credentials/applecerts.pem',
                  'code_resources_template.xml',
                  'version.json'],
    },
    scripts=['bin/isign',
             'bin/multisign',
             'bin/isign_export_creds.sh',
             'bin/isign_guess_mobileprovision.sh']
)
