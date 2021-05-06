# Risks and considerations

There are several risks to think about before putting on these types of trades:

-   **Exchange security** – if the exchange or your account gets hacked, who knows what will happen to the futures contracts.
-   **Exchange credit risk** – if the crypto pair gaps down, the profitability of the trade depends on your short futures leg. If for whatever reason the exchange is not able to fulfil this, you may experience material loss of capital. This is partially mitigated by the existence of [insurance funds](https://www.binance.com/en/support/faq/360033525371).
-   **Liquidation risk** – if the future gaps up and spot doesn't immediately move with it, it is possible that Binance will liquidate you (as your account would momentarily show a large negative balance). This is unlikely, particularly using coin-margined futures, but crazy things do happen in the crypto markets.
-   **Implementation risk** – by default, Binance futures trade at 20x leverage with cross-margin. This should be changed to 1x leverage and isolated margin to minimise risk. If you accidentally leave it at 20x leverage (which I have done several times in the past) and crypto prices have a big up move, your entire margin balance may be liquidated.
-   **Annualised returns can often be deceptive** – there is no guarantee that a given premium will exist when you try to roll it (whether that is within 8 hours time for perps, or 6 months time for a delivery future).
-   The data shown here **does not account for fees, spread, or slippage**. These matter especially if you are trading in and out of perpetuals hoping to constantly roll to the highest-yielding perp.
