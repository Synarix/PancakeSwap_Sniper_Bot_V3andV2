from pyRixSwapOracle.imports import *


class IERC20:
    def __init__(self, settings, w3, token, w3U):
        self.settings, self.user_address, self.priv_key, self.w3, self.token, self.w3U = settings, settings.settings["metamask_address"], settings.settings["metamask_private_key"], w3, token, w3U
        self.token_Instance = self.init_token_instance()
        
    def init_token_instance(self):
        with open("./pyRixSwapOracle/ABIS/IERC20.json") as f:
            IERC20_abi = json.load(f)
        token_Instance = self.w3.eth.contract(
            address=Web3.to_checksum_address(self.token), abi=IERC20_abi)
        return token_Instance
    
    def get_token_address(self):
        return Web3.to_checksum_address(self.token_Instance.address)

    def get_token_decimals(self):
        return self.token_Instance.functions.decimals().call()

    def get_token_Name(self):
        return self.token_Instance.functions.name().call()

    def get_token_Symbol(self):
        return self.token_Instance.functions.symbol().call()
    
    def get_token_balance(self, address):
        return self.token_Instance.functions.balanceOf(Web3.to_checksum_address(address)).call()
    
    def get_token_allowance(self, spender):
        return self.token_Instance.functions.allowance(self.user_address, spender).call()
    
    def is_approved(self, spender, amountIn):
        allowance = self.get_token_allowance(spender)
        if int(allowance) >= int(amountIn):
            return True
        else:
            return False
        
    def approve(self, spender, amountIn):
        if self.is_approved(spender, amountIn) == False:
            txn = self.token_Instance.functions.approve(
                Web3.to_checksum_address(spender),
                2**256 - 1
            ).build_transaction(
                {'from': self.user_address,
                 'gas_Price': self.w3.eth.gas_price + Web3.to_wei(self.settings.settings["GWEI_OFFSET"], "gwei"),
                 'nonce': self.w3.eth.get_transaction_count(self.user_address),
                 'value': 0}
            )
            gas = self.w3U.estimateGas(txn)
            txn.update({'gas': int(gas[0])})
            signed_txn = self.w3.eth.account.sign_transaction(
                txn,
                self.priv_key
            )
            txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                txn, timeout=self.settings.settings["timeout"])
            if txn_receipt['status'] == 1:
                return True, txn.hex(), gas[1]
            else:
                return False, txn.hex(), gas[1]
        else:
            return True, "Already Approved", ""
            

    def transfer(self, receiver, amountIn):
        try:
            txn = self.token_Instance.functions.transfer(
                    Web3.to_checksum_address(receiver),
                    self.w3U.to_wei(amountIn, self.get_token_decimals())
                ).build_transaction(
                    {'from': self.user_address,
                     'gas_Price': self.w3.eth.gas_Price + Web3.to_wei(self.settings.settings["GWEI_OFFSET"], "gwei"),
                     'nonce': self.w3.eth.get_transaction_count(self.user_address),
                     'value': 0
                    }
                )
            txn.update({'gas': int(self.w3U.estimateGas(txn)[0])})
            signed_txn = self.w3.eth.account.sign_transaction(
                txn,
                self.priv_key
            )
            txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                txn, timeout=self.settings.settings["timeout"])
            if txn_receipt['status'] == 1:
                return True, txn.hex()
            else:
                return False, txn.hex()
        except Exception as e:
            print(e)
            return False, txn.hex()
