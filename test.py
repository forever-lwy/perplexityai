from perplexity import Perplexity

perplexity = Perplexity("example@email.com")
answer = perplexity.search("What is the meaning of life?")
for a in answer:
    print(a)
perplexity.close()
