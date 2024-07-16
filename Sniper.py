from time import sleep

from halo import Halo
from pyRixSwapOracle.RixSwapOracleV1 import SwapOracle
import requests
from pyRixSwapOracle.imports import *

class CustomPrinter:
    COLORS = {
        'reset': '\033[0m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }

printer = CustomPrinter()


ascii = """
                                  ##
 ####                             ##
##  #
###   ## ## #####    ###   ### # ###  ## ##
 ###  ## ##  ## ##  ## ##   ####  ##   ###
  ###  ###   ## ##   ####   ##    ##    #
#  ##  ###   ## ##  ## ##   ##    ##   ###
####    #   ### ###  ##### ####  #### ## ##
      ###
      ##

Supports Uniswap V2 and V3 Forks.
"""

parser = argparse.ArgumentParser(
    description='Set your Token and Amount example: "sniper.py -t 0x2BD29A514C306454F5be6923a421dbBE37B4aBDa -a 0.2"')
parser.add_argument(
    '-t', '--token', help='str, Token for snipe e.g. "-t 0x2BD29A514C306454F5be6923a421dbBE37B4aBDa"')
parser.add_argument('-a', '--amount', default=0,
                    help='float, Amount in Bnb to snipe e.g. "-a 0.1"')
parser.add_argument('-tx', '--txamount', default=1, nargs="?", const=1, type=int,
                    help='int, how mutch tx you want to send? It Split your BNB Amount in e.g. "-tx 5"')
parser.add_argument('-sp', '--sellpercent', default=100, nargs="?", const=1, type=int,
                    help='int, how mutch tokens you want to sell? Percentage e.g. "-sp 80"')
parser.add_argument('-hp', '--honeypot', default=False, action="store_true",
                    help='Check if your token to buy is a Honeypot, e.g. "-hp" or "--honeypot"')
parser.add_argument('-nb', '--nobuy', action="store_true",
                    help='No Buy, Skipp buy, if you want to use only TakeProfit/StopLoss/TrailingStopLoss')
parser.add_argument('-tp', '--takeprofit', default=0, nargs="?", const=True,
                    type=int, help='int, Percentage TakeProfit from your input BNB amount "-tp 50" ')
parser.add_argument('-sl', '--stoploss', default=0, nargs="?", const=True, type=int,
                    help='int, Percentage Stop loss from your input BNB amount "-sl 50" ')
parser.add_argument('-tsl', '--trailingstoploss', default=0, nargs="?", const=True,
                    type=int, help='int, Percentage Trailing-Stop-loss from your first Quote "-tsl 50" ')
parser.add_argument('-wb', '--awaitBlocks', default=0, nargs="?", const=True,
                    type=int, help='int, Await Blocks before sending BUY Transaction "-wb 5" ')
parser.add_argument('-cmt', '--checkMaxTax',  action="store_true",
                    help='get Token Tax and check if its higher.')
parser.add_argument('-cc', '--checkcontract',  action="store_true",
                    help='Check is Contract Verified and Look for some Functions.')
parser.add_argument('-so', '--sellonly',  action="store_true",
                    help='Sell all your Tokens from given address')
parser.add_argument('-bo', '--buyonly',  action="store_true",
                    help='Buy Tokens with from your given amount')
parser.add_argument('-cl', '--checkliquidity',  action="store_true",
                    help='with this arg you use liquidityCheck')
parser.add_argument('-r', '--retry', default=1, nargs="?", const=True, type=int,
                    help='with this arg you retry automatically if your tx failed, e.g. "-r 5" or "--retry 5" for max 5 Retrys')
parser.add_argument('-sec', '--SwapEnabledCheck',  action="store_true",
                    help='this argument disabled the SwapEnabled Check!')
args = parser.parse_args()




class SniperBot():
    def __init__(   self, 
                    token, 
                    amount, 
                    txamount, 
                    sellpercent, 
                    honeypot, 
                    nobuy, 
                    takeprofit, 
                    stoploss, 
                    trailingstoploss, 
                    awaitBlocks, 
                    checkMaxTax, 
                    checkcontract, 
                    sellonly, buyonly,
                    checkliquidity,
                    retry, 
                    SwapEnabledCheck
                ):
        self.token = token
        self.amount = amount
        self.tx = txamount
        self.sellpercent = sellpercent
        self.hp = honeypot
        self.nobuy = nobuy
        self.tp = takeprofit
        self.sl = stoploss
        self.tsl = trailingstoploss
        self.wb = awaitBlocks
        self.checkMaxTax = checkMaxTax
        self.checkcontract = checkcontract
        self.sellonly = sellonly
        self.buyonly = buyonly
        self.cl = checkliquidity
        self.retry = retry
        self.SwapEnabledCheck = SwapEnabledCheck
        self.stoploss = 0
        self.takeProfitOutput = 0
        if txamount != 0 or txamount != 1:
            self.amountForSnipe = float(self.amount) / float(self.tx)
        if self.sellpercent == 0 or self.sellpercent == None:
            self.sellpercent = 100
        self.COLORS = {
            'reset': '\033[0m',
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'purple': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m'
        }

        self.TXN = SwapOracle(token)
        self.SayWelcome()

    def print_custom(self, text:str="", color:str="", end:str = None):
        color_code = self.COLORS.get(color.lower(), self.COLORS['reset'])
        print(
            f"{color_code}{text}{self.COLORS['reset']}",
            end=end
            )


    def SayWelcome(self):
        if self.token == None:
            self.print_custom(
                "Please Check your Token argument e.g. -t 0x2BD29A514C306454F5be6923a421dbBE37B4aBDa", color="red")
            self.print_custom("exit!", color="red")
            raise SystemExit

        if self.nobuy != True:
            if not self.sellonly:
                if self.amount == 0:
                    self.print_custom("Please Check your Amount argument e.g. -a 0.01", color="red")
                    self.print_custom("exit!", color="red")
                    raise SystemExit
                
        self.tokenSymbol = self.TXN.IERC20.get_token_Symbol()
        self.print_custom(ascii, color="blue")
        self.print_custom("Attention, You pay a 1% Tax on your swap amount if you dont hold 1k RIX!", color="red")
        self.print_custom("Start Sniper Tool with following arguments:", color="yellow")
        self.print_custom( "---------------------------------", color="blue")
        self.print_custom(f"User Balance: {Web3.from_wei(self.TXN.SwapContract.getBNBBalance(), "ether")} BNB", color="yellow")
        self.print_custom("Amount for Buy: "+str(self.amount)+" BNB", color="yellow")
        self.print_custom("Token to Interact: "+str(self.token) , color="yellow")
        self.print_custom("Token Name: "+str(self.TXN.IERC20.get_token_Name()) , color="yellow")
        self.print_custom("Token Symbol: "+ str(self.tokenSymbol), color="yellow")
        self.print_custom("Transaction to send: "+str(self.tx) , color="yellow")
        self.print_custom("Amount per transaction: "+str(self.TXN.w3U.get_human_amount(self.amountForSnipe)) , color="yellow")
        self.print_custom("Await Blocks before buy: "+ str(self.wb), color="yellow")

        if self.tsl != 0:
            self.print_custom("Trailing Stop loss Percent: "+ str(self.tsl), color="yellow")
        if self.tp != 0:
            self.print_custom("Take Profit Percent: " + str(self.tp), color="yellow")
        if self.sl != 0:
            self.print_custom("Stop loss Percent: "+str(self.sl), color="yellow")
        self.print_custom("---------------------------------", color="blue")

                

    def getOutputTokenToBNB(self, percent: int = 100) -> int:
        tokenBalance = self.TXN.IERC20.get_token_balance(self.TXN.SwapContract.user_address)
        if tokenBalance > 0:
            AmountForInput = int((tokenBalance / 100) * percent)
            if percent == 100:
                AmountForInput = tokenBalance
        return self.TXN.SwapContract.getAmountsOutTokenToBNB(AmountForInput)[-1]
            

    def calcProfit(self):
        if self.amountForSnipe == 0.0:
            self.amountForSnipe = self.TXN.w3U.from_wei(self.getOutputTokenToBNB(percent=self.sellpercent))
                
        a = ((self.amountForSnipe * self.tx) * self.tp) / 100
        b = a + (self.amountForSnipe * self.tx)
        return b

    def calcloss(self):
        if self.amountForSnipe == 0.0:
            self.amountForSnipe = self.TXN.w3U.from_wei(self.getOutputTokenToBNB(percent=self.sellpercent))
        a = ((self.amountForSnipe * self.tx) * self.sl) / 100
        b = (self.amountForSnipe * self.tx) - a
        return b

    def calcNewTrailingStop(self, currentPrice):
        a = (currentPrice * self.tsl) / 100
        b = currentPrice - a
        return b

    def awaitBuy(self):
        for i in range(self.tx):
            tx = self.TXN.SwapContract.SwapETHtoToken(self.amountForSnipe, self.retry)
            try:
                if tx[0] == True:
                    self.print_custom("Buy Hash: " + tx[1] , color="green"), self.print_custom(tx[2] , color="yellow")
                if tx[0] != True:
                    self.print_custom("[ERROR]: Transaction fail, exiting", color="red")
                    raise SystemExit
            except Exception as e:
                print(e)

    def awaitSell(self):
        tokenBalance = self.TXN.w3U.from_wei(self.TXN.IERC20.get_token_balance(self.TXN.SwapContract.user_address), self.TXN.IERC20.get_token_decimals())
        AmountForInput = (tokenBalance / 100) * self.sellpercent
        tx = self.TXN.SwapContract.SwapTokentoETH(AmountForInput, self.retry)
        if tx[0] == True:
            self.print_custom("Sell TX Hash: " + tx[1] , color="green")
            self.print_custom(tx[2] , color="yellow")
        elif tx[0] != True:
            raise SystemExit


    def awaitApprove(self):
        tx = self.TXN.IERC20.approve(
            self.TXN.SwapContract.constants.RixSwapOracle,
            self.TXN.IERC20.get_token_balance(self.TXN.SwapContract.user_address)
            )
        if tx[0] == True:
            self.print_custom("Approve TX Hash: "+ tx[1] , color="green")
            self.print_custom(tx[2] , color="yellow")
        else:
            raise SystemExit


    def awaitBlocks(self):
        waitForBlock = self.TXN.w3U.block() + self.wb
        while True:
            sleep(0.3)
            if self.TXN.w3U.block() > waitForBlock:
                break
        self.print_custom("[DONE] Wait Blocks finish!", color="green")


    def CheckVerifyCode(self):
        while True:
            req = requests.get(
                f"https://api.bscscan.com/api?module=contract&action=getsourcecode&address={self.token}&apikey=YourApiKeyToken")
            if req.status_code == 200:
                getsourcecode = req.text.lower()
                jsonSource = json.loads(getsourcecode)
                if not "MAX RATE LIMIT REACHED".lower() in str(jsonSource["result"]).lower():
                    if not "NOT VERIFIED".lower() in str(jsonSource["result"]).lower():
                        self.print_custom("[CheckContract] IS Verfied")
                        for BlackWord in self.TXN.settings.settings["cc_BlacklistWords"]:
                            if BlackWord.lower() in getsourcecode:
                                self.print_custom(
                                    f"[CheckContract] BlackWord {BlackWord} FOUND, Exit!", color="red")
                                raise SystemExit
                        self.print_custom(
                              "[CheckContract] No known abnormalities found.", color="green")
                        break
                    else:
                        self.print_custom(
                            "[CheckContract] Code Not Verfied, Can't check, Exit!", color="red")
                        raise SystemExit
                else:
                    self.print_custom("Max Request Rate Reached, Sleep 5sec.", color="yellow")
                    sleep(5)
                    continue
            else:
                self.print_custom("BSCScan.com Request Faild, Exiting.", color="red")
                raise SystemExit


    def awaitLiquidity(self):
        spinner = Halo(text='await Liquidity', spinner='dots')
        spinner.start()
        while True:
            sleep(0.07)
            try:
                self.TXN.SwapContract.getAmountsOutBNBToToken(
                    self.TXN.w3U.to_wei(self.amountForSnipe, 18)
                )
                spinner.stop()
                break
            except Exception as e:
                # Uncomment next line to see errors inside the await Liquidity
                #print(e)
                if "UPDATE" in str(e):
                    self.print_custom(e)
                    raise SystemExit
                continue
        self.print_custom("[DONE] Liquidity is Added!", color="green")

    def fetchLiquidity(self):
        liq = self.TXN.w3U.from_wei(self.TXN.SwapContract.getLiquidityUSD(False), (18 +self.TXN.IERC20.get_token_decimals()))
        self.print_custom("[LIQUIDTY] Current Token Liquidity: "+str(round(liq))+" USD" , color="yellow" )
        if float(liq) < float(self.TXN.settings.settings["MinLiquidityUSD"]):
            self.print_custom("[LIQUIDTY] <- TO SMALL, EXIT!", color="red")
            raise SystemExit
        return True
    
    def awaitEnabledBuy(self):
        spinner = Halo(text='await Dev Enables Swapping', spinner='dots')
        spinner.start()
        while True:
            sleep(0.07)
            try:
                if self.TXN.SwapContract.TestSwapETHtoToken(self.amountForSnipe) == True:
                    spinner.stop()
                    break
            except Exception as e:
                self.print_custom(str(e), color="red")
                if "UPDATE" in str(e):
                    self.print_custom(e, color="red")
                    raise SystemExit
                continue
        self.print_custom("[DONE] Swapping is Enabeld!", color="green")

    def awaitMangePosition(self):
        highestLastPrice = 0
        if self.tp != 0:
            self.takeProfitOutput = self.calcProfit()
        if self.sl != 0:
            self.stoploss = self.calcloss()
        TokenBalance = float(self.TXN.w3U.get_human_amount(self.TXN.w3U.from_wei(
            self.TXN.IERC20.get_token_balance(self.TXN.SwapContract.user_address),
            self.TXN.IERC20.get_token_decimals()
        )))

        while True:
            try:
                sleep(0.9)
                LastPrice = float(
                    self.getOutputTokenToBNB(self.sellpercent) / (10**18))
                if self.tsl != 0:
                    if LastPrice > highestLastPrice:
                        highestLastPrice = LastPrice
                        self.TrailingStopLoss = self.calcNewTrailingStop(
                            LastPrice)
                    if LastPrice < self.TrailingStopLoss:
                        self.print_custom(
                              "[TRAILING STOP LOSS] Triggert!",  color="green")
                        self.awaitSell()
                        break


                if self.takeProfitOutput != 0:
                    if LastPrice >= self.takeProfitOutput:
                        self.print_custom(
                              "[TAKE PROFIT] Triggert!", color="green")
                        self.awaitSell()
                        break


                if self.stoploss != 0:
                    if LastPrice <= self.stoploss:
                        self.print_custom()
                        self.print_custom(
                              "[STOP LOSS] Triggert!", color="green")
                        self.awaitSell()
                        break

                msg = str("Token Balance: " + str(TokenBalance) + " | CurrentOutput: "+str(self.TXN.w3U.custom_round(LastPrice))+" BNB")
                if self.stoploss != 0:
                    msg = msg + " | Stop loss below: "+str(self.TXN.w3U.custom_round(self.stoploss)) + " BNB"
                if self.takeProfitOutput != 0:
                    msg = msg + "| Take Profit Over: "+str(self.TXN.w3U.custom_round(self.takeProfitOutput)) + " BNB"
                if self.tsl != 0:
                    msg = msg + " | Trailing Stop loss below: "+str(self.TXN.w3U.custom_round(self.TrailingStopLoss)) + " BNB"
                self.print_custom(text=msg, end="\r", color="yellow")

            except Exception as e:
                self.print_custom(f"[ERROR] {str(e)},\n\nSleeping now 20sec and Reinit RPC!", color="red")
                sleep(20)
                self.TXN = SwapOracle(self.token)
                continue

        self.print_custom(
              "[DONE] Position Manager Finished!", color="green")


    def StartUP(self):
        if self.sellonly:
            self.print_custom("Start SellOnly, for selling tokens!", color="yellow")
            self.awaitApprove()
            if self.SwapEnabledCheck == True:
                self.awaitEnabledBuy()
            if self.sellpercent > 0 and self.sellpercent < 100:
                pass
            else:
                self.sellpercent = int(input("Enter Percent you want to sell: "))
            tokenBalance = self.TXN.w3U.from_wei(self.TXN.IERC20.get_token_balance(self.TXN.SwapContract.user_address), self.TXN.IERC20.get_token_decimals())
            self.print_custom(f"Token Balance: {tokenBalance} {self.tokenSymbol}", color="yellow")
            AmountForInput = (tokenBalance / 100) * self.sellpercent
            self.print_custom("Sell TX Hash: " + self.TXN.SwapContract.SwapTokentoETH(AmountForInput)[1], color="green")
            raise SystemExit

        if self.buyonly:
            self.print_custom(
                f"Start BuyOnly, buy now with {self.amountForSnipe}BNB tokens!", color="yellow")
            self.print_custom("Buy TX Hash: " + self.TXN.SwapContract.SwapETHtoToken(self.amountForSnipe, self.retry)[1] , color="green")
            raise SystemExit

        if self.nobuy != True:
            self.awaitLiquidity()
            if self.SwapEnabledCheck == True:
                self.awaitEnabledBuy()

        if self.checkcontract:
            self.CheckVerifyCode()

        if self.hp == True:
            try:
                self.print_custom("[HONEYPOT]: Checking Token...", color="yellow")
                honeyTax = self.TXN.SwapContract.getTokenInfos()
                if honeyTax[2] == True:
                    self.print_custom("[HONEYPOT]: Token is Honeypot, exiting", color="red")
                    raise SystemExit
                
                elif honeyTax[2] == False:
                    self.print_custom(
                          "[HONEYPOT]: Token is NOT a Honeypot!", color="green"
                          )
                    
            except Exception as e:
                print(e)
                self.i = input(
                    "Error in HoneyPot Check, HIGH Risk to enter a Honeypot!\n" +" Exiting? y/n \n > ")
                if self.i.lower() == "y":
                    raise SystemExit

        if self.checkMaxTax == True:
            try:
                honeyTax = self.TXN.SwapContract.getTokenInfos()
                self.print_custom("[TOKENTAX] Current Token BuyTax: "+str(honeyTax[0])+" %" , color="yellow")
                self.print_custom("[TOKENTAX] Current Token SellTax: "+str(honeyTax[1])+" %" , color="yellow")
                if honeyTax[1] > self.TXN.settings.settings["MaxSellTax"]:
                    self.print_custom("[TOKENTAX] Token SellTax exceeds Settings.json, exiting!", color="red")
                    raise SystemExit
                if honeyTax[0] > self.TXN.settings.settings["MaxBuyTax"]:
                    self.print_custom("[TOKENTAX] Token BuyTax exceeds Settings.json, exiting!", color="red")
                    raise SystemExit
            except Exception as e:
                print(e)
                self.i = input(
                        "Error in Token Tax Check, HIGH Risk to enter a Honeypot!\n"+"Exiting? y/n \n > " )
                if self.i.lower() == "y":
                        raise SystemExit

        if self.wb != 0:
            self.awaitBlocks()
            
        self.print_custom(f"[TOKEN PRICE]: ${self.TXN.w3U.custom_round(self.TXN.w3U.from_wei(self.TXN.SwapContract.getUSDPrice(), 18)) }", color="green")

        if self.cl == True:
            if self.fetchLiquidity() != False:
                pass

        if self.nobuy != True:
            self.awaitBuy()

        if self.tsl != 0 or self.tp != 0 or self.sl != 0:
            sleep(3)
            self.awaitApprove()
            self.awaitMangePosition()

        self.print_custom("Synarix Sniper Bot Finish Work.", color="green")



if __name__ == "__main__":
    sniper_bot = SniperBot(
        args.token, 
        args.amount, 
        args.txamount, 
        args.sellpercent, 
        args.honeypot, 
        args.nobuy, 
        args.takeprofit, 
        args.stoploss, 
        args.trailingstoploss, 
        args.awaitBlocks, 
        args.checkMaxTax, 
        args.checkcontract, 
        args.sellonly, 
        args.buyonly,
        args.checkliquidity,
        args.retry, 
        args.SwapEnabledCheck
).StartUP()
