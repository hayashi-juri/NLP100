import warnings

# 警告を非表示にする
warnings.filterwarnings("ignore", category=FutureWarning)

import treetaggerwrapper as ttw # type: ignore

def main():
    tagger = ttw.TreeTagger(TAGLANG='de', TAGPARFILE = '/home/juri/treetagger/lib/german.par')
    tags = tagger.TagText('Das ist ein Test.')
    print(tags)

if __name__ == '__main__':
    main()
