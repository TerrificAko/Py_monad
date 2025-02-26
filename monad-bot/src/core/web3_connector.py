from web3 import Web3

class Web3Connector:
    def __init__(self, rpc_url):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        assert self.w3.is_connected(), "Failed to connect to RPC"
