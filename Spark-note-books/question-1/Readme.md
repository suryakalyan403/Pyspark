## PROBLEM STATEMENT

UnitedHealth Group has a program called Advocate4Me, which allows members to call an advocate and receive support for their health
care needs – whether that's behavioural, clinical, well-being, health care financing, benefits, claims or pharmacy help.
Write a query to get the patients who made a call within 7 days of their previous call. If a patient called more than twice in a span of 7
days, count them as once.

## Given Table
    +-----------------+---------------+
    |Column Name      |        Type   |
    +-----------------+---------------+
    | Policy_holder_id|      Integer  |
    | call_category   |      String   |
    | call_received   |      timestamp|
    +-----------------+---------------+
    

