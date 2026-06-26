# Dynamic Grid Trading Strategy: From Zero Expectation to Market Outperformance

This repository contains the Python/PyTorch implementation of the research paper **"Dynamic Grid Trading Strategy: From Zero Expectation to Market Outperformance"** by Kai-Yuan Chen, Kai-Hsin Chen, and Jyh-Shing Roger Jang. The paper introduces a novel trading strategy, Dynamic Grid-based Trading (DGT), designed to outperform traditional grid trading and buy-and-hold strategies in the cryptocurrency market through dynamic adaptation to market conditions.

## Table of Contents

1. [Introduction](#introduction)
2. [Key Concepts](#key-concepts)
3. [Repository Overview](#repository-overview)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Results](#results)
7. [Contributions](#contributions)
8. [License](#license)

---

## Introduction

Grid trading is a popular, systematic trading strategy that divides a specified price range into multiple levels ("grids") and executes buy and sell orders at these levels. While it has been widely used due to its simplicity and predictability, the authors of this paper demonstrate that its expected return, under straightforward assumptions, converges to zero.

To address this limitation, the authors propose a **Dynamic Grid-based Trading (DGT)** strategy that adjusts grid positions dynamically based on market conditions. This adaptive approach aims to maximize profitability and control risk in volatile markets, such as cryptocurrencies.

This repository provides the code to replicate the findings in the paper, including backtesting results on Bitcoin and Ethereum datasets.

---

## Key Concepts

### 1. Traditional Grid Trading
- **Overview**: Divides a predefined price range into equal intervals (grids) and alternates between buying and selling at these grid levels.
- **Limitation**: Assumes a stationary market and does not adapt to changing conditions, leading to zero expected returns over time.

### 2. Dynamic Grid-based Trading (DGT)
- **Core Idea**: Dynamically adjusts the grid range and levels based on real-time market conditions.
- **Benefits**:
  - Adapts to volatility and trend changes in the market.
  - Mitigates the risk of stagnation during prolonged unidirectional trends.
  - Achieves higher internal rate of return (IRR) compared to traditional methods.

### 3. Performance Evaluation
The strategy was backtested using minute-level Bitcoin and Ethereum trading data from January 2021 to July 2024. Metrics used for evaluation include:
- **Internal Rate of Return (IRR)**: A measure of profitability.
- **Risk Control**: Quantified through metrics like drawdown and volatility.

---

## Repository Overview

The repository includes the following components:

```
.
├── data/
│   ├── btc_data.csv            # Minute-level historical BTC price data
│   ├── eth_data.csv            # Minute-level historical ETH price data
├── models/
│   ├── grid_trading.py         # Implementation of the traditional grid trading strategy
│   ├── dynamic_grid_trading.py # Implementation of the DGT strategy
├── utils/
│   ├── data_loader.py          # Functions to load and preprocess market data
│   ├── metrics.py              # Utility functions for performance evaluation (e.g., IRR, risk metrics)
├── notebooks/
│   ├── backtesting.ipynb       # Jupyter notebook for running backtests
│   ├── visualization.ipynb     # Notebook for plotting and analyzing results
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── LICENSE                     # License information
```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/dynamic-grid-trading.git
   cd dynamic-grid-trading
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Data Preparation
Place your minute-level cryptocurrency data in the `data/` directory. Sample data files (`btc_data.csv`, `eth_data.csv`) are included for convenience.

### 2. Running Backtests
Use the provided Jupyter notebook `backtesting.ipynb` to run backtests on the traditional grid and DGT strategies. Customize parameters such as grid size, initial capital, and trading fees as needed.

### 3. Visualization
Use the `visualization.ipynb` notebook to analyze and visualize the results. This includes performance metrics like IRR, drawdown, and PnL curves.

### 4. Customization
You can modify the grid trading parameters and DGT logic in `grid_trading.py` and `dynamic_grid_trading.py`. The `metrics.py` file can also be extended to include additional evaluation metrics.

---

## Results

The backtesting results in the paper show that:

1. **Traditional Grid Trading**:
   - Achieves near-zero expected returns over the long term due to its static nature.

2. **Dynamic Grid-based Trading (DGT)**:
   - Outperforms traditional grid trading and buy-and-hold strategies.
   - Demonstrates higher profitability (IRR) and better risk control during volatile market conditions.

The implementation in this repository reproduces the key results from the paper, allowing you to explore the impact of different parameters and market conditions.

---

## Contributions

We welcome contributions to improve this implementation or extend its functionality. Please feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.