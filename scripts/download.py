import os
import tarfile
import zipfile
import gzip
import shutil


import click
from pget.down import Downloader
from tqdm import tqdm


DATASETS = {
    'europarl': 'http://www.statmt.org/europarl/v7/de-en.tgz',
    'news_commentary': 'http://data.statmt.org/news-commentary/v14/training-monolingual/news-commentary-v14.de.gz',
    'tuda_text': 'http://ltdata1.informatik.uni-hamburg.de/kaldi_tuda_de/German_sentences_8mil_filtered_maryfied.txt.gz',
}


@click.command()
@click.argument('out_folder', type=click.Path())
def run(out_folder):
    os.makedirs(out_folder, exist_ok=True)

    tmp_folder = os.path.join(out_folder, 'tmp')
    os.makedirs(tmp_folder, exist_ok=True)

    for name, url in DATASETS.items():
        tmp_path = os.path.join(tmp_folder, name)
        target_path = os.path.join(out_folder, '{}.txt'.format(name))

        if not os.path.isfile(target_path):
            print('Download {} ...'.format(name))
            download_file(url, tmp_path)

            print('Extract {} ...'.format(name))
            extract(name, tmp_path, target_path, tmp_folder)
        else:
            print('Already downloaded - {}'.format(name))


def download_file(url, target_path):
    downloader = Downloader(url, target_path, 8)
    downloader.start()

    while downloader.total_length == 0:
        pass

    pbar = tqdm(total=downloader.total_length, desc='Download File', unit_scale=True)

    def update_pbar(x):
        pbar.update(x.total_downloaded - pbar.n)

    downloader.subscribe(update_pbar, 10)
    downloader.wait_for_finish()

    pbar.close()

def extract(name, tmp_path, target_path, tmp_folder):
    if name in ['europarl']:
        with tarfile.open(tmp_path, "r:gz") as archive:
            os.path.join(tmp_folder, 'extract_{}'.format(name))
            archive.extractall(tmp_folder)
            de_path = os.path.join(tmp_folder, 'europarl-v7.de-en.de')
            shutil.copy(de_path, target_path)
    elif name  in ['news_commentary', 'tuda_text']:
        with gzip.open(tmp_path, 'rb') as f:
            with open(target_path, 'wb') as fo:
                shutil.copyfileobj(f, fo)
    elif tarfile.is_tarfile(tmp_path):
        with tarfile.open(tmp_path, 'r') as archive:
            archive.extractall(target_path)
    elif zipfile.is_zipfile(tmp_path):
        with zipfile.ZipFile(tmp_path) as archive:
            archive.extractall(target_path)



if __name__ == '__main__':
    run()

