import re
import glob
import os
from collections import defaultdict

# --- CONFIGURATION ---
# Change this to any list (e.g., [100, 500, 1000]) to adjust the scope of the analysis
TARGET_LIMITS = [100, 200, 300, 400, 500]
# ---------------------

def clean_ngram(raw_text):
    """
    Strips whitespace, commas, periods, and numbers.
    Returns None if the resulting string has internal spaces or is empty.
    """
    # Remove commas, periods, and numbers as requested
    cleaned = re.sub(r'[,.0-9]', '', raw_text)
    # Strip leading/trailing whitespace
    core = cleaned.strip().lower()
    
    # Validation: If it's empty or contains internal spaces (like "d e"), discard
    if not core or " " in core:
        return None
    return core

def analyze_language_files(wordlist_path, ngram_path):
    # 1. Load the 100-word list
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            words = [w.strip().lower() for w in f.read().split() if w.strip()]
    except Exception as e:
        return f"Error: {e}"

    # 2. Aggregation Logic
    aggregated_ngrams = defaultdict(int)
    try:
        with open(ngram_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.match(r'^\s*(\d+)\s+(.+)$', line)
                if match:
                    freq = int(match.group(1))
                    raw_ngram = match.group(2)
                    
                    # Clean the n-gram using the specific filtering rules
                    clean_core = clean_ngram(raw_ngram)
                    
                    if clean_core:
                        # Summing variants into one core (e.g., " en", "en ", "en")
                        aggregated_ngrams[clean_core] += freq
    except Exception as e:
        return f"Error: {e}"

    # 3. Sort by cumulative frequency
    sorted_ngrams = sorted(aggregated_ngrams.items(), key=lambda x: x[1], reverse=True)
    total_internal_freq = sum(n[1] for n in sorted_ngrams)

    results = {}
    for limit in TARGET_LIMITS:
        subset_ngrams = sorted_ngrams[:limit]
        
        # Potential: The total weight of these Top N patterns in the language
        potential_freq = sum(n[1] for n in subset_ngrams)
        
        # Actual: Weight of patterns from this Top N actually in your list
        found_count = sum(1 for ngram_core, freq in subset_ngrams if any(ngram_core in w for w in words))
        
        # Word Coverage: How many of the 100 words hit a pattern in this Top N
        covered_words = sum(1 for w in words if any(n[0] in w for n in subset_ngrams))
        
        # Actual Coverage Weight
        actual_freq_sum = sum(freq for ngram_core, freq in subset_ngrams if any(ngram_core in w for w in words))
                
        results[limit] = {
            "found_count": found_count,
            "ngram_match_perc": (found_count / limit) * 100,
            "word_cov": (covered_words / len(words)) * 100,
            "potential_weight": (potential_freq / total_internal_freq) * 100,
            "actual_coverage": (actual_freq_sum / total_internal_freq) * 100,
            "efficiency": (actual_freq_sum / potential_freq * 100) if potential_freq > 0 else 0
        }
    return results

def main():
    wordlist_files = glob.glob("*.txt")
    md_output = "# KeyDuel Statistical Validation\n\n"
    
    for txt_file in wordlist_files:
        lang_name = os.path.splitext(txt_file)[0]
        ngram_file = f"{lang_name}.3"
        if os.path.exists(ngram_file):
            print(f"Processing {lang_name}...")
            data = analyze_language_files(txt_file, ngram_file)
            if isinstance(data, dict):
                md_output += f"### Language: {lang_name.capitalize()}\n"
                
                # Dynamic Table Headers based on TARGET_LIMITS
                headers = [f"n={lim}" for lim in TARGET_LIMITS]
                md_output += f"| Metric | {' | '.join(headers)} |\n"
                md_output += f"| :--- | {' | '.join([':---:'] * len(TARGET_LIMITS))} |\n"
                
                rows = {
                    "N-grams Found": [str(data[lim]['found_count']) for lim in TARGET_LIMITS],
                    "N-grams Found %": [f"{data[lim]['ngram_match_perc']:.1f}%" for lim in TARGET_LIMITS],
                    "Words Exercised %": [f"{data[lim]['word_cov']:.1f}%" for lim in TARGET_LIMITS],
                    "Potential Core Weight": [f"{data[lim]['potential_weight']:.1f}%" for lim in TARGET_LIMITS],
                    "Corpus Coverage": [f"{data[lim]['actual_coverage']:.1f}%" for lim in TARGET_LIMITS],
                    "List Efficiency": [f"{data[lim]['efficiency']:.1f}%" for lim in TARGET_LIMITS]
                }
                for label, values in rows.items():
                    md_output += f"| **{label}** | {' | '.join(values)} |\n"
                md_output += "\n"

    with open("keyduel_efficiency_report.md", "w", encoding="utf-8") as f:
        f.write(md_output)
    print("Report generated successfully.")

if __name__ == "__main__":
    main()