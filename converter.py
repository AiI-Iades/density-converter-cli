import argparse

def convert_density(value, from_unit, to_unit):
    units = {
        'kg/m³': 1,
        'g/cm³': 1000,
        'lb/ft³': 16.0185
    }
    return value * units[to_unit] / units[from_unit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert density units')
    parser.add_argument('value', type=float, help='Value to convert')
    parser.add_argument('from_unit', help='Unit to convert from')
    parser.add_argument('to_unit', help='Unit to convert to')
    args = parser.parse_args()
    result = convert_density(args.value, args.from_unit, args.to_unit)
    print(f'{args.value} {args.from_unit} = {result:.2f} {args.to_unit}')