import nltk
# nltk.download()
# 除了WordPunct tokenizer之外，NLTK中还提供有另外三个分词方法，TreebankWordTokenizer，PunktWordTokenizer和WhitespaceTokenizer
# 对于比较复杂的词型，需要借助正则表达式的强大能力来完成分词任务，使用的函数是regexp_tokenize()

from nltk.tokenize import WordPunctTokenizer

text1 = "Are you old enough to remember Michael Jackson"
words = WordPunctTokenizer().tokenize(text1)
print(words)

text2 = 'That U.S.A. poster-print costs $12.40...'
print(WordPunctTokenizer().tokenize(text2)) # incorrect result

pattern = r"""(?x)                   # set flag to allow verbose regexps
              (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A.
              |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages
              |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe
              |\.\.\.                # ellipsis
              |(?:[.,;"'?():-_`])    # special characters with meanings
            """

print(nltk.regexp_tokenize(text2, pattern))
