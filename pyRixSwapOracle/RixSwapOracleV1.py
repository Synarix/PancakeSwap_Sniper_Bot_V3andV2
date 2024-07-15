
from .libs.W3Utils import *
from .libs.IERC20 import *
from .libs.RixSwapOracle import *


class initSettings():
    def __init__(self):
        self.settings = self.initSettings()
        self.checkSettings()

    def reinitSettings(self):
        self.settings = self.initSettings()

    def initSettings(self):
        with open("./Settings.json") as f:
            keys = json.load(f)
        return keys
    
    def checkSettings(self):
        if Web3.is_address(self.settings["metamask_address"]) != True:
            print("Please check your Settings.json:  Error in: metamask_address!")
            raise SystemExit
        
        if len(self.settings["metamask_private_key"]) != 64 or len(self.settings["metamask_private_key"]) != 66:
            print("Please check your Settings.json:  Error in: metamask_private_key!")
            raise SystemExit


    def updateSettings(self, new_settings):
        self.settings.update(new_settings)
        with open("./Settings.json", "w") as f:
            json.dump(self.settings, f)


class SwapOracle:
    def __init__(self, token):

        self.settings = initSettings()
        self.w3 = self.connect()
        self.w3U = W3Utils(self.settings, self.w3)
        if Web3.is_address(token):
            pass
        else:
            token = constant(self.w3.eth.chain_id).RIX
        self.IERC20 = IERC20(self.settings, self.w3, Web3.to_checksum_address(token), self.w3U)
        self.SwapContract = RixSwapOracle(self.settings, self.w3, self.IERC20, self.w3U)
        
    def connect(self):
        keys = self.settings.settings
        if keys["RPC"][:2].lower() == "ws":
            w3 = Web3(Web3.WebsocketProvider(keys["RPC"],request_kwargs={'timeout': int(keys["timeout"])}))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        else:
            w3 = Web3(Web3.HTTPProvider(keys["RPC"], request_kwargs={'timeout': int(keys["timeout"])}))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        return w3
    

    








