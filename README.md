# coinflip-cli

A single‑file Python script that flips a virtual coin.

## Features
- Fair flip (`--bias 0.5`) or custom bias (`--bias 0.7` for 70% heads).
- Optional count to flip multiple times.
- Simple, zero‑dependency, works on any platform with Python 3.

## Usage
```bash
python coinflip.py          # one fair flip
python coinflip.py -c 10   # ten fair flips
python coinflip.py -b 0.8  # biased towards heads
python coinflip.py -c 5 -b 0.3
```

## License
MIT