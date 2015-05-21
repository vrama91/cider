Consensus-based Image Description Evaluation (CIDEr Code)
===================

Evaluation code for CIDEr metric. Provies CIDEr as well as
CIDEr-D (CIDEr Defended) which is more robust to gaming effects.
## Requirements ##
- java 1.8.0
- python 2.7

## Files ##
./
- cidereval.py (demo script)

./PyDataFormat
- loadData.py (load the json files for references and candidates)

./results
- {$result_file}.json 

./pycocoevalcap: The folder where all evaluation codes are stored.
- evals.py: Performs tokenization and runs both the metrics
- tokenizer: Python wrapper of Stanford CoreNLP PTBTokenizer
- cider: CIDEr evaluation codes
- ciderD: CIDEr-D evaluation codes

## Instructions ##
1. Set path to folder containing the reference and candidate json files.
2. Sample json reference and candidate files are pascal50S.json and pascal_candsB.json
3. Ensure candidate file has one caption for each image in the reference file, and no more.
4. CIDEr scores are stored in "scores" variable

## References ##

- PTBTokenizer: We use the [Stanford Tokenizer](http://nlp.stanford.edu/software/tokenizer.shtml) which is included in [Stanford CoreNLP 3.4.1](http://nlp.stanford.edu/software/corenlp.shtml).
- CIDEr: [CIDEr: Consensus-based Image Description Evaluation] (http://arxiv.org/pdf/1411.5726.pdf)

## Developers ##
- Xinlei Chen (CMU)
- Hao Fang (University of Washington)
- Tsung-Yi Lin (Cornell)
- Ramakrishna Vedantam (Virgina Tech)

## Acknowledgement ##
- David Chiang (University of Norte Dame)
- Michael Denkowski (CMU)
- Alexander Rush (Harvard University)
