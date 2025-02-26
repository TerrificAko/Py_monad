from setuptools import setup, find_packages

setup(
    name="monad-bot",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
         "web3>=6.0           "
        ,"selenium>=4.10      "
        ,"eth-account>=0.9    "
        ,"python-dotenv>=1.0  "
        ,"pandas>=1.3.0       "
        ,"openpyxl>=3.0.0     "
        ,"mnemonic>=0.20      "
    ],
)