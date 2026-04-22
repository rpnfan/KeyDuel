# KeyDuel — Try Out Your Layout

**Test two layouts. Compare comfort. Pick your winner.**

KeyDuel is a systematic approach to compare two layouts in terms of subjective typing comfort. The basic idea is to "translate" an alternative layout you consider to learn into the key positions of the layout you are currently using for touch-typing. A list of carefully selected test words allows you to get a much more meaningful and representative impression about how a layout will feel in real-world use, than typing random sentences.

<img width="2404" height="1009" alt="image" src="https://github.com/user-attachments/assets/08b95e2e-d4e6-4d16-8276-e378f0f35fc9" />


## 1. Purpose and High-Level Approach

The goal is to **compare perceived typing comfort between two keyboard layouts** — which layout feels more natural and effortless when typing real words in a given language. This is a *subjective comparative* test, not an objective speed or accuracy measurement.

The method combines three principles drawn from existing layout evaluation practice:

- **Linguistic frequency** — words that appear most often in real text should dominate the score, because that is where a layout spends most of its effort
- **Typing-relevant word shapes** — the word set must cover both short function words, which include the most frequent words and therefore are vital to exhibit typical finger patterns (same-finger bigrams, scissors, lateral reach and redirects). But longer content words must also be included to better exhibit alternation and roll patterns.
- **Practical test ergonomics** — sessions must be short enough to complete without fatigue, yet representative enough to give a meaningful result

Two test modes are provided:

| Mode | Words | Purpose |
|---|---|---|
| **Quick check** | 25 | Plausibility check — decide whether to proceed to the full test |
| **Full evaluation** | 100  (25 + 75) | Complete comparative assessment |



## 2. Scope and Limitations

KeyDuel measures **perceived typing comfort**, the subjective feeling of typing each word, not speed or accuracy. Speed tests on typing trainers measure how well you have learned a layout, not how comfortable it is. After a few weeks on any layout you will reach acceptable speed; comfort is the more durable and more personal variable. Used honestly, KeyDuel gives you a very good idea about overall comfort differences between two layouts.

Further limitations to be aware of:

- **Adaptation is not controlled.** A layout you have used for years will feel more natural regardless of its ergonomic properties. For a meaningful comparison, it is important to try to separate the ergonomic feel of a layout from how familiar you are with it. The How-To section will give guidance how to achieve that.
- **Individual anatomy is relevant.** Hand size, finger proportions, keyboard type, keycaps, your typing posture and more all affect comfort. Results from a single tester should not be generalised. But for yourself the results are fully valid and even better than a generalized approach can achieve.
- **Language mix is not tested.** The lists are single-language. If you regularly type in multiple languages, no single list fully represents your typing. 



## 3. How to Use KeyDuel

KeyDuel uses two components: a word list you type using a layout try-out tool, and a spreadsheet where you record your ratings.

### 1. Set up the layout try-out tool

Open [keyboard-layout-try-out.pages.dev](https://keyboard-layout-try-out.pages.dev/) and configure it to translate your target layout into the key positions of your current layout. This lets you type in the new layout without having learned it. Copy and paste the words from the plain-text word list for your language (the .txt files in the word-lists/ folder of this repo).

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

The spreadsheet calculates a normalized score between −1 and +1, displayed in percentages -100 % to 100 %. A score close to zero means no meaningful difference was detected. When you evaluate more than one layout you will get a feeling how the normalized score, displayed in percent in the spreadsheet translates to larger or smaller perceived differences between the layouts.

The spreadsheet provides two distinct metrics to help you make your decision. Both scores are relevant, but have a different practical meaning:

- **Raw List Preference (Unweighted):** This tells you which layout felt better across the list of 100 words.

    ⇒ Best for: Assessing pure ergonomic variety and how the layout handles different "word shapes".
- **Frequency Weighted Score (Normalized %):** This score takes into account how often a test word occurs roughly in a real world text. This tells you if you typed a 10,000-word essay today, which layout would leave your hands feeling more relaxed.

     ⇒ Best for: Making the final "Pick your winner" decision. This score gives you an indication how often the layout differences will play out in day-to-day typing.


> **Note:** A more detailed walkthrough with screenshots is planned. The current spreadsheet already contains a worked example — a comparison of anymak:END and Graphite — which illustrates how to fill it in.

## 4. Why Word Selection Matters

A keyboard layout is essentially a map of finger-travel pathways. Whether one layout is more comfortable than another depends on how efficiently it supports common finger patterns and how it handles specific ergonomic "pain points." However, these pain points don't appear equally in all types of text.

Keyboard layout differences do not apply uniformly across words. They emerge through **specific typing patterns**, which are shaped by:

- **Finger assignment** (strong vs weak fingers)  
- **Hand alternation vs same-hand sequences**  
- **Same-finger bigrams (SFBs)**  
- **Row changes and lateral reach**  
- **Hand load distribution**  
- **Higher-order motions** (rolls, redirects, scissors, etc.)

These factors are not properties of individual keys, but of **letter sequences**.  As a result, evaluating a layout is fundamentally a coverage problem: a test is only meaningful if it exercises a representative set of these patterns.

### From factors to patterns

Each ergonomic factor manifests as a pattern that must be exercised:

- Same-finger usage → words containing common SFBs  
- Hand alternation → alternating bigram chains  
- Finger strength → letters mapped to weaker fingers appearing in realistic contexts  
- Row and reach → vertical and lateral movement within words  
- Hand balance → both left- and right-heavy sequences

A word list that does not include these patterns cannot reveal how a layout behaves under them.

### From Frequency to Coverage

A frequency list answers: “What do users type most often?”\
An ergonomic test must answer: “What movement patterns does this layout need to handle?”

These are not the same.

A word list must therefore be constructed to **cover the space of typing patterns**, not just reflect raw frequency. In almost every language, the 100 most frequent words are overwhelmingly short function words.

**The problem:** If you only type the Top 100 words, you are only testing a narrow slice of the possible finger patterns. You are essentially testing the layout in "easy mode".  A purely frequency-based list captures *what is common*, but not *what is ergonomically diverse*.

**The solution: Designing for pattern coverage** 

A well-constructed test list should be treated like a test suite, where the goal is to cover the full space of relevant typing behaviors.

This implies:

- Coverage over raw frequency — include patterns even if they are less common
- Deliberate inclusion — ensure each major pattern type is exercised
- Balanced sampling — avoid dominance of any single pattern class

In practice, this leads to a tiered structure (introduced here and defined in detail in the next section):
- Tier A (high frequency): short, common words; captures rhythm and alternation
- Tier B (mid frequency): medium-length words; introduces mixed patterns and moderate movement
- Tier C and Tier D (pattern stress): longer or structurally complex words; exposes more SFBs, redirects, and lateral reach

Each tier serves a distinct role in increasing overall pattern coverage, similar to how unit, integration, and stress tests target different failure modes in software. The result is a test set that not only reflects real-world usage, but also systematically exposes the strengths and weaknesses of a layout across the full range of typing behaviors.

## 5. The Four-Tier Word Pool

Every 100-word list is organised into four tiers. The tiers serve both a
*linguistic classification* purpose and a *scoring weight* purpose. The
primary design goal is that the words collectively cover the most important letter bigrams and trigrams of the language, as proxies for the underlying typing patterns, weighted by how often those patterns occur in real-world text.

### Tier A — Very high-frequency function words (weight 1.0)

Articles, prepositions, conjunctions, pronouns, and auxiliary verbs. Examples:
*the, and, in, to, of, with, have, is* (English); *der, und, in, ich, ist, mit*
(German); *de, en, in, het, is, zijn* (Dutch).

**Why include them:** These words constitute the statistical backbone of any
language. In typical prose they account for a disproportionately large share of
all keystrokes. Their short length means they are typed rapidly in tight
succession.

**Why weight 1.0:** Their dominance in real text means a layout's handling of
them has the greatest impact on everyday comfort.

### Tier B — Common content words and frequent short forms (weight 0.6)

High-frequency nouns, adjectives, adverbs, and short derived forms that appear
across many topics and text types: *people, time, world, life, good, right, new*
(English); *Zeit, Leben, Welt, Arbeit, Leute* (German); *mensen, tijd, wereld,
werk* (Dutch).

**Why include them:** These words carry meaning and appear across virtually any
text a person writes. At 4–8 letters they exercise a broader range of finger
movements and bigram patterns than the very short Tier A words. They reflect
realistic typing without being domain-specific.

**Why weight 0.6:** Frequent and important, but less dominant than function
words on a per-keystroke basis.

### Tier C — Morphologically complex and lower frequency words (weight 0.3)

Verb forms, inflected nouns, derived words, and other longer forms whose letter
sequences introduce finger patterns not well represented by Tier A/B vocabulary:
*tell, keep, early, needed* (English); *machen, kommen, finden,
brauchen* (German); *maken, werken, denken, gaan* (Dutch). In agglutinative
languages (Finnish, Turkish, Polish, Russian) this tier also includes inflected
noun and verb forms that carry the highly frequent grammatical suffixes of those
languages — for example Turkish case endings (*-lerde, -lara*) and present
tense forms (*-iyor*), or Finnish verb infinitives and conjugations.

**Why include them:** Longer and morphologically complex words generate letter
combinations and same-finger sequences that short words cannot expose. A layout
may handle *work* comfortably but create a collision on *working*. Including
inflected and derived forms exposes these differences. The selection is guided
by trigram frequency data: words are chosen to cover letter patterns that are
common in real text but absent from the shorter Tier A/B vocabulary.

**Why weight 0.3:** These words are less frequent than Tier A/B in isolation,
and subjective rating variance at this level is comparable to the underlying frequency differences.

### Tier D — Long structurally diagnostic words (weight 0.1)

Longer nouns and abstract terms of 7 letters or more, for example for English: *different, important,
information, government, question, example* and if appropriate their equivalents in each
language.

**Why include them:** Long words stress finger travel, lateral reach, and
same-finger avoidance in ways that shorter words cannot. A layout that
optimises the home row for common letters may do so at the cost of uncomfortable
reach sequences in longer words. A small number of long words guards against
this blind spot and adds length variety to the test. The specific words chosen
are not necessarily the most frequent in the language; they are selected to
introduce letter combinations not already covered by Tiers A–C.

**Why weight 0.1:** These words are infrequent in everyday text. They are
present for diagnostic purposes — to catch layout weaknesses that would
otherwise be invisible — but must not dominate the score.



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
| 15 | because | 0.6 | |
| 16 | working | 0.6 | |
| 17 | when | 0.6 | |
| 18 | some | 0.6 | |
| 19 | just | 0.6 | |
| 20 | life | 0.6 | |
| 21 | making | 0.6 | |
| 22 | new | 0.6 | |
| 23 | right | 0.6 | |
| 24 | can | 0.6 | |
| 25 | getting | 0.6 | ← end of quick-check subset |
| … | *rows 26–49: Tier A/B/C interleaved* | | |
| 50 | at | 1.0 | |
| 51 | more | 0.6 | |
| 52 | having | 0.6 | |
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

*Rows 1–25: fixed quick-check subset Tier A/B. Rows 26–94: Tier A/B/C words interleaved. Rows 95–100: Tier D diagnostic words.*



## 7. Tier Composition Across All 14 Languages

The number of words per tier varies by language because linguistic structures 
differ. Languages with rich morphology (Finnish, Turkish, Polish, Russian) carry 
more Tier C words because inflected forms are more numerous and their suffixes 
contribute heavily to the trigram frequency profile of those languages. Languages 
with heavy function-word usage (French, German, English) carry more Tier A words. 
The lists were validated against trigram frequency data for 12 of the 14 languages 
(Russian and Norwegian excluded due to data availability). The word lists 
cover between 73% and 91% of the top-100 most frequent internal n-grams per 
language; confirming that virtually 
every word in the list exercises a statistically significant letter pattern. Full 
results are in the Annex.


| Language | Tier A (1.0) | Tier B (0.6) | Tier C (0.3) | Tier D (0.1) |
|---|:---:|:---:|:---:|:---:|
| English | 28 | 56 | 10 | 6 |
| German | 40 | 39 | 16 | 5 |
| Dutch | 27 | 54 | 13 | 6 |
| French | 35 | 42 | 17 | 6 |
| Spanish | 28 | 50 | 16 | 6 |
| Italian | 20 | 58 | 16 | 6 |
| Portuguese | 27 | 50 | 17 | 6 |
| Polish | 14 | 63 | 17 | 6 |
| Russian | 25 | 48 | 22 | 5 |
| Norwegian | 19 | 55 | 21 | 5 |
| Swedish | 21 | 53 | 21 | 5 |
| Danish | 19 | 57 | 19 | 5 |
| Finnish | 17 | 53 | 24 | 6 |
| Turkish | 17 | 48 | 31 | 4 |

The variation is intentional and linguistically sound. A fixed tier distribution
imposed on all languages would either distort word selection or produce lists
that do not reflect actual usage patterns in those languages.


## 8. The 25-Word Quick-Check Subset

The first 25 rows of every list form the quick-check subset. They are deliberately composed to be predictive of the full test result.

**Composition:** approximately 60–70% Tier A/B words and 30–40% Tier C words. The subset must independently stress both the alternation/rhythm dimension (via short function words) and the finger-travel dimension (via longer content words and verb forms).

**Purpose:** a tester who finds no meaningful difference after 25 words can stop. A tester who finds a clear preference has an early signal to confirm with the full test. The quick-check result is a *filter*, not a standalone measurement.



## 9. Ordering of the Full 100-Word List

```
Rows  1–25    Rows 1–25: Quick-check subset (mixed Tier A/B/C)
Rows 26–94    Tier A/B/C words interleaved
Rows 95–100   Tier D diagnostic words (long words, placed at end)
```

Rows 26–94 are interleaved so that the tester experiences a consistent mix of short function words and longer content words throughout the session, rather than a block of one type followed by another. Tiers are interleaved under a mathematically computed constraint: no single tier repeats more than its optimal maximum, typically 3 consecutive words for most languages, 4 for languages where Tier B is very dominant (Italian, Polish). Within each tier, words are placed in a randomised order, ensuring variety of specific words even though the tier pattern is regular.

Tier D words are placed at the end because the long diagnostic words would create a disproportionately strong first impression if placed early.

Different test instances for the same language always present the same word sequence, which is a deliberate design choice for this instrument: the test is always run in the same fixed order, so results across testers and sessions are directly comparable without needing to record or transmit the randomised sequence.


## 10. Scoring Formula

Each word receives a rating from the tester on a five-point scale:

| Rating | Meaning |
|:---:|---|
| +2 | New layout clearly more comfortable |
| +1 | New layout slightly more comfortable |
| 0 | No perceptible difference |
| −1 | Original layout slightly more comfortable |
| −2 | Original layout clearly more comfortable |

The normalized score is:

$$\text{Normalized score} = \frac{\displaystyle\sum_{i=1}^{100} \left(\text{rating}_i \times \text{weight}_i\right)}{2 \times \displaystyle\sum_{i=1}^{100} \text{weight}_i}$$

Result range **[−1, +1]**:

- **+1.0** — new layout clearly preferred on every word
- **0.0** — no net preference
- **−1.0** — original layout clearly preferred on every word

The denominator normalises by twice the total weight because the maximum absolute rating is 2. Dividing by 2 × Σweight scales the result to [−1, +1] regardless of tier distribution.

**Why grouped weights are sufficient:** The dominant source of variance in subjective comfort ratings is the tester's own perception from trial to trial. Four tiers capture the signal that matters — function words dominate real typing, rare words do not — while keeping the method robust, transparent, and reproducible.

> The evaluation spreadsheet shows both an unweighted and a frequency-weighted score, the latter is the more meaningful for day-to-day typing.



## 11. Methodology Discussion


### Why This Approach Rather Than Alternatives

The goal of the curated word list is to provide a meaningful representation of the language. This approach was chosen instead of simpler options:

**Versus raw corpus frequency lists:** Top-100 frequency lists are dominated by very short function words, testing only one narrow slice of the ergonomic space. The tiered approach rebalances the list to be ergonomically representative.

**Versus N-gram frequency optimisation:** Selecting words to reproduce the letter bigram and trigram distribution of a corpus maximises statistical representativeness of letter sequences but does not reflect word-level or rhythm-level typing experience. The tiered approach was preferred because a human tester rates whole words as typed units, not letter sequences in isolation.

**Versus sentence-based or synthetic text tests:** Full sentences introduce syntactic parsing and reading comprehension workload, which can obscure pure motor comfort assessments. Isolated words keep cognitive load minimal and the typing signal cleaner.


### N-gram Coverage Analysis

To ensure the KeyDuel word list is a high-fidelity proxy for real-world typing, each language list was validated using a custom n-gram analysis. This process measures how many of the language's most frequent "finger motions" are exercised by the 100 test words.



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

The script analysed the top **500 n-grams** and measured four metrics for 
each threshold (n=100, 200, 300, 400, 500):

* **N-grams Found:** The number of top-N patterns that appear in at least 
  one word of the 100-word list.
* **N-grams Found %:** N-grams Found as a percentage of N (how much of the 
  top-N set is represented).
* **Words Exercised %:** The percentage of the 100 words that contain at 
  least one top-N pattern. Near 100% means almost no "dead weight" words.
* **Corpus Coverage %:** The fraction of *all* language pattern occurrences
  accounted for by the n-grams actually found in the word list. This differs from Potential Core Weight, which represents the theoretical maximum if all top-N patterns were present. The Corpus Coverage is the most meaningful metric: it answers "if someone typed real text in this language all day, what share of their finger motions would be exercised by the KeyDuel list?"

#### 4. Key Findings (German Example)

The results demonstrate the "concentrated power" of the 100-word list:

| Top N-grams | Found Count | N-grams Found % | Words Exercised % | Corpus Coverage % |Potential Core Weight | List Efficiency |
| :--- | :---: | :---: | :---: | :---: |:---: | :---: |
| **Top 100** | 91 | 91.0% | 99.0% | 38.2% | 40.9% | 93.3% |
| **Top 200** | 155 | 77.5% | 100.0% | 46.3% | 53.5% | 86.4% |
| **Top 500** | 267 | 53.4% | 100.0% | 53.5% | 71.2% | 75.1% |

#### 5. Interpretation

* **High Pattern Match:** The list captures **91% of the top 100 most frequent 
  letter patterns** in German, meaning the words were chosen to cover the 
  statistically dominant finger motions.
* **Real-World Relevance:** The Corpus Coverage of 53.5% at n=500 means that by typing these 100 words, you exercise patterns accounting for more than half of all pattern occurrences in real German text — confirming the list is a representative proxy for everyday typing.
* **Diagnostic Depth:** Words Exercised reaching **100%** at n=500 means  
  every word in the list exercises a high-frequency pattern. There is essentially 
  no dead weight in the test.
* **List Efficiency:** The ratio of Corpus Coverage to the 
  theoretical maximum (Potential Core Weight) quantifies how well the 100 words 
  were selected. A high efficiency means the words collectively cover the 
  available patterns well, not just the most obvious ones.

See the Annex A for the full analysis list of all tested languages.
> **Conclusion:** The validation confirms that the KeyDuel word list is an extremely high-density proxy for the language. By typing these 100 words, you are effectively "stress-testing" the ergonomic core of the layout. The results confirm that even a small, manageable word list can provide a statistically representative impression of a layout's comfort in daily use.

### Quick-Check Subset Validation (25, 50, 75 compared to 100 words)

A second analysis validated that the 25-word quick-check subset is a genuine 
predictor of the full 100-word result, not just an arbitrary first slice.

Using the same n-gram methodology, the script measured coverage at each 
subset size against the top N n-grams of the language. The following example shows the results for the top 500 n-grams for German.

#### German

| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 103 | 175 | 212 | 267 |
| **N-grams Found %** | 20.6% | 35.0% | 42.4% | 53.4% |
| **Words Exercised %** | 100% | 100% | 100% | 100% |
| **Corpus Coverage %** | 30.3% | 41.6% | 46.7% | 53.5% |

The results confirm 
that the 25-word subset already exercises the majority of high-frequency 
patterns — providing a meaningful early signal — while the full 100 words 
add the remaining coverage needed for a reliable final score. But even using 50 words improves the Corpus Coverage by more than 11%, while the next 25 words (75 total) just improve the Corpus Coverage by about 5%. With the full set of 100 words improving about 7%, covering already more than the half complete corpus.

This diminishing return is expected: language corpora follow a [Zipfian distribution](https://en.wikipedia.org/wiki/Zipf's_law), where the most frequent patterns are dramatically more common than the rest, so the first 25 words capture a disproportionately large share.

Full results for each language at n=100, n=500 and n=2000 are in Annex B.


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


# Annex A: Language N-gram Analysis Results


### Language: Danish
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 86 | 145 | 189 | 225 | 244 |
| **N-grams Found %** | 86.0% | 72.5% | 63.0% | 56.2% | 48.8% |
| **Words Exercised %** | 97.0% | 99.0% | 99.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 40.2% | 53.1% | 61.0% | 66.5% | 70.6% |
| **Corpus Coverage** | 37.0% | 44.6% | 48.2% | 50.2% | 51.0% |
| **List Efficiency** | 92.0% | 84.0% | 79.0% | 75.5% | 72.2% |

### Language: Dutch
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 89 | 150 | 199 | 230 | 261 |
| **N-grams Found %** | 89.0% | 75.0% | 66.3% | 57.5% | 52.2% |
| **Words Exercised %** | 89.0% | 97.0% | 100.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 39.6% | 52.1% | 60.1% | 66.0% | 70.6% |
| **Corpus Coverage** | 37.0% | 44.9% | 48.8% | 50.6% | 52.1% |
| **List Efficiency** | 93.5% | 86.2% | 81.2% | 76.7% | 73.7% |

### Language: English
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 85 | 141 | 179 | 209 | 233 |
| **N-grams Found %** | 85.0% | 70.5% | 59.7% | 52.2% | 46.6% |
| **Words Exercised %** | 98.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 39.1% | 51.0% | 59.0% | 65.1% | 70.0% |
| **Corpus Coverage** | 35.6% | 42.4% | 45.4% | 47.3% | 48.5% |
| **List Efficiency** | 91.1% | 83.1% | 77.0% | 72.6% | 69.3% |

### Language: Finnish
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 73 | 128 | 168 | 198 | 224 |
| **N-grams Found %** | 73.0% | 64.0% | 56.0% | 49.5% | 44.8% |
| **Words Exercised %** | 92.0% | 96.0% | 100.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 31.2% | 44.2% | 53.2% | 60.1% | 65.7% |
| **Corpus Coverage** | 24.8% | 32.0% | 35.7% | 37.7% | 39.2% |
| **List Efficiency** | 79.5% | 72.4% | 67.0% | 62.7% | 59.7% |

### Language: French
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 72 | 129 | 181 | 218 | 247 |
| **N-grams Found %** | 72.0% | 64.5% | 60.3% | 54.5% | 49.4% |
| **Words Exercised %** | 91.0% | 97.0% | 100.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 39.7% | 51.9% | 59.9% | 65.6% | 70.0% |
| **Corpus Coverage** | 32.0% | 39.2% | 43.4% | 45.5% | 46.8% |
| **List Efficiency** | 80.5% | 75.4% | 72.4% | 69.4% | 66.9% |

### Language: German
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 91 | 155 | 212 | 240 | 267 |
| **N-grams Found %** | 91.0% | 77.5% | 70.7% | 60.0% | 53.4% |
| **Words Exercised %** | 99.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 40.9% | 53.5% | 61.3% | 66.9% | 71.2% |
| **Corpus Coverage** | 38.2% | 46.3% | 50.7% | 52.3% | 53.5% |
| **List Efficiency** | 93.3% | 86.4% | 82.7% | 78.2% | 75.1% |

### Language: Italian
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 78 | 128 | 169 | 203 | 234 |
| **N-grams Found %** | 78.0% | 64.0% | 56.3% | 50.7% | 46.8% |
| **Words Exercised %** | 96.0% | 99.0% | 99.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 38.5% | 52.4% | 61.1% | 67.5% | 72.6% |
| **Corpus Coverage** | 32.5% | 39.6% | 43.1% | 45.3% | 46.9% |
| **List Efficiency** | 84.5% | 75.5% | 70.6% | 67.2% | 64.6% |

### Language: Polish
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 81 | 139 | 184 | 216 | 247 |
| **N-grams Found %** | 81.0% | 69.5% | 61.3% | 54.0% | 49.4% |
| **Words Exercised %** | 98.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 29.5% | 40.7% | 48.5% | 54.4% | 59.2% |
| **Corpus Coverage** | 25.2% | 31.6% | 35.2% | 37.1% | 38.6% |
| **List Efficiency** | 85.5% | 77.7% | 72.6% | 68.2% | 65.2% |

### Language: Spanish
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 81 | 138 | 182 | 211 | 234 |
| **N-grams Found %** | 81.0% | 69.0% | 60.7% | 52.8% | 46.8% |
| **Words Exercised %** | 99.0% | 99.0% | 100.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 43.3% | 55.2% | 62.9% | 68.6% | 73.1% |
| **Corpus Coverage** | 39.3% | 46.2% | 49.6% | 51.2% | 52.3% |
| **List Efficiency** | 90.7% | 83.7% | 78.8% | 74.7% | 71.5% |

### Language: Swedish
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 88 | 150 | 201 | 241 | 276 |
| **N-grams Found %** | 88.0% | 75.0% | 67.0% | 60.2% | 55.2% |
| **Words Exercised %** | 90.0% | 98.0% | 100.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 38.0% | 49.9% | 57.9% | 63.9% | 68.4% |
| **Corpus Coverage** | 35.1% | 42.7% | 46.9% | 49.2% | 50.8% |
| **List Efficiency** | 92.3% | 85.6% | 80.9% | 77.0% | 74.3% |

### Language: Turkish
| Metric | n=100 | n=200 | n=300 | n=400 | n=500 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **N-grams Found** | 73 | 141 | 183 | 216 | 241 |
| **N-grams Found %** | 73.0% | 70.5% | 61.0% | 54.0% | 48.2% |
| **Words Exercised %** | 95.0% | 99.0% | 99.0% | 100.0% | 100.0% |
| **Potential Core Weight** | 29.5% | 41.6% | 49.7% | 56.1% | 61.2% |
| **Corpus Coverage** | 23.1% | 31.3% | 34.8% | 36.8% | 38.1% |
| **List Efficiency** | 78.3% | 75.3% | 69.9% | 65.7% | 62.3% |



# Annex B: 25, 50 and 75 Word Subset Analysis

## Language 100 N-gram Analysis (Subset Comparison)


### Language: Danish
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 49 | 74 | 82 | 86 |
| **N-grams Found %** | 49.0% | 74.0% | 82.0% | 86.0% |
| **Words Exercised %** | 100.0% | 100.0% | 98.7% | 97.0% |
| **Corpus Coverage %** | 26.0% | 33.2% | 35.8% | 37.0% |

### Language: Dutch
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 50 | 71 | 79 | 89 |
| **N-grams Found %** | 50.0% | 71.0% | 79.0% | 89.0% |
| **Words Exercised %** | 92.0% | 88.0% | 85.3% | 89.0% |
| **Corpus Coverage %** | 24.0% | 30.9% | 34.1% | 37.0% |

### Language: English
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 44 | 65 | 74 | 85 |
| **N-grams Found %** | 44.0% | 65.0% | 74.0% | 85.0% |
| **Words Exercised %** | 96.0% | 96.0% | 97.3% | 98.0% |
| **Corpus Coverage %** | 23.1% | 30.1% | 32.5% | 35.6% |

### Language: Finnish
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 37 | 55 | 64 | 73 |
| **N-grams Found %** | 37.0% | 55.0% | 64.0% | 73.0% |
| **Words Exercised %** | 96.0% | 96.0% | 92.0% | 92.0% |
| **Corpus Coverage %** | 12.9% | 19.3% | 21.8% | 24.8% |

### Language: French
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 32 | 54 | 62 | 72 |
| **N-grams Found %** | 32.0% | 54.0% | 62.0% | 72.0% |
| **Words Exercised %** | 92.0% | 94.0% | 93.3% | 91.0% |
| **Corpus Coverage %** | 14.9% | 24.2% | 27.1% | 32.0% |

### Language: German
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 49 | 70 | 79 | 91 |
| **N-grams Found %** | 49.0% | 70.0% | 79.0% | 91.0% |
| **Words Exercised %** | 100.0% | 100.0% | 98.7% | 99.0% |
| **Corpus Coverage %** | 25.4% | 32.1% | 34.8% | 38.2% |

### Language: Italian
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 38 | 61 | 72 | 78 |
| **N-grams Found %** | 38.0% | 61.0% | 72.0% | 78.0% |
| **Words Exercised %** | 96.0% | 96.0% | 97.3% | 96.0% |
| **Corpus Coverage %** | 17.4% | 27.0% | 30.5% | 32.5% |

### Language: Polish
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 38 | 64 | 72 | 81 |
| **N-grams Found %** | 38.0% | 64.0% | 72.0% | 81.0% |
| **Words Exercised %** | 96.0% | 98.0% | 97.3% | 98.0% |
| **Corpus Coverage %** | 13.5% | 21.2% | 22.8% | 25.2% |

### Language: Spanish
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 43 | 60 | 70 | 81 |
| **N-grams Found %** | 43.0% | 60.0% | 70.0% | 81.0% |
| **Words Exercised %** | 96.0% | 98.0% | 98.7% | 99.0% |
| **Corpus Coverage %** | 27.6% | 32.4% | 35.4% | 39.3% |

### Language: Swedish
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 45 | 67 | 81 | 88 |
| **N-grams Found %** | 45.0% | 67.0% | 81.0% | 88.0% |
| **Words Exercised %** | 88.0% | 86.0% | 89.3% | 90.0% |
| **Corpus Coverage %** | 23.8% | 29.3% | 33.0% | 35.1% |

### Language: Turkish
| Metric (tested against Top 100 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 100)** | 35 | 56 | 65 | 73 |
| **N-grams Found %** | 35.0% | 56.0% | 65.0% | 73.0% |
| **Words Exercised %** | 92.0% | 94.0% | 93.3% | 95.0% |
| **Corpus Coverage %** | 13.5% | 19.0% | 21.0% | 23.1% |



## Language 500 N-gram Analysis (Subset Comparison)



### Language: Danish
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 76 | 148 | 197 | 244 |
| **N-grams Found %** | 15.2% | 29.6% | 39.4% | 48.8% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 28.3% | 40.0% | 46.4% | 51.0% |

### Language: Dutch
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 89 | 159 | 210 | 261 |
| **N-grams Found %** | 17.8% | 31.8% | 42.0% | 52.2% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 27.5% | 39.1% | 45.8% | 52.1% |

### Language: English
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 92 | 149 | 189 | 233 |
| **N-grams Found %** | 18.4% | 29.8% | 37.8% | 46.6% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 27.6% | 37.8% | 42.9% | 48.5% |

### Language: Finnish
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 73 | 133 | 177 | 224 |
| **N-grams Found %** | 14.6% | 26.6% | 35.4% | 44.8% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 16.7% | 27.0% | 32.7% | 39.2% |

### Language: French
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 90 | 155 | 190 | 247 |
| **N-grams Found %** | 18.0% | 31.0% | 38.0% | 49.4% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 20.3% | 33.2% | 38.2% | 46.8% |

### Language: German
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 103 | 175 | 212 | 267 |
| **N-grams Found %** | 20.6% | 35.0% | 42.4% | 53.4% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 30.3% | 41.6% | 46.7% | 53.5% |

### Language: Italian
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 66 | 136 | 185 | 234 |
| **N-grams Found %** | 13.2% | 27.2% | 37.0% | 46.8% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 20.3% | 33.7% | 41.0% | 46.9% |

### Language: Polish
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 75 | 155 | 203 | 247 |
| **N-grams Found %** | 15.0% | 31.0% | 40.6% | 49.4% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 16.7% | 29.0% | 33.5% | 38.6% |

### Language: Spanish
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 87 | 152 | 186 | 234 |
| **N-grams Found %** | 17.4% | 30.4% | 37.2% | 46.8% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 31.6% | 40.7% | 45.3% | 52.3% |

### Language: Swedish
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 80 | 170 | 226 | 276 |
| **N-grams Found %** | 16.0% | 34.0% | 45.2% | 55.2% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 26.8% | 38.2% | 45.1% | 50.8% |

### Language: Turkish
| Metric (tested against Top 500 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 500)** | 72 | 143 | 190 | 241 |
| **N-grams Found %** | 14.4% | 28.6% | 38.0% | 48.2% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 17.2% | 27.0% | 32.0% | 38.1% |




## Language 2000 N-gram Analysis (Subset Comparison)


### Language: Danish
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 89 | 177 | 249 | 330 |
| **N-grams Found %** | 4.5% | 8.8% | 12.4% | 16.5% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 28.7% | 40.6% | 47.4% | 52.7% |

### Language: Dutch
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 112 | 211 | 282 | 363 |
| **N-grams Found %** | 5.6% | 10.5% | 14.1% | 18.1% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 28.1% | 40.4% | 47.5% | 54.6% |

### Language: English
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 128 | 203 | 260 | 345 |
| **N-grams Found %** | 6.4% | 10.2% | 13.0% | 17.2% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 28.4% | 39.2% | 44.7% | 51.3% |

### Language: Finnish
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 97 | 212 | 292 | 382 |
| **N-grams Found %** | 4.9% | 10.6% | 14.6% | 19.1% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 17.4% | 29.3% | 36.0% | 43.6% |

### Language: French
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 104 | 196 | 254 | 347 |
| **N-grams Found %** | 5.2% | 9.8% | 12.7% | 17.3% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 20.6% | 34.2% | 39.8% | 49.1% |

### Language: German
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 116 | 217 | 276 | 357 |
| **N-grams Found %** | 5.8% | 10.8% | 13.8% | 17.8% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 30.6% | 42.4% | 48.0% | 55.4% |

### Language: Italian
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 86 | 205 | 284 | 373 |
| **N-grams Found %** | 4.3% | 10.2% | 14.2% | 18.6% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 20.8% | 35.2% | 43.1% | 50.1% |

### Language: Polish
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 88 | 216 | 305 | 416 |
| **N-grams Found %** | 4.4% | 10.8% | 15.2% | 20.8% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 17.0% | 30.4% | 36.0% | 42.6% |

### Language: Spanish
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 101 | 208 | 283 | 371 |
| **N-grams Found %** | 5.1% | 10.4% | 14.1% | 18.6% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 32.0% | 42.0% | 47.3% | 55.1% |

### Language: Swedish
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 93 | 219 | 296 | 379 |
| **N-grams Found %** | 4.7% | 10.9% | 14.8% | 18.9% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 27.0% | 39.2% | 46.7% | 53.0% |

### Language: Turkish
| Metric (tested against Top 2000 N-grams) | 25 Words | 50 Words | 75 Words | 100 Words |
| :--- | :---: | :---: | :---: | :---: |
| **Found N-grams (of 2000)** | 98 | 226 | 320 | 434 |
| **N-grams Found %** | 4.9% | 11.3% | 16.0% | 21.7% |
| **Words Exercised %** | 100.0% | 100.0% | 100.0% | 100.0% |
| **Corpus Coverage %** | 18.0% | 29.1% | 35.3% | 42.9% |



# Star History

Please star this project if it helped you! Your feedback shows me how many people benefit from these resources, which motivates me making keyboard layout optimization accessible to everyone. :-)

<a href="https://www.star-history.com/?repos=rpnfan%2FAnymak%2Crpnfan%2FKeyDuel&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=rpnfan/Anymak%2Crpnfan/KeyDuel&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=rpnfan/Anymak%2Crpnfan/KeyDuel&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=rpnfan/Anymak%2Crpnfan/KeyDuel&type=date&legend=top-left" />
 </picture>
</a>

