from importlib.metadata import entry_points
from brownie import FundMe,accounts,MockV3Aggregator #type:ignore
from scripts.helpful_scripts import get_account
from web3 import Web3
import time
def fund():
    fundme=FundMe[-1]
    account=get_account()
    entrance_fee=fundme.getEntranceFee()
    print(entrance_fee)
    fundme.fund({"from":account,"value":entrance_fee*100})



def withdraw():
    fundme=FundMe[-1]
    account=get_account()
    fundme.withdraw({"from":account})


def main():
    fund()
    time.sleep(10)
    withdraw()