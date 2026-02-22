# competition/render_leaderboard.py
import csv
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "leaderboard" / "leaderboard.csv"
MD_PATH = ROOT / "leaderboard" / "leaderboard.md"
HTML_PATH = ROOT / "docs" / "leaderboard.html" # Path to your web display

def read_rows():
    if not CSV_PATH.exists():
        return []
    with CSV_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # Ensure your CSV has headers: team,model,score,timestamp_utc,notes
        rows = [r for r in reader if (r.get("team") or "").strip()]
    return rows

def main():
    rows = read_rows()
    
    # Sort: Score (descending), then Timestamp (earlier is better for ties)
    rows.sort(key=lambda r: (float(r.get("score", 0)), r.get("timestamp_utc", "")), reverse=True)

    # --- GENERATE MARKDOWN ---
    md_lines = ["# Leaderboard\n", f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n\n"]
    md_lines.append("| Rank | Team | Model | Score | Date |\n|---:|---|---|---:|---|\n")
    for i, r in enumerate(rows, start=1):
        md_lines.append(f"| {i} | {r['team']} | `{r['model']}` | {r['score']} | {r['timestamp_utc']} |\n")
    MD_PATH.write_text("".join(md_lines), encoding="utf-8")

    # --- GENERATE HTML ---
    # You can keep your existing leaderboard.js and .css by injecting just the table rows
    table_rows = "".join([
        f"<tr><td>{i+1}</td><td>{r['team']}</td><td>{r['model']}</td><td>{r['score']}</td><td>{r['timestamp_utc']}</td></tr>" 
        for i, r in enumerate(rows)
    ])
    
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head><link rel="stylesheet" href="leaderboard.css"><title>Leaderboard</title></head>
    <body>
        <h1>OctoNode Cup Leaderboard</h1>
        <table>
            <thead><tr><th>Rank</th><th>Team</th><th>Model</th><th>Score</th><th>Date</th></tr></thead>
            <tbody>{table_rows}</tbody>
        </table>
    </body>
    </html>
    """
    HTML_PATH.write_text(html_template, encoding="utf-8")

if __name__ == "__main__":
    main()
