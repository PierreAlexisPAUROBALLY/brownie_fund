from scripts.helpful_scripts import get_account,LOCAL_BLOCKCHAIN_ENVIRONMENT
from scripts.deploy import deploy_fund
from brownie import network #type:ignore
import pytest

def test_fw():
    acc=get_account()
    fm=deploy_fund()
    fee=fm.getEntranceFee()
    #...
    #assert ...

def test_WD():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip("skipping this test")
    else:
        pass