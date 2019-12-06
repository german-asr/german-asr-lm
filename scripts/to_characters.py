import os

import click
from tqdm import tqdm
import spoteno


@click.command()
@click.argument('source_path', type=click.Path(exists=True))
@click.argument('target_path', type=click.Path())
def run(source_path, target_path):
    if not os.path.isfile(target_path):
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        print('Create character level data ...')

        with open(source_path, 'r') as f:
            sentences = [l.strip() for l in f.readlines()]

        words = set()

        for s in sentences:
            words.update(s.split(' '))

        split_words = [' '.join(list(w)) for w in words if len(w) > 1]

        with open(target_path, 'w') as f:
            f.write('\n'.join(split_words))
    else:
        print('Already character level done')


if __name__ == '__main__':
    run()

