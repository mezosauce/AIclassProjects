:- consult('mc.pl').

%% tests.pl
:- begin_tests(missionaries_cannibals).

% Test Case: Safety constraint should succeed for initial state
test(safe_initial, [nondet]) :-
    safe([3, 3, left]).

% Test Case: Safety constraint should fail for 1M, 2C on left bank
test(unsafe_state, [fail]) :-
    safe([1, 2, left]).

% Test Case: Move generation from the start state
test(move_gen, [nondet]) :-
    move([3, 3, left], _S2, _A).

% Test Case: BFS finds a valid path
test(bfs_finds_path, [nondet]) :-
    solve_bfs(Path),
    Path \= [].

% Test Case: BFS path starts at the initial state and ends at the goal
test(bfs_start_goal, [nondet]) :-
    solve_bfs(Path),
    start(Start),
    goal(Goal),
    Path = [Start|_],
    last(Path, Goal).

% Test Case: DFS finds a valid path
test(dfs_finds_path, [nondet]) :-
    solve_dfs(Path),
    Path \= [].

% Test Case: DFS path starts at the initial state and ends at the goal
test(dfs_start_goal, [nondet]) :-
    solve_dfs(Path),
    start(Start),
    goal(Goal),
    Path = [Start|_],
    last(Path, Goal).

% Test Case: Path validity for DFS (every consecutive pair is a valid move)
test(valid_path_dfs, [nondet]) :-
    solve_dfs(Path),
    valid_path(Path).

% Test Case: Path validity for BFS (every consecutive pair is a valid move)
test(valid_path_bfs, [nondet]) :-
    solve_bfs(Path),
    valid_path(Path).

% Test Case: Compare length (BFS path length must be =< DFS path length)
test(bfs_shorter_or_equal, [nondet]) :-
    solve_bfs(PathBFS),
    solve_dfs(PathDFS),
    length(PathBFS, LBFS),
    length(PathDFS, LDFS),
    format('~nBFS Path Length: ~w states', [LBFS]),
    format('~nDFS Path Length: ~w states', [LDFS]),
    LBFS =< LDFS.

% Test Case: Demonstrate run(bfs) output format
test(demo_bfs, [nondet]) :-
    format('~n--- Demonstrating BFS Output ---'),
    run(bfs).

% Test Case: Demonstrate run(dfs) output format
test(demo_dfs, [nondet]) :-
    format('~n--- Demonstrating DFS Output ---'),
    run(dfs).

% Helper: check if a list of states is a valid path
valid_path([_]).
valid_path([S1, S2 | Rest]) :-
    move(S1, S2, _),
    valid_path([S2 | Rest]).

:- end_tests(missionaries_cannibals).
