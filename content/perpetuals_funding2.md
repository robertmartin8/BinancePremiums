## Perpetual funding tutorial

In this example (purely educational), we show how one might take advantage of a positive funding rate for DOGEUSD_PERP.

1. Register for a Binance account – using my [referral link](https://www.binance.com/en/register?ref=BN5UXJ7P) gives you 5% off fees.
2. Deposit cash/crypto and buy DOGE spot.
3. Transfer this DOGE into your COIN-M Futures wallet (so far, the same steps as for Cash-and-Carry).
4. Select the COIN-M DOGEUSD perpetual contract.
5. <span style="color: red">**Important:**</span> change the margin mode from "Cross" to "Isolated" and **adjust leverage to 1x**
6. In the "Place Order" window, place a limit order to **Sell/Short** 100%.

<img src="https://github.com/robertmartin8/ReasonableDeviations/blob/gh-pages/assets/images/binance_tutorials/perp-funding.png?raw=true" style="width:100%;"/>
<br/><br/>

Having put this position on, you will receive the funding rate every 8 hours.

<span style="color: red">**Warning:**</span> the funding rate can vary significantly. If you put on the above trade when the funding is positive, but 8h later the funding becomes negative, you will be _paying_ to put the position on. As a result, one may wish to look for contracts whose funding rates have been consistently high over a longer time period (e.g by looking at the 30d avg funding).
