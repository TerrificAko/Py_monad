import os
from pathlib import Path

PROJECT_STRUCTURE = {
    "config": {
        "proxies.yaml": "# 代理IP池配置\nproxy_pools:\n  - type: socks5\n    servers: []\n",
        "rpc_nodes.yaml": "# RPC节点列表\nmonad:\n  - https://rpc.monad.xyz\n",
        "ads_profiles": {}
    },
    "src": {
        "core": {
            "web3_connector.py": """from web3 import Web3

class Web3Connector:
    def __init__(self, rpc_url):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        assert self.w3.is_connected(), "Failed to connect to RPC"
""",
            "wallet_manager.py": """from eth_account import Account

class WalletManager:
    @staticmethod
    def create():
        return Account.create()
""",
            "contract_interactor": {
                "ambient_finance.py": """class AmbientFinance:
    @staticmethod
    def add_liquidity(amount):
        pass
""",
                "monadverse_nft.py": """class MonadverseNFT:
    @staticmethod
    def mint():
        pass
"""
            }
        },
        "browser_control": {
            "ads_api.py": """import requests

class ADSController:
    API_ENDPOINT = 'http://localhost:50360/api/v1'
""",
            "metamask_automation.py": """from selenium import webdriver

class MetaMaskAutomator:
    def __init__(self, driver):
        self.driver = driver
""",
            "interaction_flow.py": """class InteractionFlow:
    def execute(self):
        pass
"""
        },
        "utils": {
            "fingerprint_tools.py": """# 指纹随机化生成器
def gen_fingerprint():
    pass
""",
            "ip_rotator.py": """# 代理IP轮换策略
class IPRotator:
    pass
""",
            "transaction_utils.py": """# 交易构造工具
def build_tx():
    pass
"""
        },
        "tasks": {
            "monad_daily.py": """from datetime import datetime

def daily_task():
    print(f"{datetime.now()} Starting daily task")
""",
            "cross_chain_task.py": """def cross_chain():
    pass
"""
        }
    },
    "tests": {
        "test_web3_connector.py": """import pytest

def test_connector():
    assert True
""",
        "test_metamask_flow.py": """def test_metamask():
    assert 1 + 1 == 2
""",
        "integration_test": {
            "__init__.py": ""
        }
    },
    "requirements.txt": """web3>=6.0
selenium>=4.10
eth-account>=0.9
python-dotenv>=1.0
""",
    "Dockerfile": """FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/tasks/monad_daily.py"]
""",
    "README.md": """# Monad Bot Project
Web3 interaction automation framework
"""
}


def create_project(root: Path, structure: dict):
    for name, content in structure.items():
        path = root / name

        if isinstance(content, dict):
            path.mkdir(exist_ok=True)
            create_project(path, content)
        else:
            if name.endswith(('.yaml', '.py', '.txt', '.md', 'Dockerfile')):
                path.parent.mkdir(exist_ok=True)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Created: {path.relative_to(root.parent)}")


if __name__ == "__main__":
    project_root = Path("../monad-bot")
    if project_root.exists():
        print(f"Error: Directory {project_root} already exists")
        exit(1)

    project_root.mkdir()
    try:
        create_project(project_root, PROJECT_STRUCTURE)
        print(f"\n✅ Project scaffold generated at: {project_root.absolute()}")
    except Exception as e:
        print(f"Error: {str(e)}")
        project_root.rmdir()
        exit(1)