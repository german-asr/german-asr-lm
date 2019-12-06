import os
import click


DATASETS = {
    'europarl': 'http://www.statmt.org/europarl/v7/de-en.tgz',
    'news_commentary': 'http://data.statmt.org/news-commentary/v14/training-monolingual/news-commentary-v14.de.gz',
    'tuda_text': 'http://ltdata1.informatik.uni-hamburg.de/kaldi_tuda_de/German_sentences_8mil_filtered_maryfied.txt.gz',
}


@click.command()
@click.argument('in_folder', type=click.Path(exists=True))
@click.argument('out_path', type=click.Path())
def run(in_folder, out_path):
    sentences = set()

    for name in DATASETS.keys():
        print('Merge {} ..'.format(name))
        src_path = os.path.join(in_folder, '{}.txt'.format(name))

        with open(src_path, 'r') as f:
            s = [l.strip() for l in f.readlines()]
            sentences.update(s)

    with open(out_path, 'w') as f:
        f.write('\n'.join(sentences))


if __name__ == '__main__':
    run()

