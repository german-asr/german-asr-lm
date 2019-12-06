# Language Models for German ASR

This repository contains scripts to train German language models.
Check licenses on the sites of the specific datasets, if you want use the these language models.

## Data Sources

| Name                 | Num. Sentences | Site                                                                              |
| -------------------- | -------------- | --------------------------------------------------------------------------------- |
| EuroParl             | 1920208        | http://www.statmt.org/europarl/                                                   |
| News-Commentary      | 383764         | https://www.statmt.org/wmt13/translation-task.html                                |
| Tuda-Text            | 7776674        | https://www.inf.uni-hamburg.de/en/inst/ab/lt/resources/data/acoustic-models.html  |

## Reproduce
In order to reproduce the language models, first the data has to be prepared. The required commands can be found in ``prepare_data.sh``.

### kenlm
For n-gram language models, [kenlm](https://github.com/kpu/kenlm) is used.

## Trained Models
Trained models can be found in the attachements of the releases.
