# Naïve Bayes
A decades old approach to generative machine learning, [Naïve Bayes](https://www.ibm.com/topics/naive-bayes)
is based on [Bayes Theorem](https://www.investopedia.com/terms/b/bayes-theorem.asp), 
a mathematical formula for calculating a conditional probability of an event given 
new or additional information about the event.

Naïve Bayes makes simplifying assumptions: features are treated as independent (not 
influencing each other), and all features are considered equally important for prediction.


While in practice, these assumptions may not necessarily hold, Naïve Bayesian inference is
still a powerful technique that allows for decision making based on the incomplete information
while updating the probabilities of events as new evidence emerges or is known. It also
formulates a process that is conceptually similar to how many of us make decisions when
faced with changing conditions and incomplete information.
 
## Formulation

P (A|B) = P(A) * P(B|A) / P(B)

Where:

- P(A) is the probability of A occurring
- P(B) is the probability of B occurring
- P(A|B) is the probability of A given B
- P(B|A) is the probability of B given A

## Example
Imagine a library is trying to classify new books as either "popular" or "academic" based on features like 
word count, presence of illustrations, and subject matter. Naïve Bayes could be used to calculate the 
probability of a book being "popular" given these features, even if we don't have complete information 
about all new books.

Features we'll consider:

1. Word Count (WC): Low (<50,000 words) or High (≥50,000 words)
1. Illustrations (IL): Present or Absent
1. Subject Matter (SM): General or Specialized

### Step 1: Define our sample data
Let's say we have data on 100 books:

- 60 are classified as "Popular" and 40 as "Academic"
- Among Popular books: 45 have low WC, 40 have illustrations, 50 have general SM
- Among Academic books: 10 have low WC, 5 have illustrations, 35 have specialized SM

### Step 2: Calculate prior probabilities
P(Popular) = 60/100 = 0.6

P(Academic) = 40/100 = 0.4

### Step 3: Calculate conditional probabilities

#### For Popular books:
P(Low WC | Popular) = 45/60 = 0.75

P(Illustrations Present | Popular) = 40/60 = 0.67

P(General SM | Popular) = 50/60 = 0.83

#### For Academic books:
P(Low WC | Academic) = 10/40 = 0.25

P(Illustrations Present | Academic) = 5/40 = 0.125

P(Specialized SM | Academic) = 35/40 = 0.875

### Step 4: Apply Naive Bayes to a new book

Let's say we have a new book with these features:
- Low word count
- Illustrations present
- General subject matter

We'll use the formula:

P(Class|Features) = P(Class) * P(Feature1|Class) * P(Feature2|Class) * P(Feature3|Class) / P(Features)

#### Calculate for Popular:
P(Popular|Features) = 0.6 * 0.75 * 0.67 * 0.83 = 0.25

#### Calculate for Academic:
P(Academic|Features) = 0.4 * 0.25 * 0.125 * (1 - 0.875) = 0.0015625

### Step 5: Normalize the probabilities
Total = 0.25 + 0.0015625 = 0.2515625

P(Popular|Features) = 0.25 / 0.2515625 = 0.994 or 99.4%

P(Academic|Features) = 0.0015625 / 0.2515625 = 0.006 or 0.6%

### Conclusion:
Based on this Naive Bayes calculation, we would classify this new book as "Popular" with 99.4% probability.

## Application to Libraries
While Naïve Bayes has limitations due to its assumptions, it offers a powerful and efficient approach for classification tasks.
A common use of Bayesian inference in technologies used in libraries include SPAM 
filtering emails. While the [literature][^CLASSIFY] for using Bayesian inference in libraries
is rather limited, improving the decision making around topics like collection development and 
financial accountability could be a useful application if this technique was embedded into the
technology we use. A nice feature of Bayesian inference is that it easily scalable and doesn't 
require the massive resources necessary for large language models or other AI computational 
approaches. 

[^CLASSIFY]: [Automated Classification to Improve the Efficiency of Weeding library Collections](https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=8375&context=etd_theses)


