from brownie import network,accounts,config,MockV3Aggregator #type:ignore
from web3 import Web3

DECIMALS=8
STARTING_PRICE=2000000000000000000000

LOCAL_BLOCKCHAIN_ENVIRONMENT=["development","ganache-local"]
FORKED_LOCAL_ENVIRONMENT=["mainnet-fork-dev"]
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENT:
        return(accounts[0])
    else:
        return(accounts.add(config["wallets"]["from_key"]))

def deploy_mocks():
    if len(MockV3Aggregator)<=0:
            MockV3Aggregator.deploy(DECIMALS,STARTING_PRICE,{"from":get_account()})
        