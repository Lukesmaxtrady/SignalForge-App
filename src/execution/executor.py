import os
import time
import numpy as np
import random
from typing import Optional, Dict, Any
from src.utils.logger import get_logger

logger = get_logger("executor")

class ExecutionEngine:
    """
    Simulates the execution of trading signals/orders with latency and slippage.
    Logs trades to a CSV file.
    """

    def __init__(self, demo: bool = True, latency_ms: int = 300, slippage_bps: float = 2.0):
        """
        Args:
            demo (bool): If True, run in demo (simulated) mode.
            latency_ms (int): Execution latency in milliseconds.
            slippage_bps (float): Average slippage in basis points.
        """
        self.demo = demo
        self.latency_ms = latency_ms
        self.slippage_bps = slippage_bps

        # Ensure the trade log directory exists
        self.trade_log_dir = "data/trades"
        os.makedirs(self.trade_log_dir, exist_ok=True)
        self.trade_log_path = os.path.join(self.trade_log_dir, "trade_log.csv")

        # Create log file with header if it doesn't exist or is empty
        if not os.path.exists(self.trade_log_path) or os.path.getsize(self.trade_log_path) == 0:
            with open(self.trade_log_path, "w") as f:
                f.write("timestamp,symbol,signal,init_price,fill_price,size,fee,status\n")

        self._running = False  # Control flag for run_async

    def execute(
        self,
        signal: str,
        price: float,
        size: float,
        symbol: str,
        extra: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Simulate execution of a trade signal with latency and slippage.

        Args:
            signal (str): 'buy' or 'sell'
            price (float): Market price
            size (float): Trade amount
            symbol (str): Trading symbol
            extra (dict, optional): Additional parameters

        Returns:
            dict: Trade result info
        """
        try:
            time.sleep(self.latency_ms / 1000.0)
            fill_price = price * (1 + np.random.normal(0, self.slippage_bps / 10000))
            status = "filled"
            if random.random() < 0.03:
                status = "partial"

            logger.info(
                f"Executed: {signal} {size} {symbol} @ {fill_price:.6f} [{status}] (demo={self.demo})"
            )

            with open(self.trade_log_path, "a") as f:
                f.write(
                    f"{time.strftime('%Y-%m-%d %H:%M:%S')},{symbol},{signal},{price:.6f},{fill_price:.6f},{size:.6f},0,{status}\n"
                )

            return {
                "signal": signal,
                "init_price": price,
                "fill_price": fill_price,
                "size": size,
                "symbol": symbol,
                "status": status,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "demo": self.demo,
                "extra": extra,
            }
        except Exception as e:
            logger.error(f"Execution error: {e}")
            return {
                "signal": signal,
                "init_price": price,
                "fill_price": None,
                "size": size,
                "symbol": symbol,
                "status": "error",
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "demo": self.demo,
                "error": str(e),
            }

    def toggle_mode(self, live: bool = True):
        """
        Toggle between live and demo mode.
        """
        self.demo = not live
        logger.info(f"Trading mode set to {'LIVE' if live else 'DEMO'}.")

    def run_async(self):
        """
        Dummy async run loop for background execution.
        Replace or extend with your actual trading logic.
        """
        logger.info("ExecutionEngine run_async started.")
        self._running = True
        try:
            while self._running:
                # Example task: log heartbeat or process queued trades
                logger.debug("ExecutionEngine is running...")
                time.sleep(10)  # Run every 10 seconds
        except Exception as e:
            logger.error(f"ExecutionEngine run_async error: {e}")
        finally:
            logger.info("ExecutionEngine run_async stopped.")

    def stop_async(self):
        """
        Stop the async run loop cleanly.
        """
        self._running = False
        logger.info("ExecutionEngine run_async stop requested.")

# Export as TradingEngine to match your app's import
TradingEngine = ExecutionEngine
