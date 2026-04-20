import os
import glob

csv_files = glob.glob("*.csv")
print(f"Processing {len(csv_files)} CSV files...")

for filename in csv_files:
    print(f"\n{filename} -> {os.path.splitext(filename)[0]}.txt")
    
    output_file = os.path.splitext(filename)[0] + '.txt'
    
    words = []
    try:
        with open(filename, 'r', encoding='utf-8', errors='replace') as f:
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line or i == 1:  # Skip empty/header
                    continue
                parts = line.split(';')
                if len(parts) >= 2:
                    word = parts[1].strip()
                    if word:  # Skip empty words
                        words.append(word)
    except Exception as e:
        print(f"  Error: {e}")
        continue
    
    # Join ALL words with spaces, single line
    if words:
        content = ' '.join(words) + '\n'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ {len(words)} words -> {output_file}")
    else:
        print(f"  No words found")

print("\nDone! Check: type *.txt")