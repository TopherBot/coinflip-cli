#!/usr/bin/env python3
"""coinflip-cli – tiny coin flipping utility.

Run without arguments for a single fair flip.
Options:
  -c, --count N   Number of flips (default: 1)
  -b, --bias P   Probability of heads (0.0‑1.0, default: 0.5)
"""
import argparse, random, sys

def parse_args():
    p = argparse.ArgumentParser(description='Tiny coin flip utility')
    p.add_argument('-c', '--count', type=int, default=1, help='Number of flips')
    p.add_argument('-b', '--bias', type=float, default=0.5, help='Probability of heads (0.0-1.0)')
    return p.parse_args()

def flip(bias):
    return 'Heads' if random.random() < bias else 'Tails'

def main():
    args = parse_args()
    if not (0.0 <= args.bias <= 1.0):
        sys.stderr.write('Error: bias must be between 0.0 and 1.0\n')
        sys.exit(1)
    results = [flip(args.bias) for _ in range(args.count)]
    for i, r in enumerate(results, 1):
        print(f'{i}: {r}')
    heads = results.count('Heads')
    tails = results.count('Tails')
    if args.count > 1:
        print(f'\nSummary: Heads={heads}, Tails={tails}, Total={args.count}')

if __name__ == '__main__':
    main()
