% ==========================================
% Tic-Tac-Toe Minimax (Starter)
% Board: list of 9 cells, each x/o/e
% Max player: x
% Min player: o
% ==========================================

:- dynamic(expanded/1).

% ---------- instrumentation ----------
clear_count :- retractall(expanded(_)), assertz(expanded(0)).
inc_count   :- retract(expanded(N)), N1 is N+1, assertz(expanded(N1)).
get_count(N):- expanded(N).

% ---------- helpers ----------
other(x,o).
other(o,x).

% pretty print (optional)
print_board([A,B,C,D,E,F,G,H,I]) :-
    format("~w ~w ~w~n~w ~w ~w~n~w ~w ~w~n", [A,B,C,D,E,F,G,H,I]).

% ---------- winning lines ----------
line(1,2,3). line(4,5,6). line(7,8,9).
line(1,4,7). line(2,5,8). line(3,6,9).
line(1,5,9). line(3,5,7).

% win(+Board, +Player)
win(Board, P) :-
    line(I,J,K),
    nth1(I,Board,P),
    nth1(J,Board,P),
    nth1(K,Board,P).

% full(+Board)
full(Board) :- \+ member(e, Board).


% move(Board, Player, NextBoard) holds if NextBoard results from placing Player in an empty cell.
% predicate: A NextBoard is valid if we can find an 'e' in the Board 
% and replace it with the Player's symbol ('x' or 'o').
move(Board, Player, NextBoard) :-
    append(Before, [e|After], Board),     % Find a spot where 'e' exists
    append(Before, [Player|After], NextBoard). % Create NextBoard with Player there


% terminal(+Board) is true if there is a winner or no moves left.
terminal(Board) :- win(Board, x). % X won 
terminal(Board) :- win(Board, o). % O won 
terminal(Board) :- \+ member(e, Board). % No 'e' left (Board is full) 

utility(Board, U) :-
    % U=1 if x wins, -1 if o wins, 0 if draw
    ( win(Board, x) -> U = 1 % x wins
    ; win(Board, o) -> U = -1 % o wins
    ; full(Board) -> U = 0 % draw
    ).

% ---------- minimax ----------
% minimax_value(+Board, +Player, -Value)
minimax_value(Board, Player, Value) :-
    inc_count, % Count Node
    ( terminal(Board) ->
        utility(Board, Value)
    ; Player == x ->
        % Max node: take maximum over children
        findall(V,
                ( move(Board, Player, B2),
                  other(Player, P2),
                  minimax_value(B2, P2, V)
                ),
                Vs),
        max_list(Vs, Value)
    ; % Min node: take minimum over children
        findall(V,
                ( move(Board, Player, B2),
                  other(Player, P2),
                  minimax_value(B2, P2, V)
                ),
                Vs),
        min_list(Vs, Value)
    ).

% ---------- best_move/4 ----------
% choose successor with best minimax value for Player
best_move(Board, Player, BestBoard, BestValue) :-
    findall((V, B), 
            ( move(Board, Player, B),
              other(Player, P2),
              minimax_value(B, P2, V)
            ),
            Moves),
    ( Player == x -> 
        % Max player: find Move with max V
        max_member((BestValue, BestBoard), Moves)
    ; % Min player: find Move with min V
        min_member((BestValue, BestBoard), Moves)
    ).

% Example queries (use in REPL):
% clear_count, minimax_value([e,e,e,e,e,e,e,e,e], x, V), get_count(N).
% clear_count, minimax_value([x,e,e,e,o,e,e,e,x], x, V), get_count(N).
% clear_count, minimax_value([x,o,x,o,x,o,o,x,e], o, V), get_count(N).
