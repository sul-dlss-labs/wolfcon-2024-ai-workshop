# Naïve Bayes
A decades old approach to generative machine learning, [Naïve Bayes](https://www.ibm.com/topics/naive-bayes)
is based on [Bayes Theorem](https://www.investopedia.com/terms/b/bayes-theorem.asp), 
a mathematical formula for calculating a conditional probability of an event given 
new or additional information about the event.

In the Naïve Bayes, a couple of assumptions are made to simplify calculations. They
are:
1. All predictors are conditionally independent
2. All features contribute equally to the outcome.

While in practice, these assumptions may not necessarily hold, Naïve Bayesian inference is
still a powerful technique that allows for decision making based on the incomplete information
while updating the probabilities of events as new evidence emerges or is known. It is also
formulates a process that is conceptually similar to how we many of us make decisions when
faced with changing conditions and incomplete information.
 
## Formulation

P (A|B) = P(A) * P(B|A) / P(B)

Where:
- P(A) is the probability of A occurring
- P(B) is the probability of B occurring
- P(A|B) is the probability of A given B
- P(B|A) is the probability of B given A


## Application to Libraries
A common use of Bayesian inference in technologies used in libraries include SPAM 
filtering emails. While the [literature][^CLASSIFY] for using Bayesian inference in libraries
is rather limited, improving the decision making around topics like collection development and 
financial accountability could be a useful application if this technique was embedded into the
technology we use. A nice feature of Bayesian inference is that it easily scalable and doesn't 
require the massive resources necessary for large language models or other AI computational 
approaches. 

[^CLASSIFY]: [Automated Classification to Improve the Efficiency of Weeding library Collections](https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=8375&context=etd_theses)


