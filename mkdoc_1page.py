WORDFILE = "words.txt"
SIX = range(6)

def main():
    with open(WORDFILE) as f:
        words = [word.strip() for word in f.readlines()]
        assert(len(words) == 6 ** 4)
    word = iter(words)
    tabwords = [[[[next(word) for _ in SIX] for _ in SIX] for _ in SIX] for _ in SIX]
    
    print(r"\documentclass[a4paper]{article}")
    print(r"\usepackage[lmargin=2.2cm,tmargin=1cm,rmargin=1cm,bmargin=1cm]{geometry}")
    print(r"\pagestyle{empty}")
    print(r"\begin{document}")
    print(r"\begin{flushleft}")
    print(r"\tiny")
    print(r"\setlength{\tabcolsep}{1pt}")

    for d0 in range(0, 6, 2):
        colwidths = "|".join(["p{5.5em}"] * 6)
        print(r"\begin{tabular}{ |%s|p{0.1em}|%s| }" % (colwidths, colwidths))
        for d1 in range(6):
            print(r"\hline")
            print(*(r"\textbf{%d%d%d}" % (d0+1, d1+1, (d2%6)+1) for d2 in range(6)), sep=" & ", end=" ")
            print(" & & ", end="")
            print(*(r"\textbf{%d%d%d}" % (d0+2, d1+1, (d2%6)+1) for d2 in range(6)), sep=" & ", end=" \\\\\n")
            print(r"\hline")
            for d3 in range(6):
                print(*(r"\textbf{%d} %s" % (d3+1, tabwords[d0+0][d1][d2%6][d3]) for d2 in range(6)), sep=" & ", end=" ")
                print(" & & ", end="")
                print(*(r"\textbf{%d} %s" % (d3+1, tabwords[d0+1][d1][d2%6][d3]) for d2 in range(6)), sep=" & ", end=" \\\\\n")
        
        print(r"\hline")
        print(r"\end{tabular}")
        print(r"\\")

    print(r"\end{flushleft}")
    print(r"\end{document}")


if __name__ == "__main__":
    main()
