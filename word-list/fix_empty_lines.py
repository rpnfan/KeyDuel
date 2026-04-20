import os
import glob
import csv

csv_files = glob.glob("*.csv")
print(f"Found {len(csv_files)} files: {[os.path.basename(f) for f in csv_files]}")

for filename in csv_files:
    print(f"\nProcessing: {filename}")
    
    # Backup
    backup = filename + '.clean.bak'
    os.rename(filename, backup)
    
    # Read as CSV rows (handles quoted newlines/escapes properly)
    rows = []
    with open(backup, 'r', encoding='utf-8', errors='replace') as f:
        try:
            reader = csv.reader(f)
            for row in reader:
                # Skip fully empty rows
                if any(cell.strip() for cell in row):
                    rows.append(row)
        except Exception as e:
            print(f"  CSV parse error: {e} - falling back to lines")
            # Fallback: line-based
            with open(backup, 'r', encoding='utf-8', errors='replace') as f2:
                lines = f2.readlines()
            rows = [line for line in lines if line.strip()]
    
    # Write back clean
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    print(f"✓ Cleaned {len(rows)} non-empty rows in {filename}")
    print(f"  Original backup: {backup}")

print("\nDone. Verify with: type yourfile.csv")