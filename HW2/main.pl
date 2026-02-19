% Define States [ML, CL, side]
start([3,3,left]).
goal([0,0,right]).

% Define the safe/1 predicate
safe([ML,CL,_]) :- 
% Rule 1: ML must be between (including) 0 and 3
  ML >= 0, ML =< 3,
% Rule 2: CL must be between (including) 0 and 3
  CL >= 0, CL =< 3,
% Rule 3: Number of missionaries must be greater than or equal to number of cannibals, or 0
  (ML =:=0 ; ML >= CL),
% Rule 4: Same as Rule 3, but calculate for opposite bank as well
% NOTE: Technically 3-ML=:=0 is more readable, but I shortened it to ML=:=3 here
 ( ML =:= 3 ; 3 - ML >= 3 - CL).

% Possible boat combinations, passenger(missionaries, cannibals):
passenger(2,0).
passenger(0,2).
passenger(1,0).
passenger(0,1).
passenger(1,1).

% Move from left to right
move([ML,CL,left], [ML2,CL2,right], boat(M,C)) :-
  % The boat combination must be possible
  passenger(M,C),
  % Subtract departing passengers from left bank
  ML2 is ML-M,
  CL2 is CL-C,
  % Resulting state must be safe
  safe([ML2,CL2,right]).

% Move from left to right
move([ML,CL,right], [ML2,CL2,left], boat(M,C)) :-
  % The boat combination must be possible
  passenger(M,C),
  % Add returning passengers to the left bank
  ML2 is ML+M,
  CL2 is CL+C,
  % Resulting state must be safe
  safe([ML2,CL2,left]).
