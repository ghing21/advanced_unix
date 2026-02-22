# exercise7.py

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

            # Convert all remaining columns to floats (dynamic number)
            scores = list(map(float, parts[1:]))

            N = len(scores)
            weighted_sum = 0.0

            # Sliding weight: first score 1.5, last score 0.5
            for P, value in enumerate(scores, start=1):
                if N > 1:
                    W = 1.5 - (P - 1) / (N - 1)
                else:
                    W = 1.0  # edge case: only one score
                weighted_sum += value * W

            data.append((weighted_sum, line.strip()))
    return data

def main():
    banned = load_negative_list("negative_list.txt")
    translation = load_translation("translation.txt")

    data = read_scores("scores.txt", banned, translation)

    # Sort by weighted score (highest first)
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