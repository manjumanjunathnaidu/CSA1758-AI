% Base case: the sum of integers from 1 to 1 is 1.
sum_to_n(1, 1).

% Recursive case: sum_to_n(N, Sum) is true if Sum is the sum of integers from 1 to N.
sum_to_n(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_to_n(N1, Sum1),
    Sum is Sum1 + N.