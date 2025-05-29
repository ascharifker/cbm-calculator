# CBM Calculator

This repository provides a simple CBM (cubic meter) container calculator.
It allows you to estimate how many shipping containers are required for
multiple boxes based on their dimensions.

## Usage

Use the command line interface in `cli.py`:

```bash
python3 cli.py --box 1 1 1 10 --box 0.5 0.5 0.5 20
```

You can specify custom container dimensions with `--container`:

```bash
python3 cli.py --box 1 1 1 10 --container 6 2.4 2.4
```

Run tests with:

```bash
python3 -m unittest
```

