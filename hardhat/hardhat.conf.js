module.exports = {
 solidity: {
   version: "0.8.26",
   settings: {
     optimizer: {
       enabled: true,
       runs: 200,
     },
   },
 },
 networks: {
   hardhat: {
     forking: {
       url: "https://endpoints.omniatech.io/v1/bsc/mainnet/public",
       blockNumber: 39915435
     },
     chains: {
       56: {
         hardforkHistory: {
           cancun: 39915435
         }
       }
     }
   },
 }
}

