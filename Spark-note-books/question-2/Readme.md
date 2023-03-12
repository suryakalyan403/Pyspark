## PROBLEM STATEMENT

Sometimes, payment transactions are repeated by accident; it could be due to user error, API failure or a retry error that causes a credit card to
be charged twice.Using the transactions table, identify any payments made at the same merchant with the
same credit card for the same amount within 10 minutes of each other. Count such repeated payments

## Given Table
    +------------------- ------+---------------+
    | Column Name              |        Type   |
    +------------------ -------+---------------+
    | tranaction_id            |      Integer  |
    | merchant_id              |      String   |
    | credit_card_id           |      timestamp|
    | amount                   |      Integer  |
    | transaction_timestamp    |      String   |
    +------------------------ -+---------------+
    

