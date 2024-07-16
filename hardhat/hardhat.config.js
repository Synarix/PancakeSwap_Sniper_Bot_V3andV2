require("@nomicfoundation/hardhat-toolbox");
console.log("Loading hardhat.config.js ...");

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
        url: "https://bscrpc.com",
        blockNumber: 40515030 // add here last block
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
};

console.log("hardhat.config.js Loaded!");
