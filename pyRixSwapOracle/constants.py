


class constant:
    def __init__(self, chainID):
        #print(f"Connected to ChainID: {chainID}")
        self.RixSwapOracle = None
        self.RixFeeUtils = None
        self.ZERO = "0x0000000000000000000000000000000000000000"  # This is constant across all chains
        self.WETH = None
        self.RIX = None

        if int(chainID) == 56:
            self.RixSwapOracle = "0xBf2bd32bd3D643C1CfD6183120F9FF93171b58cD"
            self.RIX = "0x2BD29A514C306454F5be6923a421dbBE37B4aBDa"
            self.WETH = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"

        elif int(chainID) == 31337: #Local Hardhat fork for testing 
            self.RixSwapOracle = "0xBf2bd32bd3D643C1CfD6183120F9FF93171b58cD"
            self.RIX = "0x2BD29A514C306454F5be6923a421dbBE37B4aBDa"
            self.WETH = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
            
        else:
            raise SystemExit("ChainID not Supported!")

