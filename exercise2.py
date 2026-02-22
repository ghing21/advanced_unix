def read_scores(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            acc = parts[0]
            scores = list(map(float, parts[1:]))
            combined = sum(scores)
            data.append((combined, line.strip()))
    return data

def main():
    data = read_scores("scores.txt")

    # Sort by combined score (highest first)
    data.sort(reverse=True, key=lambda x: x[0])

    # Top 10 highest
    top10 = data[:10]

    # Bottom 10 lowest
    bottom10 = data[-10:]

    # Write output
    with open("scoresextreme.txt", "w") as out:
        for score, line in top10:
            out.write(line + "\n")
        for score, line in bottom10:
            out.write(line + "\n")

if __name__ == "__main__":
    main()