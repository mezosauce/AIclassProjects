/**
 * Assignment #2: Missionaries and Cannibals Problem
 * 
 * All members contributed to the assignment equally.
 * 
 * State Format: [ML, CL, Side]
 *   ML: Missionaries on Left bank (0-3)
 *   CL: Cannibals on Left bank (0-3)
 *   Side: Location of boat (left or right)
 * 
 * Algorithms implemented:
 *   - Depth-First Search (DFS) with cycle checking: solve_dfs/1
 *   - Breadth-First Search (BFS) for shortest solution: solve_bfs/1
 *
 * How to run:
 *   1. Start SWI-Prolog: swipl -s mc.pl
 *   2. Run DFS solution: ?- run(dfs).
 *   3. Run BFS solution: ?- run(bfs).
 * 
 * How to run tests:
 *   1. Load tests: swipl -s tests.pl
 *   2. Run all tests: ?- run_tests.
 */

% Define States [ML, CL, side]
start([3, 3, left]).
goal([0, 0, right]).

% Define the safe/1 predicate
safe([ML, CL, _]) :-
    % Rule 1: ML must be between (including) 0 and 3
    ML >= 0, ML =< 3,
    % Rule 2: CL must be between (including) 0 and 3
    CL >= 0, CL =< 3,
    % Rule 3: Number of missionaries must be greater than or equal to number of cannibals, or 0
    (ML =:=0 ; ML >= CL),
    % Rule 4: Same as Rule 3, but calculate for opposite bank as well
  % NOTE: Technically 3-ML=:=0 is more readable, but I shortened it to ML=:=3 here
    ( ML =:= 3 ; 3 - ML >= 3 - CL ).

% Possible boat combinations, passenger(missionaries, cannibals):
passenger(2, 0).
passenger(0, 2).
passenger(1, 0).
passenger(0, 1).
passenger(1, 1).

% Move from left to right
move([ML, CL, left], [ML2, CL2, right], boat(M, C)) :-
    % The boat combination must be possible
    passenger(M, C),
    % Subtract departing passengers from left bank
    ML2 is ML-M,
    CL2 is CL-C,
    % Resulting state must be safe
    safe([ML2, CL2, right]).

% Move from left to right
move([ML, CL, right], [ML2, CL2, left], boat(M, C)) :-
    % The boat combination must be possible
    passenger(M, C),
    % Add returning passengers to the left bank
    ML2 is ML+M,
    CL2 is CL+C,
    % Resulting state must be safe
    safe([ML2, CL2, left]).



%% solve_bfs(Path) - finds shortest path from start to goal using BFS
%% Path is a list of states from initial to goal state.

solve_bfs(Path) :-
    start(Start),
    bfs([[Start]], [], Path).

% bfs(+Queue, +Visited, -Path)
% Queue: list of paths (each path is a list of states, most recent first)

% Visited: list of already-visited states

bfs([[Current|Rest]|_], _, Path) :-
    goal(Current),
    reverse([Current|Rest], Path).

% Recursive case: expand the current path and continue BFS
bfs([[Current|Rest]|Queue], Visited, Path) :-
    \+ goal(Current),

    findall(
        [Next, Current|Rest],
        (move(Current, Next, _), \+ member(Next, Visited), \+ member([Next|_], Queue)),
        NewPaths
    ),
    % Append paths end of queue (FIFO)
    append(Queue, NewPaths, NewQueue),
    
    % Visted 
    bfs(NewQueue, [Current|Visited], Path).




%% solve_dfs(Path) - finds a path from start to goal using DFS with cycle checking

solve_dfs(Path) :-
    start(Start),
    dfs(Start, [Start], Path).

% dfs(+Current, +Visited, -Path)
% Current: the current state being explored
% Visited: list of states already visited (to prevent cycles)

% Base case: current state is the goal, reverse visited path to get correct order

dfs(Current, Visited, Path) :-
    goal(Current),
    reverse(Visited, Path).

% Recursive case: move to a next state not yet visited

dfs(Current, Visited, Path) :-
    \+ goal(Current),
    move(Current, Next, _),
    \+ member(Next, Visited),
    dfs(Next, [Next|Visited], Path).

%% run(Algorithm) - finds and displays a solution path
% Algorithm can be 'dfs' or 'bfs'

run(dfs) :-
    solve_dfs(Path),
    print_solution(Path, dfs).
run(bfs) :-
    solve_bfs(Path),
    print_solution(Path, bfs).

% print_solution(+Path, +Algorithm) - prints path and its metadata
print_solution(Path, Alg) :-
    format('~nResults for ~w search:~n', [Alg]),
    print_path(Path),
    length(Path, L),
    Crossings is L - 1,
    format('~nNumber of crossings: ~w~n', [Crossings]).

% print_path(+Path) - prints each state and the action leading to the next
print_path([]).
print_path([State]) :-
    format('~w~n', [State]).
print_path([S1, S2 | Rest]) :-
    format('~w~n', [S1]),
    move(S1, S2, Action),
    format('  --> ~w -->~n', [Action]),
    print_path([S2 | Rest]).

