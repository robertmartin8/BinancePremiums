### Tutorial

This example explains how one might put on a carry trade for BNBUSD-0625 (purely educational).

1. Register for a Binance account – using my [referral link](https://www.binance.com/en/register?ref=BN5UXJ7P) gives you 5% off fees.
2. Deposit cash/crypto and buy BNB spot.
3. Transfer this BNB into your COIN-M Futures wallet.
4. Select the BNBUSD Quarterly 0625 contract (COIN-M -> Delivery).
5. **IMPORTANT**: change the margin mode from "Cross" to "Isolated" and **adjust leverage to 1x**
6. In the "Place Order" window, place a limit order to **Sell/Short** 100%.

You are now long BNB spot and short the BNB future, with no exposure to the movement of BNB (in principle). A worked example is as follows.

Suppose BNB is currently trading at $500 and the future is trading at $600, a 20% premium. We buy 1 BNB and put it in our margin account, then short $500 worth of the BNB future at 1x leverage.

If BNB appreciates to $750 by expiry. In this case, we made a **profit of $250** ($750 - $250) on the long spot position and a **loss of $150** ($750 - $600) on the short future.

If BNB sells off to $300 by expiry, we make a **loss of $200** ($500 - $300) on the long spot position and a **gain of $300** ($600 - $300) on the short future.

In both cases, we make **$100 profit on a $500 position**, locking in the 20% premium we observed.
