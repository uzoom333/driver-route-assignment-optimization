# Driver-to-Route Assignment Optimization

A university Algorithm Design project that models one-to-one driver and route assignment as a minimum-cost bipartite matching problem.

## Project Overview

The case study uses the fictional company MidWest Logistics S/A. Each driver-route pair has a cost that may represent time, distance, risk, or a weighted combination of factors. The program compares two assignment methods:

- a greedy algorithm, which is straightforward and fast but does not guarantee a global optimum;
- the Hungarian algorithm, which solves the assignment problem optimally in polynomial time.

The repository contains the input data used by the project, both implementations, generated assignments, and visual comparisons.

## Mathematical Formulation

Drivers and routes form the two partitions of a bipartite graph. An edge connects every eligible driver-route pair and carries its assignment cost. The objective is to select a one-to-one matching with minimum total cost.

## Repository Structure

```text
projetopaa/
├── data/        # Driver, route, and cost-matrix CSV files
├── docs/        # Course report material
├── resultados/  # Generated CSV, JSON, and chart outputs
├── src/
│   ├── benchmark.py
│   ├── dados.py
│   ├── guloso.py
│   ├── hungaro.py
│   ├── main.py
│   ├── saida.py
│   └── visual.py
└── README.md
```

## Requirements

- Python 3.9 or later
- pandas
- NumPy
- SciPy
- Matplotlib

## Installation

```bash
git clone https://github.com/uzxcontato-ui/projetopaa.git
cd projetopaa

python3 -m venv .venv
source .venv/bin/activate
python -m pip install pandas numpy scipy matplotlib
```

On Windows PowerShell, activate the environment with `.\.venv\Scripts\Activate.ps1`.

## Running the Project

The current scripts use paths relative to the `src` directory:

```bash
cd src
python main.py
```

Generated assignment files and figures are written to `resultados/`.

## Outputs

- greedy and Hungarian assignments in CSV and JSON;
- a cost-matrix heatmap;
- per-assignment cost charts;
- console output with total costs for comparison.

The committed outputs correspond to the repository's example dataset and should not be generalized to real logistics operations without additional modeling and validation.

## Technologies

- Python for implementation
- pandas and NumPy for data handling
- SciPy for the Hungarian assignment routine
- Matplotlib for visualization

## Academic Context

Developed in November 2025 for the Project and Analysis of Algorithms course.

### Group 5

- Renato Morais
- Gabriel Dantas
- Guilherme Aguiar
- Flaelisnanda
