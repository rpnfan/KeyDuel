import re
import glob
import os
from collections import defaultdict

# --- CONFIGURATION ---
# Change this variable to run the analysis against any number of Top N-grams
TARGET_NGRAM_LIMIT = 100
# ---------------------

def analyze_language_files(wordlist_path, ngram_path, target_limit):
    # 1. Load the 100-word list
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            full_wordlist = [w.strip().lower() for w in f.read().split() if w.strip()]
    except Exception as e:
        return f"Error: {e}"

    # 2. Aggregation Logic (Filter mid-spaces, Sum boundary variants)
    aggregated_ngrams = defaultdict(int)
    try:
        with open(ngram_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.match(r'^\s*(\d+)\s+(.+)$', line)
                if match:
                    freq = int(match.group(1))
                    raw_ngram = match.group(2).lower()
                    core = raw_ngram.strip()
                    
                    if " " not in core and core != "":
                        aggregated_ngrams[core] += freq
    except Exception as e:
        return f"Error: {e}"

    sorted_ngrams = sorted(aggregated_ngrams.items(), key=lambda x: x[1], reverse=True)
    total_internal_freq = sum(n[1] for n in sorted_ngrams)

    # Subsets to test: [First 25, First 50, First 75, Full 100]
    subsets = [25, 50, 75, 100]
    
    results = {}

    for s_size in subsets:
        current_words = full_wordlist[:s_size]
        
        # Analyze against the specific target limit provided
        subset_ngrams = sorted_ngrams[:target_limit]
        
        # Count N-grams found in this word subset
        found_count = sum(1 for ngram_core, freq in subset_ngrams if any(ngram_core in w for w in current_words))
        
        # Words Exercised (percentage of words in the CURRENT subset that contain a top N-gram)
        covered_words = sum(1 for w in current_words if any(ngram_core in w for ngram_core, freq in subset_ngrams))
        
        # Weight: Always relative to total internal language frequency
        freq_weight = (sum(n[1] for n in subset_ngrams if any(n[0] in w for w in current_words)) / total_internal_freq) * 100
        
        results[s_size] = {
            "count": found_count,
            "ngram_perc": (found_count / target_limit) * 100,
            "word_cov": (covered_words / len(current_words)) * 100,
            "freq_weight": freq_weight
        }
    return results

def main():
    wordlist_files = glob.glob("*.txt")
    md_output = f"# Language {TARGET_NGRAM_LIMIT} N-gram Analysis (Subset Comparison)\n\n"
    
    for txt_file in wordlist_files:
        lang_name = os.path.splitext(txt_file)[0]
        ngram_file = f"{lang_name}.3"
        if os.path.exists(ngram_file):
            # Pass the TARGET_NGRAM_LIMIT to the analysis function
            data = analyze_language_files(txt_file, ngram_file, TARGET_NGRAM_LIMIT)
            if isinstance(data, dict):
                md_output += f"## Language: {lang_name.capitalize()}\n"
                # Table Header dynamically updates based on the variable
                md_output += f"| Metric (tested against Top {TARGET_NGRAM_LIMIT} N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |\n"
                md_output += "| :--- | :---: | :---: | :---: | :---: |\n"
                
                counts = " | ".join([str(data[s]['count']) for s in [25, 50, 75, 100]])
                n_perc = " | ".join([f"{data[s]['ngram_perc']:.1f}%" for s in [25, 50, 75, 100]])
                w_cov = " | ".join([f"{data[s]['word_cov']:.1f}%" for s in [25, 50, 75, 100]])
                f_weight = " | ".join([f"{data[s]['freq_weight']:.1f}%" for s in [25, 50, 75, 100]])

                md_output += f"| **Found N-grams (of {TARGET_NGRAM_LIMIT})** | {counts} |\n"
                md_output += f"| **N-grams Found %** | {n_perc} |\n"
                md_output += f"| **Words Exercised %** | {w_cov} |\n"
                md_output += f"| **Corpus Coverage %** | {f_weight} |\n\n"

    filename = f"subset_analysis_n{TARGET_NGRAM_LIMIT}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_output)
    print(f"Analysis complete. Results written to {filename}")

if __name__ == "__main__":
    main()