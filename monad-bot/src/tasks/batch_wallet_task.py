from pathlib import Path
from core.wallet_manager import WalletManager


def batch_create_and_export(num_wallets: int = 10):
    # 批量生成钱包
    wallets = WalletManager.batch_create_wallets(num_wallets)

    # 导出到 Excel
    WalletManager.export_to_excel(wallets, "wallets.xlsx")
    print(f"✅ {num_wallets} 个钱包已生成并导出到 {Path('output').resolve() / 'wallets.xlsx'}")


if __name__ == "__main__":
    batch_create_and_export()