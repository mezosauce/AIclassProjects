% terminal(+Board) is true if there is a winner or no moves left.
terminal(Board) :- win(Board, x). % X won 
terminal(Board) :- win(Board, o). % O won 
terminal(Board) :- \+ member(e, Board). % No 'e' left (Board is full) 

% Helper: win(+Board, +Player)
% We define what a "win" looks like for a specific player.
% This uses pattern matching on the 9-cell list.

% Rows
win([P,P,P, _,_,_, _,_,_], P) :- P \= e.
win([_,_,_, P,P,P, _,_,_], P) :- P \= e.
win([_,_,_, _,_,_, P,P,P], P) :- P \= e.

% Columns
win([P,_,_, P,_,_, P,_,_], P) :- P \= e.
win([_,P,_, _,P,_, _,P,_], P) :- P \= e.
win([_,_,P, _,_,P, _,_,P], P) :- P \= e.

% Diagonals
win([P,_,_, _,P,_, _,_,P], P) :- P \= e.
win([_,_,P, _,P,_, P,_,_], P) :- P \= e.