consult('main.pl').

constult('bfs.pl').

consult('dfs.pl').

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

% Test Case: BFS finds a path
test(bfs_finds_path) :-
    user:solve_bfs(Path),
    Path \= [].

% Test Case: BFS path starts at start and ends at goal
test(bfs_start_goal) :-
    user:solve_bfs(Path),
    user:start(Start),
    user:goal(Goal),
    Path = [Start|_],
    last(Path, Goal).


% Test Case: DFS finds a path
test(dfs_finds_path) :-
    user:solve_dfs(Path),
    Path \= [].

% Test Case: DFS path starts at start and ends at goal
test(dfs_start_goal) :-
    user:solve_dfs(Path),
    user:start(Start),
    user:goal(Goal),
    Path = [Start|_],
    last(Path, Goal).

:- end_tests(missionaries_cannibals).
