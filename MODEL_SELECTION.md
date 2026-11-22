# Model selection

## The question
The model predicts whether a customer will leave the service. Incorrect predictions may cause the company to lose customers or spend resources on unnecessary retention efforts.

## Candidates

| Candidate | Why I tried it | AUC | F1 | F1 per slice (lowest) | p95 latency (ms) | Size (KB) | MLflow run ID |
|---|---|---|---|---|---|---|---|
| Logistic Regression | Simple and fast baseline | 0.798 | 0.495 | 0.250 | 3.798 | 3.548 | 9c6e42ed85214e1e93a0c32d598f3928 |
| Random Forest | Captures nonlinear relationships | 0.759 | 0.454 | 0.222 | 16.390 | 3160.1 | 64662b243fe640cb9775c3a00a010779 |
| Gradient Boosting | Sequentially improves predictions | 0.748 | 0.417 | 0.222 | 4.115 | 141.7 | 6306c7ec1bdb46bab4afd8bfb3a88d39 |

## The champion
I selected Logistic Regression because it achieved the highest F1 (0.495), highest AUC (0.798), and best weakest-slice F1 (0.250). It also had the lowest latency (3.798 ms) and smallest size (3.548 KB).

I accepted lower F1 on one-year and two-year contracts compared with some other candidates in exchange for better overall performance and efficiency.

## My promotion rules
- Latency budget (p95): 20 ms, because it provides reasonable response time and allows some execution overhead.
- Minimum gain to replace the champion (F1 points): 0.01, because a new model should demonstrate a meaningful performance improvement.

## What I would check next
I would examine the number of customers in each contract group to ensure that the slice F1 scores are reliable. I would also monitor data drift because changes in customer behavior could reduce model performance.
