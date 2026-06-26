import numpy as np
import torch

class DynamicGridTrading:
    def __init__(self, initial_balance, grid_size, grid_levels, dynamic_reset_threshold):
        """
        Initialize the Dynamic Grid Trading strategy.
        
        :param initial_balance: Initial balance in USD.
        :param grid_size: The price difference between grid levels.
        :param grid_levels: Number of grid levels above and below the initial price.
        :param dynamic_reset_threshold: Threshold for resetting the grid dynamically.
        """
        self.initial_balance = initial_balance
        self.grid_size = grid_size
        self.grid_levels = grid_levels
        self.dynamic_reset_threshold = dynamic_reset_threshold
        self.reset()

    def reset(self):
        """Reset the trading state."""
        self.balance = self.initial_balance
        self.holdings = 0
        self.current_price = None
        self.grid_prices = None
        self.last_reset_price = None

    def initialize_grid(self, price):
        """Initialize the grid based on the current price."""
        self.current_price = price
        self.last_reset_price = price
        self.grid_prices = np.array([price + i * self.grid_size for i in range(-self.grid_levels, self.grid_levels + 1)])

    def check_reset_condition(self, price):
        """Check if the grid needs to be reset based on the dynamic reset threshold."""
        if abs(price - self.last_reset_price) / self.last_reset_price >= self.dynamic_reset_threshold:
            return True
        return False

    def reset_grid(self, price):
        """Reset the grid dynamically."""
        self.initialize_grid(price)

    def trade(self, price):
        """
        Execute trades based on the grid strategy.
        
        :param price: Current market price.
        """
        if self.grid_prices is None:
            self.initialize_grid(price)

        if self.check_reset_condition(price):
            self.reset_grid(price)

        for grid_price in self.grid_prices:
            if price <= grid_price and self.balance >= grid_price:
                # Buy at grid level
                self.holdings += 1
                self.balance -= grid_price
            elif price >= grid_price and self.holdings > 0:
                # Sell at grid level
                self.holdings -= 1
                self.balance += grid_price

    def get_portfolio_value(self, price):
        """Calculate the total portfolio value."""
        return self.balance + self.holdings * price

if __name__ == '__main__':
    # Dummy data for testing
    np.random.seed(42)
    torch.manual_seed(42)

    # Simulate a random walk for price data
    initial_price = 100
    num_steps = 100
    price_changes = np.random.normal(0, 1, num_steps)
    prices = np.cumsum(price_changes) + initial_price

    # Initialize the Dynamic Grid Trading strategy
    initial_balance = 1000
    grid_size = 5
    grid_levels = 3
    dynamic_reset_threshold = 0.1
    dgt = DynamicGridTrading(initial_balance, grid_size, grid_levels, dynamic_reset_threshold)

    # Simulate trading
    portfolio_values = []
    for price in prices:
        dgt.trade(price)
        portfolio_values.append(dgt.get_portfolio_value(price))

    # Print results
    print("Final Balance:", dgt.balance)
    print("Final Holdings:", dgt.holdings)
    print("Final Portfolio Value:", portfolio_values[-1])