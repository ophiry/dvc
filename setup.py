import platform
from setuptools import setup, find_packages
from distutils.errors import DistutilsPlatformError
from dvc import VERSION

install_requires = [
    'altgraph',
    'appdirs',
    'backports.shutil-get-terminal-size',
    'boto',
    'cachetools',
    'configparser',
    'decorator',
    'dill',
    'enum34',
    'fasteners',
    'funcsigs',
    'future',
    'futures',
    'gapic-google-cloud-datastore-v1',
    'gapic-google-cloud-error-reporting-v1beta1',
    'gapic-google-cloud-logging-v2',
    'gapic-google-cloud-pubsub-v1',
    'gapic-google-cloud-spanner-admin-database-v1',
    'gapic-google-cloud-spanner-admin-instance-v1',
    'gapic-google-cloud-spanner-v1',
    'gapic-google-cloud-speech-v1beta1',
    'gapic-google-cloud-vision-v1',
    'google-auth',
    'google-auth-httplib2',
    'google-cloud',
    'google-cloud-bigquery',
    'google-cloud-bigtable',
    'google-cloud-core',
    'google-cloud-datastore',
    'google-cloud-dns',
    'google-cloud-error-reporting',
    'google-cloud-language',
    'google-cloud-logging',
    'google-cloud-monitoring',
    'google-cloud-pubsub',
    'google-cloud-resource-manager',
    'google-cloud-runtimeconfig',
    'google-cloud-spanner',
    'google-cloud-speech',
    'google-cloud-storage',
    'google-cloud-translate',
    'google-cloud-vision',
    'google-gax',
    'googleapis-common-protos',
    'grpc-google-iam-v1',
    'grpcio',
    'httplib2',
    'ipython',
    'ipython-genutils',
    'macholib',
    'mock',
    'modulegraph',
    'monotonic',
    'nose',
    'oauth2client',
    'packaging',
    'pbr',
    'pexpect',
    'pickleshare',
    'ply',
    'prompt-toolkit',
    'proto-google-cloud-datastore-v1',
    'proto-google-cloud-error-reporting-v1beta1',
    'proto-google-cloud-logging-v2',
    'proto-google-cloud-pubsub-v1',
    'proto-google-cloud-spanner-admin-database-v1',
    'proto-google-cloud-spanner-admin-instance-v1',
    'proto-google-cloud-spanner-v1',
    'proto-google-cloud-speech-v1beta1',
    'proto-google-cloud-vision-v1',
    'protobuf',
    'ptyprocess',
    'pyasn1',
    'pyasn1-modules',
    'Pygments',
    'PyInstaller',
    'pyparsing',
    'requests',
    'rsa',
    'scandir',
    'simplegeneric',
    'six',
    'traitlets',
    'wcwidth',
    'colorama',
    'google-compute-engine'
]

if platform.system() == 'Darwin':
    install_requires.append('appnope')
    install_requires.append('py2app')

setup(
    name='dvc',
    version=VERSION,
    description='Data Version Control makes your data science projects reproducible and shareable.',
    author='Dmitry Petrov',
    author_email='dmitry@dataversioncontrol.com',
    url='https://github.com/dataversioncontrol/dvc.git',
    license='Apache License 2.0',
    install_requires=install_requires,
    keywords='data science, data version control, machine learning',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['bin', 'tests', 'functests']),
    include_package_data=True,
    download_url='http://dataversioncontrol.com',
    entry_points={
        'console_scripts': ['dvc = dvc.main:main']
    },
    zip_safe=False
)
