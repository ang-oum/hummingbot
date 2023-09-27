from hummingbot.strategy.script_strategy_base import ScriptStrategyBase

#subclass of scriptstrategybase
class QuickstartScript(ScriptStrategyBase): 
    markets = {"binance_paper_trade":{"BTC-USDT, ETH-USDT"}}

    def on_tick(self):
        price = self.connectors["binance_paper_trade"].get_mid_price("BTC-USDT")
        msg = f"Bitcoin price ${price}"
        self.logger().info(msg)                  #insert logger example: telegram
        self.notify_hb_app_with_timestamp(msg)