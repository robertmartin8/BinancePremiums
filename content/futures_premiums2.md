# Tutorials

## Cash-and-Carry tutorial

This example explains how one might put on a carry trade for BNBUSD-0625 (purely educational). This example uses coin-margined contracts, but similar steps apply to USD-margined contracts.

1. Register for a Binance account – using my [referral link](https://www.binance.com/en/register?ref=BN5UXJ7P) gives you 5% off fees.
2. Deposit cash/crypto
3. Buy BNB spot (`Trade --> Classic`)
4. Transfer this BNB into your COIN-M Futures wallet. This can be done by navigating to `Wallet --> Futures --> COIN-M Futures`. You will need to review the educational material and complete the quiz if you have not already done so.

<img src="https://github.com/robertmartin8/ReasonableDeviations/blob/gh-pages/assets/images/binance_tutorials/cash-carry-1.png?raw=true" style="width:100%;"/>
<br/><br/>

5. Select the BNBUSD Quarterly 0625 contract (COIN-M -> Delivery).
6. <span style="color: red">**Important:**</span>: change the margin mode from "Cross" to "Isolated" and **adjust leverage to 1x**.
7. In the "Place Order" window, place a limit order to **Sell/Short** 100%.

<img src="https://github.com/robertmartin8/ReasonableDeviations/blob/gh-pages/assets/images/binance_tutorials/cash-and-carry-2.png?raw=true" style="width:100%;"/>
<br/><br/>

You are now long BNB spot and short the BNB future, with no exposure to the movement of BNB (in principle). A worked example is as follows.

Suppose BNB is currently trading at $500 and the future is trading at $600, a 20% premium. We buy 1 BNB and put it in our margin account, then short $600 worth of the BNB future at 1x leverage (i.e using 100% of our 1 BNB margin balance at 1x leverage).

-   Case 1: BNB appreciates to $750 by expiry. We make a **profit of $250** ($750 - $500) on the long spot position and a **loss of $150** ($750 - $600) on the short future.
-   Case 2: BNB sells off to $300 by expiry. We make a **loss of $200** ($500 - $300) on the long spot position and a **gain of $300** ($600 - $300) on the short future.

In both cases, we make **$100 profit on a $500 position**, locking in the 20% premium we observed.
