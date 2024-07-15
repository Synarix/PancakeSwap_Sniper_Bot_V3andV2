


class constant:
    def __init__(self, chainID):
        print(f"Connected to ChainID: {chainID}")
        self.RixSwapOracle = None
        self.RixFeeUtils = None
        self.ZERO = "0x0000000000000000000000000000000000000000"  # This is constant across all chains
        self.WETH = None
        self.RIX = None

        if int(chainID) == 56:
            self.RixSwapOracle = "0xa88EE4962D365535aa02e60E93f1C10F51DFd5EA"
            self.RIX = "0x2BD29A514C306454F5be6923a421dbBE37B4aBDa"
            self.WETH = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"

        elif int(chainID) == 31337: #Local Hardhat fork for testing 
            self.RixSwapOracle = "0xa88EE4962D365535aa02e60E93f1C10F51DFd5EA"
            self.RIX = "0x2BD29A514C306454F5be6923a421dbBE37B4aBDa"
            self.WETH = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
            
        else:
            raise SystemExit("ChainID not Supported!")

