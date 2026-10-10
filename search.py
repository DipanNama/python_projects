#!/usr/bin/env python3
"""Binary search on sorted integers. Returns the first match and a step trace."""
import argparse
import json

def search(numbers, target):
    if not isinstance(numbers, list) or not numbers or len(numbers) > 64:
        raise ValueError('Use 1 to 64 sorted integers')
    if any(type(n) is not int or abs(n) > 1000000 for n in numbers) or type(target) is not int or abs(target) > 1000000:
        raise ValueError('Use integers between -1000000 and 1000000')
    if any(a > b for a, b in zip(numbers, numbers[1:])):
        raise ValueError('Numbers must be sorted in ascending order')
    low, high, found, steps = 0, len(numbers) - 1, -1, []
    while low <= high:
        mid = (low + high) // 2
        value = numbers[mid]
        relation = 'equal' if value == target else ('lower' if value < target else 'higher')
        steps.append({'low': low, 'high': high, 'mid': mid, 'value': value, 'relation': relation})
        if value < target:
            low = mid + 1
        else:
            if value == target:
                found = mid
            high = mid - 1
    return {'index': found, 'steps': steps}

def cli():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('numbers', help='Comma-separated sorted integers')
    parser.add_argument('target', type=int)
    args = parser.parse_args()
    try:
        numbers = [int(n.strip()) for n in args.numbers.split(',')]
        print(json.dumps(search(numbers, args.target), indent=2))
    except ValueError as e:
        parser.exit(1, f'Error: {e}\n')

if __name__ == '__main__':
    cli()
