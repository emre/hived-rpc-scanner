from setuptools import setup

setup(
    name='hived_rpc_scanner',
    version='0.0.9',
    packages=["hived_rpc_scanner",],
    url='https://github.com/emre/hived-rpc-scanner',
    license='MIT',
    author='emre yilmaz',
    author_email='mail@emreyilmaz.me',
    description='A tool to check status of certain endpoints on Hived RPC',
    entry_points={
        'console_scripts': [
            'hived_rpc_scanner = hived_rpc_scanner.runner:runner',
        ],
    },
    install_requires=["prettytable==2.0.0", "httpx", "colored", "progressbar2"]
)