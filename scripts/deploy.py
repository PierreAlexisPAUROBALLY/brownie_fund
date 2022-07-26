from brownie import FundMe,MockV3Aggregator,network ,config#type:ignore
from scripts.helpful_scripts import get_account,deploy_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENT
from web3 import Web3

#brownie network add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 
#fork=https://eth-mainnet.g.alchemy.com/v2/MMjqw9zwr0sZVRnn0yNUVRJfDkBNMv8x accounts=10 mnemonic=brownie port=8545


def deploy_fund():
    account=get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        print(network.show_active())
        price_feed_address=config["networks"][network.show_active()]["eth_usd_price_feed"]
        print(price_feed_address)
    else:#deploy a mock
        deploy_mocks()
        price_feed_address=MockV3Aggregator[-1].address




    FM=FundMe.deploy(price_feed_address,{"from":account},publish_source=config["networks"][network.show_active()]["verify"]) #need etherscan token in brownie config
    
    print(f"deployed to {FM.address}")


def main():
    deploy_fund()
   
