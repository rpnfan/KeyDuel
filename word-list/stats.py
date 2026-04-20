import re
import glob
import os

def analyze_language_files(wordlist_path, ngram_path):
    # 1. Load the word list (language.txt)
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            words = [w.strip().lower() for w in f.read().split() if w.strip()]
    except Exception as e:
        return f"Error reading wordlist: {e}"

    # 2. Load n-grams and frequencies (language.3)
    all_ngrams = []
    try:
        with open(ngram_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.match(r'^\s*(\d+)\s+(.+)$', line)
                if match:
                    all_ngrams.append((int(match.group(1)), match.group(2).lower()))
    except Exception as e:
        return f"Error reading n-gram list: {e}"

    if not all_ngrams:
        return "N-gram file is empty or formatted incorrectly."

    total_freq_sum = sum(n[0] for n in all_ngrams)
    limits = [100, 200, 300, 400, 500]
    results = {}

    for limit in limits:
        subset = all_ngrams[:limit]
        
        # N-gram match logic
        found_count = 0
        for freq, n in subset:
            is_match = False
            if n.startswith(' ') and n.endswith(' '):
                if any(w == n.strip() for w in words): is_match = True
            elif n.startswith(' '):
                if any(w.startswith(n.lstrip()) for w in words): is_match = True
            elif n.endswith(' '):
                if any(w.endswith(n.rstrip()) for w in words): is_match = True
            else:
                if any(n in w for w in words): is_match = True
            if is_match: found_count += 1

        # Wordlist coverage
        covered_words = 0
        for w in words:
            if any(n.strip() in w for freq, n in subset):
                covered_words += 1
                
        freq_perc = (sum(n[0] for n in subset) / total_freq_sum) * 100
        results[limit] = {
            "count": found_count,
            "ngram_perc": (found_count / limit) * 100,
            "word_cov": (covered_words / len(words)) * 100,
            "freq_weight": freq_perc
        }

    return results

def main():
    wordlist_files = glob.glob("*.txt")
    md_output = "# Language N-gram Analysis Results\n\n"
    
    for txt_file in wordlist_files:
        lang_name = os.path.splitext(txt_file)[0]
        ngram_file = f"{lang_name}.3"

        if os.path.exists(ngram_file):
            data = analyze_language_files(txt_file, ngram_file)
            
            if isinstance(data, dict):
                md_output += f"## Language: {lang_name.capitalize()}\n"
                md_output += "| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |\n"
                md_output += "| :--- | :---: | :---: | :---: | :---: | :---: |\n"
                
                # Rows
                counts = " | ".join([str(data[lim]['count']) for lim in [100,200,300,400,500]])
                n_perc = " | ".join([f"{data[lim]['ngram_perc']:.1f}%" for lim in [100,200,300,400,500]])
                w_cov = " | ".join([f"{data[lim]['word_cov']:.1f}%" for lim in [100,200,300,400,500]])
                f_weight = " | ".join([f"{data[lim]['freq_weight']:.1f}%" for lim in [100,200,300,400,500]])

                md_output += f"| **Found Count** | {counts} |\n"
                md_output += f"| **N-gram Match %** | {n_perc} |\n"
                md_output += f"| **Word Coverage %** | {w_cov} |\n"
                md_output += f"| **Freq. Weight %** | {f_weight} |\n\n"

    # Write to Markdown file
    with open("analysis_results.md", "w", encoding="utf-8") as f:
        f.write(md_output)
    
    print("Analysis complete. Results written to analysis_results.md")

if __name__ == "__main__":
    main()