from eth_account import Account
from mnemonic import Mnemonic
from pathlib import Path
import pandas as pd
from typing import List, Dict

class WalletManager:
    @staticmethod
    def create() -> Dict[str, str]:
        """创建单个钱包，返回私钥、地址和助记词"""
        acct = Account.create()
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=128)
        return {
            "private_key": acct.key.hex(),
            "address": acct.address,
            "mnemonic": mnemonic
        }

    @classmethod
    def batch_create_wallets(cls, num: int) -> List[Dict[str, str]]:
        """批量创建钱包"""
        wallets = []
        for _ in range(num):
            wallets.append(cls.create())
        return wallets

    @staticmethod
    def export_to_excel(wallets: List[Dict[str, str]], filename: str) -> None:
        """导出钱包信息到 Excel"""
        df = pd.DataFrame(wallets)
        output_path = Path("output") / filename
        output_path.parent.mkdir(exist_ok=True)  # 确保 output 目录存在
        df.to_excel(output_path, index=False)