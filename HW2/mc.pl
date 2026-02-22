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

