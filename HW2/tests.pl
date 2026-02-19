consult('main.pl').


%% tests.pl
:- begin_tests(missionaries_cannibals).

% Test Case: Safety constraint should succeed
test(safe_initial) :-
    user:safe([3, 3, left]).

% Test Case: Safety constraint should fail for 1M, 2C
test(unsafe_state, [fail]) :-
    user:safe([1, 2, left]).

% Test Case: Move generation
test(move_gen) :-
    user:move([3, 3, left], _S2, _A).

:- end_tests(missionaries_cannibals).
