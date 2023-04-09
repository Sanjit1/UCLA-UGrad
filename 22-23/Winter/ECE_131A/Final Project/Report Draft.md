# <center>ECE 131A Final Project Report</center>
<center><b>by Sanjit Sarda</b> Winter 2023 </center>

## Table of Contents:

1. [Problem 1: Tossing a fair and unfair die](#1-25-pts-tossing-a-fair-and-unfair-die)
   * Simulating the toss of a fair die
   * Analytical probability of getting an odd number
   * Comparing theoretical and experimental results
   * Repetition of the experiment with an unfair die
2. [Problem 2: Maximum Likelihood Estimation](#2-25-pts-maximum-likelihood-estimation)
   * Analytically deriving the Maximum Likelihood Equation for a Gaussian distribution
   * Analytically deriving the expressions for $\mu$ and $\sigma^2$ and applying them to the data
   * Comparing the distribution of the data with the theoretical distribution
3. [Problem 3: Naive Bayes Classifier](#3-25-pts-naive-bayes-classifier)
   * Estimating individual class probabilities
   * Estimating conditional probabilities
   * Computing the probability of given events.
   * Predicting purchase probability.
4. [Problem 4: Central Limit Theorem](#4-25-pts-central-limit-theorem)
   * Distributions of sum of $n$ $X_i$ = $\mathcal{U}[3, 7]$'s for $n$ = 1, 2, 3, 10, 30, 100
   * Analytical Calculation of the mean and variance of the sum of n Uniform random variables
   * Generating gaussian RV with analytical mean and variance
   * Repetition of the experiment for $X_i$ = Biased die
   * (Bonus) Exact PDFs for the sum of n Uniform random variables
5. [Appendix](#appendix): Code for the problems



<!-- Js -->
We have classes jp-InputPrompt jp-InputArea-prompt
filter and get everything that is both those classes and delete

<script>
    var prompts = document.getElementsByClassName("jp-InputPrompt");
    var inputs = document.getElementsByClassName("jp-InputArea-prompt");
    var i;
    for (i = 0; i < prompts.length; i++) {
        prompts[i].style.display = "none";
    }
    for (i = 0; i < inputs.length; i++) {
        inputs[i].style.display = "none";
    }
</script>