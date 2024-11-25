% Base case: No moves are required to transfer 0 disks.
towers_of_hanoi(0, _, _, _, []).

% Recursive case: Move N disks from Source to Target using Auxiliary.
towers_of_hanoi(N, Source, Target, Auxiliary, Moves) :-
    N > 0,
    N1 is N - 1,
    % Move N-1 disks from Source to Auxiliary using Target
    towers_of_hanoi(N1, Source, Auxiliary, Target, Moves1),
    % Move the largest disk from Source to Target
    Move = move(Source, Target),
    % Move N-1 disks from Auxiliary to Target using Source
    towers_of_hanoi(N1, Auxiliary, Target, Source, Moves2),
    % Combine the moves
    append(Moves1, [Move | Moves2], Moves).