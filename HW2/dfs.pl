:- consult('main.pl').

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