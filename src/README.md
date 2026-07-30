# Source Code Guide

[← Back to the project README](../README.md)

The modules in this directory implement the driver-to-route assignment study.

| Module | Responsibility |
|---|---|
| `main.py` | Load data, run both algorithms, and generate outputs |
| `dados.py` | Read and validate the CSV inputs |
| `guloso.py` | Construct a greedy assignment |
| `hungaro.py` | Solve the minimum-cost assignment with the Hungarian method |
| `saida.py` | Display and export assignments |
| `visual.py` | Create the cost-matrix and assignment charts |
| `benchmark.py` | Compare algorithm execution behavior |

Run the main workflow from this directory because the current implementation uses relative paths:

```bash
python main.py
```

See the root README for installation requirements, the mathematical interpretation, generated outputs, and project credits.
