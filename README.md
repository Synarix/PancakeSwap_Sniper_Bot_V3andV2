
## 🚀 BSC Pancakeswap V2 & V3 Sniper Bot 🚀
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/) [![Release](https://img.shields.io/badge/Release-V4-brightgreen)](https://github.com/Sevens-W3-Lab/Pancakeswap_BSC_Sniper_Bot/releases/tag/V4) [![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)]()

### 📞 Need Support?
Feel free to contact me on Telegram: 
<div style="display: flex; align-items: center; ;">
    <a href="https://t.me/Synarix_DEV" target="_blank" style="background-color: #424242; padding: 10px; border-radius: 20px; text-decoration: none; display: flex; align-items: center;">
        <img src="https://cdn4.cdn-telegram.org/file/XzdWPCv8jHqaAcT1zhwL2Lk11kxLZ8o6iA-DMIrr46FlBfK8ijQHDtjXIh9VqApOI1ZhYSOB1S46yQ9a5MuyJ1ZCn4INf7NsDorpDfo9tq7-oRfR-hJlRl4j0fPTq6_Wfez8IeuxvPfSxLS7hIWi43hcPRmgwXnLEC5-9itUiIIUblNkDLyZc5saQdw7SManURuruFfa2IwMxoHKM3z4-Oz_paWrpj0UuWgrA9rLxiFFDDSTAX6S2nLSmZjnBZ7g8ZJa0Hru84-yM6UmH09J2JI1EAkmaWB9YjnaBepJMFYSTWarMC8xFg9N0m_YRk3Ho4HVOW3_XzfVHtlB2obwJA.jpg" alt="Telegram" width="40" height="40" style=" vertical-align: middle; border-radius: 50%;">
        <span style="font-size: 20px; vertical-align: middle; margin-left: 10px; margin-right:10px;">@Synarix_DEV</span>
    </a>
</div>

### 🛠️ Purpose
This bot helps you compete with other trading bots or traders when buying a cryptocurrency on the PancakeSwap DEX. It's ideal for fair launches (stealth launches) or when you want to buy as quickly as possible on PancakeSwap trading pair creation. In high-demand scenarios, manual competition is almost impossible. PancakeSwap and PooCoin have slow UX, which slows your transaction, leading to undesirable prices. Bots have long been integral to trading in cryptocurrencies, stocks, fiat currencies, and more.

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

## ⚙️ Setup

### Install Python 3.12+

To install Python 3.12+, follow these steps based on your operating system:

#### 🪟 Windows
1. Download the latest version of Python from the [official Python website](https://www.python.org/downloads/).
2. Run the installer and ensure the "Add Python to PATH" option is selected.
3. Follow the installation instructions.

#### 🍎 macOS
1. Open Terminal.
2. Use Homebrew to install Python 3:  
   ```bash
   brew install python
   ```

#### 🐧 Debian-based Linux
1. Open Terminal.
2. Use the package manager to install Python 3. For example, on Debian-based systems:
   ```bash
   sudo apt-get update
   sudo apt-get install python3
   ```

#### Install 
First of all, you need to install Python3+. To run on Android, you need to install [Termux](https://termux.com/) (only from F-Droid works atm).

```shell
termux: 
$ pkg install python git cmake 
Debian/Ubuntu: 
$ sudo apt install python3 git cmake gcc
Windows:
You need to install Visual Studio BuildTools & Python3
```

Clone Repo:  
```shell
git clone https://github.com/Synarix/PancakeSwap_Sniper_Bot_V3andV2
cd PancaksSwap_Sniper_Bot_V3andV2
python3 -m pip install -r requirements.txt # install Python requirements
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
Verified contract: [0xbf2bd32bd3d643c1cfd6183120f9ff93171b58cd](https://bscscan.com/address/0xbf2bd32bd3d643c1cfd6183120f9ff93171b58cd#code).
For security, use only the verified contract.
You can find the used contract address in `pRixSwapOracle/constants.py` line 14.

All contributions fund server costs and the Synarix project development. Be part of our journey and support us. Early investors and users will be rewarded with RIX tokens.

#### Donation Address:
###### 0x3844D3051a35AcA55f2236897f92Fcfce7A83000

