# KeyDuel — Try Out Your Layout

**Test two layouts. Compare comfort. Pick your winner.**

KeyDuel is a systematic approach to compare two layouts in terms of subjective typing comfort. The basic idea is to "translate" an alternative layout you consider to learn into the key positions of the layout you are currently using for touch-typing. A list of carefully selected test words allows you to get a much more meaningful and representative impression about how a layout will feel in real-world use, than using typing random sentences.

<img width="2404" height="1009" alt="image" src="https://github.com/user-attachments/assets/08b95e2e-d4e6-4d16-8276-e378f0f35fc9" />


## 1. Purpose and High-Level Approach

The goal is to **compare perceived typing comfort between two keyboard layouts** — which layout feels more natural and effortless when typing real words in a given language. This is a *subjective comparative* test, not an objective speed or accuracy measurement.

The method combines three principles drawn from existing layout evaluation practice:

- **Linguistic frequency** — words that appear most often in real text should dominate the score, because that is where a layout spends most of its effort
- **Typing-relevant word shapes** — the word set must cover both short function words, which include the most frequent words and therefore are vital to exhibit typical finger patterns (same-finger bigrams, scissors, lateral reach and redirects). But also longer content words need to be included better exhibiting alternation and roll patterns. 
- **Practical test ergonomics** — sessions must be short enough to complete without fatigue, yet representative enough to give a meaningful result

Two test modes are provided:

| Mode | Words | Purpose |
|---|---|---|
| **Quick check** | 25 | Plausibility check — decide whether to proceed to the full test |
| **Full evaluation** | 100  (25 + 75) | Complete comparative assessment |



## 2. Scope and Limitations

KeyDuel measures **perceived typing comfort**, the subjective feeling of typing each word, not speed or accuracy. Speed tests on typing trainers measure how well you have learned a layout, not how comfortable it is. After a few weeks on any layout you will reach acceptable speed; comfort is the more durable and more personal variable. Used honestly, KeyDuel gives you real signal about comfort differences that survive the initial adaptation period.

Further limitations to be aware of:

- **Adaptation is not controlled.** A layout you have used for years will feel more natural regardless of its ergonomic properties. For a meaningful comparison, it is important to try separate the ergonomic feel of a layout from how familiar you are with it. The How-To section will give guidance how to achieve that.
- **Individual anatomy is not accounted for.** Hand size, finger proportions, keyboard type, keycaps, your typing posture and more all affect comfort. Results from a single tester should not be generalised. But for yourself the results are fully valid.
- **Language mix is not tested.** The lists are single-language. If you regularly type in multiple languages, no single list fully represents your typing. 



## 3. How to Use KeyDuel

KeyDuel uses two components: a word list you type using a layout try-out tool, and a spreadsheet where you record your ratings.

### 1. Set up the layout try-out tool

Open [keyboard-layout-try-out.pages.dev](https://keyboard-layout-try-out.pages.dev/) and configure it to translate your target layout into the key positions of your current layout. This lets you type in the new layout without having learned it. Copy and paste the word-list of the language for which you are evaluating the new layout.

### 2. Download the scoring spreadsheet

The spreadsheet is available for Excel and Google Sheets:

**[→ KeyDuel Scoring Spreadsheet](https://docs.google.com/spreadsheets/d/1DUxuv2yWy9Cx_WR_3aSm7ectGyZmEQ8_/edit?usp=sharing&ouid=113030593881581675606&rtpof=true&sd=true)**

Delete the example ratings and enter the names of the two layouts you are comparing. The spreadsheet is pre-loaded with the English word list and calculates your weighted score automatically.

### 3. Run the quick check (25 words)

Start with the first 25 words. For each word, type it several times on layout A, then several times on layout B. Focus entirely on the finger movements. Forget the word itself and concentrate on how the motion feels. Practice each word until you have the finger-pattern engrained.

Especially for longer words it can happen that the first few characters type better in layout A, but another part of the finger-pattern is better on layout B. If that is the case you have to count how many partial finger-patterns are better in each layout. Use the same rating (see below) for the partial word evaluation and finally sum the total rating for the word:

| Rating | Meaning |
|:---:|---|
| +2 | Layout A clearly more comfortable |
| +1 | Layout A slightly more comfortable |
| 0 | No perceptible difference |
| −1 | Layout B slightly more comfortable |
| −2 | Layout B clearly more comfortable |

The spreadsheet is configured so that layout A (displayed in blue) is the layout you are evaluating. Layout B (displayed in red) is the layout you are fluent in. 

Continue word for word till you completed the short test with 25 words. If the result after 25 words is already very clear, you can stop here. If the difference is small or ambiguous, continue with the remaining 75 words for the full evaluation.

### 4. Interpret your score

The spreadsheet calculates a normalized score between −1 and +1. A score close to zero means no meaningful difference was detected. When you evaluate more than one layout you will get a feeling how the normalized score, displayed in percent in the spreadsheet translates to larger or smaller perceived differences between the layouts.

There are two ratings shown. The first is the rating without taking the weighting taken into account. This will tell you the which layout will feel better for the word list. The second "Frequency weighted score" takes into account how often a test word occurs roughly in a real world text. Both scores tell you something, but the frequency weighted is the more meaningful, because it gives you an indication how often the layout differences will play out in day-to-day typing.

> **Note:** A more detailed walkthrough with screenshots is planned. The current spreadsheet already contains a worked example — a comparison of anymak:END and Graphite — which illustrates how to fill it in.




## 4. Why Word Selection Matters

Keyboard layout differences are not uniform across all words. Whether one layout outperforms another on a given word depends on:

- **Which keys are used** and whether they fall on strong or weak fingers
- **Hand alternation** — layouts typically optimise for alternating keystrokes between hands
- **Same-finger bigrams** — consecutive letters typed by the same finger are the largest single source of discomfort and slowness
- **Row usage and lateral reach** — how much vertical and horizontal finger travel is required
- **Hand load balance** — whether one hand carries a disproportionate share of a word

A list dominated entirely by two-letter function words (*in, of, at*) would stress alternation but barely exercise finger travel. A list of only long technical words would stress movement but miss everyday rhythm. An effective test list must deliberately cover both dimensions.

This is why a raw corpus frequency list — simply the N most common words — is insufficient. The top 100 most frequent words in any language skew heavily toward very short function words, testing only one narrow slice of the ergonomic space. The tiered structure corrects for this.



## 5. The Four-Tier Word Pool

Every 100-word list is organised into four tiers. The tiers serve both a *linguistic classification* purpose and a *scoring weight* purpose.

### Tier A — Very high-frequency function words (weight 1.0)

Articles, prepositions, conjunctions, pronouns, and auxiliary verbs. Examples: *the, and, in, to, of, with, have, is* (English); *der, und, in, ich, ist, mit* (German); *de, en, in, het, is, zijn* (Dutch).

**Why include them:** These words constitute the statistical backbone of any language. In typical prose they account for a disproportionately large share of all keystrokes. Their short length means they are typed rapidly in tight succession, stressing hand alternation rhythm heavily.

**Why weight 1.0:** Their dominance in real text means a layout's handling of them has the greatest impact on everyday comfort.

### Tier B — Common content words (weight 0.6)

High-frequency nouns, adjectives, and common adverbs that appear across many topics: *people, time, world, life, good, right, new* (English); *Zeit, Leben, Welt, Arbeit, Leute* (German); *mensen, tijd, wereld, werk* (Dutch).

**Why include them:** These words carry meaning and appear across virtually any text a person writes. At 4–8 letters they exercise a broader range of finger movements and same-finger bigrams than the very short Tier A words. They reflect realistic typing without being domain-specific.

**Why weight 0.6:** Frequent and important, but less dominant than function words on a per-keystroke basis.

### Tier C — Verb forms and morphological variants (weight 0.3)

Common verbs in inflected or gerund forms: *working, making, getting, thinking* (English); *machen, kommen, finden, brauchen* (German); *maken, werken, denken, gaan* (Dutch).

**Why include them:** Inflected verb forms often produce consonant clusters and letter combinations that stress same-finger behaviour differently from root forms. A layout may handle *work* comfortably but create a collision on *working*. Including inflected and infinitive forms exposes these differences. In morphologically rich languages (Finnish, Turkish, Polish, Russian) this tier is proportionally larger because verb inflection is more extensive and more diagnostic.

**Why weight 0.3:** These words are less frequent than Tier A/B, and tester rating variance at this level is comparable in magnitude to the actual per-word frequency differences. Higher weighting would add noise without adding meaningful signal.

### Tier D — Lower-frequency but structurally diagnostic words (weight 0.1)

Longer nouns and abstract terms: *different, important, information, government, question, example* and their equivalents in each language.

**Why include them:** Long words stress finger travel, lateral reach, and same-finger avoidance in ways that short words cannot. A layout that optimises the home row for common letters may do so at the cost of uncomfortable reach sequences in longer words. A small number of long words guards against this blind spot and adds length variety to the test.

**Why weight 0.1:** These words are infrequent in everyday text. They are present for diagnostic purposes — to catch layout weaknesses that would otherwise be invisible — but must not dominate the score.



## 6. English Word List — Example

The table below shows an excerpt of the English 100-word list with tier assignments. Rows 1–25 form the fixed quick-check subset; rows 26–100 are the interleaved evaluation body.

| # | Word | Weight | Note |
|---|---|---|---|
| 1 | the | 1.0 | |
| 2 | and | 1.0 | |
| 3 | in | 1.0 | |
| 4 | to | 1.0 | |
| 5 | of | 1.0 | |
| 6 | is | 1.0 | |
| 7 | with | 1.0 | |
| 8 | that | 1.0 | |
| 9 | have | 1.0 | |
| 10 | you | 1.0 | |
| 11 | people | 0.6 | |
| 12 | time | 0.6 | |
| 13 | good | 0.6 | |
| 14 | world | 0.6 | |
| 15 | because | 0.3 | |
| 16 | working | 0.3 | |
| 17 | when | 0.6 | |
| 18 | some | 0.6 | |
| 19 | just | 0.6 | |
| 20 | life | 0.6 | |
| 21 | making | 0.3 | |
| 22 | new | 0.6 | |
| 23 | right | 0.6 | |
| 24 | can | 0.6 | |
| 25 | getting | 0.3 | ← end of quick-check subset |
| … | *rows 26–49: Tier A/B/C interleaved* | | |
| 50 | at | 1.0 | |
| 51 | more | 0.6 | |
| 52 | having | 0.3 | |
| … | *rows 53–74: Tier A/B/C interleaved* | | |
| 75 | well | 0.6 | |
| 76 | keep | 0.3 | |
| 77 | by | 1.0 | |
| … | *rows 78–94: Tier A/B/C interleaved* | | |
| 95 | different | 0.1 | ← Tier D begins |
| 96 | important | 0.1 | |
| 97 | information | 0.1 | |
| 98 | government | 0.1 | |
| 99 | question | 0.1 | |
| 100 | example | 0.1 | |

*Rows 1–25: fixed quick-check subset. Within the subset, Tier C words appear at positions 15, 16, 21, 25 to ensure length variety from the start. Rows 26–94: Tier A/B/C words interleaved. Rows 95–100: Tier D diagnostic words.*



## 7. Tier Composition Across All 14 Languages

The number of words per tier varies by language because linguistic structures differ. Languages with rich morphology (Finnish, Turkish, Polish, Russian) carry more Tier C words. Languages with heavy function-word usage (French, German, English) carry more Tier A words.

| Language | Tier A (1.0) | Tier B (0.6) | Tier C (0.3) | Tier D (0.1) |
|---|:---:|:---:|:---:|:---:|
| English | 28 | 39 | 27 | 6 |
| German | 37 | 37 | 21 | 5 |
| Dutch | 27 | 54 | 13 | 6 |
| French | 35 | 42 | 17 | 6 |
| Spanish | 28 | 50 | 16 | 6 |
| Italian | 20 | 58 | 16 | 6 |
| Portuguese | 27 | 50 | 17 | 6 |
| Polish | 14 | 62 | 18 | 6 |
| Russian | 25 | 47 | 23 | 5 |
| Norwegian | 19 | 55 | 21 | 5 |
| Swedish | 21 | 52 | 22 | 5 |
| Danish | 19 | 55 | 21 | 5 |
| Finnish | 17 | 52 | 25 | 6 |
| Turkish | 17 | 47 | 32 | 4 |

The variation is intentional and linguistically sound. A fixed tier distribution imposed on all languages would either distort word selection or produce lists that do not reflect actual usage patterns in those languages.



## 8. The 25-Word Quick-Check Subset

The first 25 rows of every list form the quick-check subset. They are deliberately composed to be predictive of the full test result.

**Composition:** approximately 60–70% Tier A/B words and 30–40% Tier C words. The subset must independently stress both the alternation/rhythm dimension (via short function words) and the finger-travel dimension (via longer content words and verb forms).

**Ordering:** the 25 words are presented in mixed order — not sorted by frequency or length. Longer words are distributed across positions 12–25 rather than clustered at the end. This ensures the quick run exercises layout stress points from early on, making it genuinely predictive.

**Purpose:** a tester who finds no meaningful difference after 25 words can stop. A tester who finds a clear preference has an early signal to confirm with the full test. The quick-check result is a *filter*, not a standalone measurement.



## 9. Ordering of the Full 100-Word List

```
Rows  1–25    Fixed quick-check subset (identical across all test instances)
Rows 26–94    Tier A/B/C words interleaved, fixed seed per language
Rows 95–100   Tier D diagnostic words (long words, placed at end)
```

**The quick subset is fixed** to ensure that results from different testers and sessions are directly comparable. Every tester encounters exactly the same 25 words in the same order for the quick check.

**Rows 26–94 are interleaved** so that the tester experiences a consistent mix of short function words and longer content words throughout the session, rather than a block of one type followed by another. Tiers are interleaved under a mathematically computed constraint: no single tier repeats more than its optimal maximum — typically 3 consecutive words for most languages, 4 for languages where Tier B is very dominant (Italian, Polish). Within each tier, words are placed in a fixed-seed randomised order, ensuring variety of specific words even though the tier pattern is regular.

**Tier D words are placed at the end** because the long diagnostic words would create a disproportionately strong first impression if placed early.

**The fixed seed** per language ensures that the ordering is reproducible. Different test instances for the same language always present the same word sequence, which is a deliberate design choice for this instrument: the test is always run in the same fixed order, so results across testers and sessions are directly comparable without needing to record or transmit the randomised sequence.



## 10. Scoring Formula

Each word receives a rating from the tester on a five-point scale:

| Rating | Meaning |
|:---:|---|
| +2 | Original layout clearly more comfortable |
| +1 | Original layout slightly more comfortable |
| 0 | No perceptible difference |
| −1 | New layout slightly more comfortable |
| −2 | New layout clearly more comfortable |

The normalized score is:

$$\text{Normalized score} = \frac{\displaystyle\sum_{i=1}^{100} \left(\text{rating}_i \times \text{weight}_i\right)}{2 \times \displaystyle\sum_{i=1}^{100} \text{weight}_i}$$

Result range **[−1, +1]**:

- **+1.0** — original layout clearly preferred on every word
- **0.0** — no net preference
- **−1.0** — new layout clearly preferred on every word

The denominator normalises by twice the total weight because the maximum absolute rating is 2. Dividing by 2 × Σweight scales the result to [−1, +1] regardless of tier distribution.

**Why grouped weights are sufficient:** The dominant source of variance in subjective comfort ratings is the tester's own perception from trial to trial. Four tiers capture the signal that matters — function words dominate real typing, rare words do not — while keeping the method robust, transparent, and reproducible.

> The evalution spreadsheet shows both an unweighted and a frequency-weighted score, the latter is the more meaningful for day-to-day typing.



## 11. Methodology Discussion


### Why This Approach Rather Than Alternatives

The goal of the curated word list is to provide a meaningful representation of the language. This approach was chosen instead of simpler options:

**Versus raw corpus frequency lists:** Top-100 frequency lists are dominated by very short function words, testing only one narrow slice of the ergonomic space. The tiered approach rebalances the list to be ergonomically representative.

**Versus N-gram frequency optimisation:** Selecting words to reproduce the letter bigram and trigram distribution of a corpus maximises statistical representativeness of letter sequences but does not reflect word-level or rhythm-level typing experience. The tiered approach was preferred because a human tester rates whole words as typed units, not letter sequences in isolation.

**Versus sentence-based or synthetic text tests:** Full sentences introduce syntactic parsing and reading comprehension workload, which can obscure pure motor comfort assessments. Isolated words keep cognitive load minimal and the typing signal cleaner.


### N-gram Coverage Analysis

To ensure the KeyDuel word list is a high-fidelity proxy for real-world typing, each language list was validated using a custom N-gram analysis. This process measures how many of the language's most frequent "finger motions" are exercised by the 100 test words.



#### 1. Why this analysis was done
The validity of KeyDuel rests on the assumption that typing 100 specific words can simulate the "feel" of typing an entire language. We needed to verify:
* **Density:** Do the most frequent letter combinations (bigrams/trigrams) actually appear in our 100 words?
* **Efficiency:** Does the list "cover" enough of the language's statistical weight to be a valid diagnostic tool?


#### 2. Filtering of the 3-grams list

The 3-grams list (```language.3```) for each language contains the absolute frequency of unigrams, bigrams and trigrams for a massive language corpus (University of Leipzig). 

**"Internal Flow" Methodology -**
The trigrams frequency lists also contain word-boundary trigrams, such as "n d". For our purpose to test isolated word comfort these are not relevant. Therefore all mid-space trigrams were excluded out of the n-gram list.

**Aggregating Boundary Patterns -**
Similarly, n-grams with a leading or trailing space are not relevant for our word based testing (e.g., Danish " og" and "og "). Our script merges these into a single unit (og), summing their frequencies to find the true cumulative weight of that finger motion.

> Core-Internal Focus: We only validate against n-grams that occur inside or at the boundaries of words, as these define the "word shape" comfort that KeyDuel measures.

#### 3. What was calculated
The script iterated through the top **500 n-grams** (the building blocks of the language) and measured three key metrics:

* **Found Count:** The raw number of top-tier n-grams present within the 100-word list.
* **Word Coverage %:** The percentage of words in the 100-word list that contain at least one of these high-frequency n-grams.
* **Frequency Weight %:** The "statistical power" of the n-grams found. This sums the absolute frequencies of the n-grams and compares them to the total frequency of the entire language file.

#### 4. Key Findings (German Example)

The results demonstrate the "concentrated power" of the 100-word list:

| N-gram Subset | Found Count | N-gram Match % | Word Coverage % | Frequency Weight % |
| :--- | :---: | :---: | :---: | :---: |
| **Top 100** | 82 | 82.0% | 91.0% | 39.3% |
| **Top 200** | 142 | 71.0% | 96.0% | 51.7% |
| **Top 500** | 239 | 47.8% | 99.0% | 69.0% |

#### 5. Interpretation
* **High Efficiency:** Even though the list only contains 100 words, it captures **82% of the top 100 most frequent letter patterns** in the German language.
* **Massive Statistical Weight:** By typing just these 100 words, you are exercising patterns that account for over **69% of all typed occurrences** in the language (based on the Top 500 n-grams).
* **Diagnostic Depth:** The "Word Coverage" reaching **99%** at $n=500$ proves that almost every single word in the KeyDuel list is exercising a high-frequency pattern, leaving almost no "dead weight" words in the test.

> **Conclusion:** The validation confirms that the KeyDuel word list is an extremely high-density proxy for the language. By typing these 100 words, you are effectively "stress-testing" the ergonomic core of the layout. The results confirm that even a small, manageable word list can provide a statistically representative impression of a layout's comfort in daily use.


## 12. Future developments: Psychophysical data base

The current implementation with a spreadsheet is sufficient for a single user. To draw general conclusions it would be needed to collect data from a larger population. With that valuable user data, representing the overall "comfort factor" of different keyboard layouts could be fitted to metrics of an analyzer, which could bring us closer to the holy grail of describing a layout's comfort in a single number.

I encourage anyone interested to pick up from here, for example by building a test website. 

For any test session the following should be recorded at minimum:

- Both layout names and versions
- Language tested
- Date and anonymised tester identifier
- Per-word ratings in row order (word order could be randomized in the first 25 words group and the second 75 word group)
- Total weighted score, total weight, max possible score, normalized score
- Session type: quick check (rows 1–25) or full evaluation (rows 1–100)
- Adaptation state: first session, or repeated trial session

This information is sufficient to aggregate results across testers, compute confidence intervals over the normalized score, and assess whether learning effects are visible across sessions.

For even better understanding the following information would be worthwhile to collect:

- Typing experience level, roughly how long the tester has been touch typing, and how long they have used each layout being tested.
- Hand size (glove size as approximation or male/ female small, middle, large)
- Finger length
- Keyboard type (row-stagger ANSI/ISO) or columnar stagger
- Keyboard split
- Keycaps
- Key spacing if not standard
- Keyboard position relative to the tester (distance, height)


## Star History

Please star this project if it helped you! Your feedback shows me how many people benefit from these resources, which motivates me making keyboard layout optimization accessible to everyone. :-)

<a href="https://www.star-history.com/?repos=rpnfan%2FAnymak%2Crpnfan%2FKeyDuel&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=rpnfan/Anymak%2Crpnfan/KeyDuel&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=rpnfan/Anymak%2Crpnfan/KeyDuel&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=rpnfan/Anymak%2Crpnfan/KeyDuel&type=date&legend=top-left" />
 </picture>
</a>


