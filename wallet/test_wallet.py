import pytest
from wallet import Wallet, InSufficientFunds


@pytest.fixture
def my_wallet():
    return Wallet()


# @pytest.fixture
# def wallet():
#     return Wallet(100)


@pytest.mark.parametrize("earned, spent, expected", [(30, 10, 20), (20, 2, 18)])
def test_transcations(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected


# def test_default_initial_amount(my_wallet):
#     assert my_wallet.balance == 0


# def test_setting_inital_amount(wallet):
#     assert wallet.balance == 100


# def test_wallet_add_cash(wallet):
#     wallet.add_cash(10)
#     assert wallet.balance == 110


# def test_wallet_spend_cash(wallet):
#     wallet.spend_cash(40)
#     assert wallet.balance == 60


def test_wallet_spend_cash_raises_exception_on_insufficient_funds(my_wallet):
    with pytest.raises(InSufficientFunds):
        my_wallet.spend_cash(100)
