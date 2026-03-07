# exercise9.py

def read_top10(filename):
    top10 = []  # list of (score, line)

    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            acc = parts[0]
            scores = list(map(float, parts[1:]))
            combined = sum(scores)

            # If we have fewer than 10 entries, just add it
            if len(top10) < 10:
                top10.append((combined, line.strip()))
                continue

            # Otherwise find the current minimum in top10
            min_score = min(top10, key=lambda x: x[0])

            # If the new score is better, replace the minimum
            if combined > min_score[0]:
                top10.remove(min_score)
                top10.append((combined, line.strip()))

    return top10


def main():
    top10 = read_top10("scores.txt")

    # Sort final top10 before writing
    top10.sort(reverse=True, key=lambda x: x[0])

    with open("scoresextreme.txt", "w") as out:
        for score, line in top10:
            out.write(line + "\n")


if __name__ == "__main__":
    main()