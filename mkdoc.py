WORDFILE = "words.txt"
SIX = range(6)

def main():
    with open(WORDFILE) as f:
        words = [word.strip() for word in f.readlines()]
        assert(len(words) == 6 ** 4)
    word = iter(words)
    
    print(r"\documentclass[a4paper,10pt,]{article}")
    print(r"\usepackage[lmargin=3cm]{geometry}")
    print(r"\pagestyle{empty}")
    print(r"\begin{document}")
    print(r"\begin{flushleft}")

    for page in SIX:
        for tabcol in SIX:
            tabwords = [[next(word) for _ in SIX] for _ in SIX]
            print(r"\begin{tabular}{ |" + "|".join(["p{6em}"] * 6) + "| }")
            print(r"\hline")
            print(*(r"\textbf{%d%d%d}" % (page+1, tabcol+1, i+1) for i in SIX), sep=" & ", end=" \\\\\n")
            print(r"\hline")
            for tabrow in SIX:
                print(*(r"\textbf{%d} %s" % (tabrow+1, tabwords[i][tabrow]) for i in SIX), sep=" & ", end=" \\\\\n")
            print(r"\hline")
            print(r"\end{tabular}")
            print(r"\\")

        print(r"\newpage")

    print(r"\end{flushleft}")
    print(r"\end{document}")


if __name__ == "__main__":
    main()
