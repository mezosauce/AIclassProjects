:- consult('main.pl').


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