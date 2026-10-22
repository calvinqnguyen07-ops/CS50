import csv
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python csv_report.py students.csv")

    try:
        with open(sys.argv[1], newline="") as file:
            reader = csv.DictReader(file)
            rows = [{"name": r["name"], "score": float(r["score"])} for r in reader]
    except FileNotFoundError:
        sys.exit("File not found")

    if not rows:
        sys.exit("No data")

    average = sum(r["score"] for r in rows) / len(rows)
    top = max(rows, key=lambda r: r["score"])

    print(f"Students: {len(rows)}")
    print(f"Average: {average:.1f}")
    print(f"Top: {top['name']} ({top['score']:.0f})")

    with open("report.csv", "w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=["name", "score", "above_average"])
        writer.writeheader()
        for r in rows:
            writer.writerow({
                "name": r["name"],
                "score": r["score"],
                "above_average": r["score"] > average,
            })

    print("Wrote report.csv")


if __name__ == "__main__":
    main()
