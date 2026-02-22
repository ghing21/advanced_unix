# exercise4.py

def load_negative_list(filename):
    banned = set()
    with open(filename, "r") as f:
        for line in f:
            banned.add(line.strip())
    return banned

def load_translation(filename):
    mapping = {}
    with open(filename, "r") as f:
        for line in f:
            acc, swiss = line.strip().split("\t")
            mapping[acc] = swiss
    return mapping

def read_scores(filename, banned, translation):
    data = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            acc = parts[0]

            # Skip if accession not in translation table
            if acc not in translation:
                continue

            swiss = translation[acc]

            # Skip banned SwissProt IDs
            if swiss in banned:
                continue

            # Dynamically read ALL score columns
            try:
                scores = list(map(float, parts[1:]))
            except ValueError:
                continue  # skip malformed lines

            combined = sum(scores)
            data.append((combined, line.strip()))
    return data

def main():
    banned = load_negative_list("negative_list.txt")
    translation = load_translation("translation.txt")
    data = read_scores("scores.txt", banned, translation)

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