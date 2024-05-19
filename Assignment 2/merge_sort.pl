%% Base case when the list is empty
mergeSort([], []) :- !.

%% Base case when the list has only 1 item
mergeSort([X], [X]) :- !.

%% General case
mergeSort(IN, OUT) :-
    split2ways(IN, SPLIT1, SPLIT2),  %% (1) Split the incoming list into 2 sublists
    mergeSort(SPLIT1, SORTED1),      %% (2) Recursively sort both lists
    mergeSort(SPLIT2, SORTED2),
    merge(SORTED1, SORTED2, OUT).    %% (3) Merge both lists into the output list

%% Merging two sorted lists
merge([], L, L).
merge(L, [], L).
merge([F0|R0], [F1|R1], [F0|L]) :-
    (F0 < F1),
    merge(R0, [F1|R1], L).
merge([F0|R0], [F1|R1], [F1|L]) :-
    (F0 >= F1),
    merge([F0|R0], R1, L).

%% Splitting the list into two sublists
split2ways(Original, R1, R2) :-
    insertIn1(Original, [], [], R1, R2).

%% insertIn1/5: Splits the list into two parts
insertIn1([], R1, R2, R1, R2). %% Base case
insertIn1([E|L], R1Temp, R2Temp, R1, R2) :-
    insertIn2(L, [E|R1Temp], R2Temp, R1, R2).

%% insertIn2/5: Splits the list into two parts
insertIn2([], R1, R2, R1, R2). %% Base case
insertIn2([E|L], R1Temp, R2Temp, R1, R2) :-
    insertIn1(L, R1Temp, [E|R2Temp], R1, R2).

