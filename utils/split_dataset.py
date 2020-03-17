import pandas as pd
import re

dataset_filename = "/data/dataset/weibo_meizhuang/dwd_weibo_meizhuang_class_dataset.csv"


def remove_at(line):
    res = re.sub(r"\@.+( |$)", "", line)
    return res


def remove_whitespace(line):
    res = re.sub(r"(\t| |\n)+", "", line)
    return res


def remove_end_more(line):
    res = re.sub(r"...全文$", "", line)
    return res


def remove_repost(line):
    res = re.sub(r"//.*$", "", line)
    return res


def remove_short_text(line):
    res = '' if len(line.strip()) <= 4 else line.strip()
    return res


def clean_text(line):
    res = remove_at(line)
    res = remove_whitespace(res)
    res = remove_repost(res)
    res = remove_short_text(res)
    return res.strip()


if __name__ == "__main__":
    res = clean_text('哈哈哈 @abc @bcd ...全文')
    print(res)
    df = pd.read_csv(dataset_filename)
    df['raw_text'] = df['text']
    df['text'] = df[['raw_text']].apply(lambda x: clean_text(x[0]), axis=1)

    df_copy = df.drop(df[df['text']==''].index)
    train_dev_set = df_copy.sample(frac=0.8, random_state=0)
    test_set = df_copy.drop(train_dev_set.index)
    dev_set = train_dev_set.sample(frac=0.1, random_state=0)
    train_set = train_dev_set.drop(dev_set.index)
    print("#train=%d\n#dev=%d\n#test=%d" % (train_set.shape[0], dev_set.shape[0], test_set.shape[0]))
    train_set[['guid', 'label', 'label', 'text']].to_csv('../data/train.tsv', sep='\t', index=False, header=False)
    dev_set[['guid', 'label', 'label', 'text']].to_csv('../data/dev.tsv', sep='\t', index=False, header=False)

    test_set['id'] = test_set['guid']
    test_set[['id', 'text', 'label']].to_csv('../data/test.tsv', sep='\t', index=False, header=True)
