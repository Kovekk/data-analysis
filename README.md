# Overview

Data grabbed from pcibex was a self-paced reading task that asked participants which person performed the task. The Qualtrics questionaire helped measure autistic traits through BAPQ and AQ (standardized autism questionaires).

I wrote this software for my wife's thesis project. She is looking at how autistic traits and object control are related.

[Software Demo Video](https://www.youtube.com/watch?v=ZqWJAc3Wsco)

# Data Analysis Results

Question 1: Which autism questionaire score(s) should be used as a proxy for our autistic traits variable?
Answer: The BAPQ and AQ were highly correlated because of Pearson's R correlation test. Also, AQ had the most complete data and came first in the survey. Due to these outcomes the total AQ score was chosen to represent autistic traits. 

Question 2: Do autistic traits affect the likelihood of object control interpretation?
Answer: With the original data, no evidence was found that autistic traits affect the likelihood of object control interpretation. However, there were limitations in sample size and diversity that could have affected the outcome. 

# Development Environment

Rstudio

R
Packages used:
tidyverse
cowplot
buildmer
emmeans
ggdist
ggpubr
interactions
factoextra

# Useful Websites

* [w3schools for R](https://www.w3schools.com/r/)
* [buildmer reference page](https://cran.r-project.org/web/packages/buildmer/refman/buildmer.html)
* [emmeans reference page](https://cran.r-project.org/web/packages/emmeans/refman/emmeans.html)

# Future Work

* Make adjustments to the synthetic data so it could pass the preprocessing and better replicate human responses.
* If I were to start over from scratch, more python with the pandas library would have been used for data gathering and preprocessing.
