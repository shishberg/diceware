WORDFILE = "words.txt"

def main():
    with open(WORDFILE) as f:
        words = [word.strip() for word in f.readlines()]
        assert(len(words) == 6 ** 4)
    word = iter(words)
    
    print(r"\documentclass{minimal}")
    print(r"\usepackage{multicol}")
    print(r"\begin{document}")

    for page in range(6):
        for tabrow in range(3):
            print(r"\begin{multicols}{2}")
            for tabcol in range(2):
                print(r"\begin{tabular}{ |c|c|c|c|c|c| }")
                print(r"\hline")
                for row in range(6):
                    print(*(next(word) for i in range(6)), sep=" & ", end=" \\\\\n")
                print(r"\hline")
                print(r"\end{tabular}")
                if tabcol == 0:
                    print(r"\columnbreak")

            print(r"\end{multicols}")

        print(r"\newpage")

    print(r"\end{document}")


if __name__ == "__main__":
    main()
