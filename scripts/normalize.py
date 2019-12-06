import os

import click
from tqdm import tqdm
import spoteno


DATASETS = {
    'europarl': 'http://www.statmt.org/europarl/v7/de-en.tgz',
    'news_commentary': 'http://data.statmt.org/news-commentary/v14/training-monolingual/news-commentary-v14.de.gz',
    'tuda_text': 'http://ltdata1.informatik.uni-hamburg.de/kaldi_tuda_de/German_sentences_8mil_filtered_maryfied.txt.gz',
}


@click.command()
@click.argument('in_folder', type=click.Path(exists=True))
@click.argument('out_folder', type=click.Path())
def run(in_folder, out_folder):
    os.makedirs(out_folder, exist_ok=True)

    normalizer = spoteno.Normalizer.de(num_workers=4)

    for name in DATASETS.keys():
        src_path = os.path.join(in_folder, '{}.txt'.format(name))
        target_path = os.path.join(out_folder, '{}.txt'.format(name))

        if not os.path.isfile(target_path):
            print('Normalize {} ...'.format(name))

            with open(src_path, 'r') as f:
                sentences = [l.strip() for l in f.readlines()]

            cleaned = normalizer.normalize_list(sentences)

            with open(target_path, 'w') as f:
                f.write('\n'.join(cleaned))
        else:
            print('Already Normalized  - {}'.format(name))


if __name__ == '__main__':
    run()

