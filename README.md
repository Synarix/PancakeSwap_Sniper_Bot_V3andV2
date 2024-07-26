


## 🚀 BSC Pancakeswap/Uniswap V2 & V3 Sniper Bot 🚀
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/) [![Release](https://img.shields.io/badge/Release-V1-brightgreen)](https://github.com/Synarix/PancakeSwap_Sniper_Bot_V3andV2) [![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)]()
### Faster and much cheaper than Maestro or other Telegram multi-user snipers.  

#### 👀 Bot Preview:
<!-- HTML-Version -->
<img src="https://imgur.com/uSdPhU7.jpg" alt="preview">

## [Show Transaction](https://bscscan.com/tx/0x5389318c7371b40904e5141159d4f8cb56f2903dea63b2379a3c287630f116f8)

### 📞 Need Support or help?
#### Join Communty: 
###### Telegram:
<!-- HTML-Version -->
<div style="display: flex; align-items: center; ;">
   <a href="https://t.me/SynarixAnnoucements" target="_blank" style="background-color: #424242; padding: 10px; border-radius: 20px; text-decoration: none; display: flex; align-items: center;">
        <img src="https://i.imgur.com/8zl66Qv.jpg" alt="Telegram" width="40" height="40" style="vertical-align: middle; border-radius: 50%;">
        <span style="font-size: 20px; vertical-align: middle; margin-left: 10px; margin-right:10px;">Synarix Annoucements</span>
    </a>
</div>


### 🛠️ Purpose
This bot helps you compete with other trading bots or traders when buying a cryptocurrency on the Uniswap V2/V3 DEX forks like PancakeSwap.

It's ideal for fair launches (stealth launches) or when you want to buy as quickly as possible on PancakeSwap trading pair creation. In high-demand scenarios, manual competition is almost impossible.

PancakeSwap and PooCoin have slow UX, which slows your transaction, leading to undesirable prices.
Bots have long been integral to trading in cryptocurrencies, stocks, fiat currencies, and more.

### 🔄 Multi Hops for Optimal Results 
The tool uses advanced algorithms to analyze multiple exchange routes to find the most efficient path for your swap. 

### ⚡ Enjoy a Seamless Swapping Experience 
With this tool, you can effortlessly swap your assets for BNB and take advantage of its many benefits. Start maximizing your returns today!

### ✨ Features
- **🚀 Sniping:** Quick token purchases during high-demand events.
- **🔍 Honeypot Checker:** Ensures safe trading.
- **🔄 Multi Hops:** Finds the most efficient swap path.
- **💸 Low Tax Rates:** 1% tax, reduced to 0.2% if holding 1k RIX.
- **🔄 Seamless Swapping:** Effortless asset swaps for BNB.

### ⚙️ Setup Python 3.12+ and Git
To install Python 3.12+, follow these steps based on your operating system:

#### 🪟 Windows
1. Download the latest version of Python from the [official Python website](https://www.python.org/downloads/).
2. Run the installer and ensure the "Add Python to PATH" option is selected.
3. Follow the installation instructions.
4. Download Git from the [official Git website](https://git-scm.com/downloads) and follow the installation instructions.

#### 🍎 macOS
1. Open Terminal.
2. Use [Homebrew](https://brew.sh/) to install Python3 and Git:  
   ```bash
   brew install python git
   ```

#### 🐧 Debian-based Linux
1. Open Terminal.
2. Use the package manager to install Python 3 and Git.
   ```bash
   sudo apt-get update
   sudo apt-get install python3 git cmake
   ```

#### 📱 Termux (Android)
1. Termux Installation:
     Download and install Termux from [F-Droid](https://f-droid.org/en/packages/com.termux/) (recommended, other Builds bricked).

2. Install Python 3.12+ and Additional Tools in Termux:
 Open Termux.
Install Python, Git, and CMake:
    ```bash
    pkg install python3 git cmake
    ```
### ⚙️ Install Sniper Bot
1. Open Shell or CMD
2. Clone Repo: Alternative Download via Zip
    ```shell
    git clone https://github.com/Synarix/PancakeSwap_Sniper_Bot_V3andV2
    ``` 
3. Go into PancaksSwap_Sniper_Bot_V3andV2 downloaded or extracted folder
    ```shell
    cd PancakeSwap_Sniper_Bot_V3andV2
    ``` 
4. Install python3 requirements
    ```shell
    python3 -m pip install -r requirements.txt
    ```

## 🚀 Start Sniper.py

The Sniper bot can be started using various command-line options. Below are the commands and their descriptions:

```shell
python Sniper.py -t <TOKEN_ADDRESS> -a <BNB_AMOUNT> -tx <TAMOUNT> -hp -wb <BLOCKS WAIT BEFORE BUY> -tp <TAKE PROFIT IN PERCENT> -sl <STOP LOSS IN PERCENT>
```

### Options
`Dont use %`
- `-t <TOKEN_ADDRESS>`: The address of the token you want to snipe.
- `-a <AMOUNT>`: The amount of BNB you want to use for the purchase.
- `-tx <TXAMOUNT>`: The number of transactions you want to send, splitting your input BNB amount into multiple transactions.
- `-sp <SELL_PERCENT>`: The percentage of tokens you want to sell.
- `-hp`: Enable the honeypot checker to ensure the token is safe.
- `-nb`: No buy, skip buy if you want to use only TakeProfit/StopLoss/TrailingStopLoss.
- `-tp <TAKE_PROFIT_IN_PERCENT>`: The percentage at which you want to take profit.
- `-sl <STOP_LOSS_IN_PERCENT>`: The percentage at which you want to stop loss.
- `-tsl <TRAILING_STOP_LOSS_IN_PERCENT>`: The percentage trailing stop loss from your first quote.
- `-wb <BLOCKS_WAIT_BEFORE_BUY>`: The number of blocks to wait after sale is open before making the purchase.
- `-cmt`: Get token tax and check if it’s higher than settings.
- `-cc`: Check if the contract is verified and look for some functions.
- `-so`: Sell all your tokens from the given address.
- `-bo`: Buy tokens with your given amount.
- `-cl`: Use liquidity check with this argument.
- `-r <RETRY>`: Retry automatically if your transaction fails.
- `-sec`: Disable the SwapEnabled check with this argument.



## 💖 Support Developer
Verified contract: [0xa88ee4962d365535aa02e60e93f1c10f51dfd5ea](https://bscscan.com/address/0xa88ee4962d365535aa02e60e93f1c10f51dfd5ea#code).
For security, use only the verified contract.
You can find the used contract address in `pRixSwapOracle/constants.py` line 14.

All contributions fund server costs and the Synarix project development. Be part of our journey and support us. Early investors and users will be rewarded with RIX tokens.

#### Donation Address:

###### EVM: [0x0000022f6f742ca30bb7F309f53f619f36E826F2](https://bscscan.com/address/0x0000022f6f742ca30bb7f309f53f619f36e826f2)
###### BTC: [bc1qr99ge06cdr84ty53lz50esc236fp5pjv7a3dut](https://btcscan.org/address/bc1qr99ge06cdr84ty53lz50esc236fp5pjv7a3dut)
