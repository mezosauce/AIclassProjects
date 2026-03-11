% move(+Board, +Player, -NextBoard)
% predicate: A NextBoard is valid if we can find an 'e' in the Board 
% and replace it with the Player's symbol ('x' or 'o').

move(Board, Player, NextBoard) :-
    append(Before, [e|After], Board),     % Find a spot where 'e' exists
    append(Before, [Player|After], NextBoard). % Create NextBoard with Player there