% Facts: Relationships in the family
parent(john, mary).      % John is the parent of Mary
parent(john, michael).   % John is the parent of Michael
parent(susan, mary).     % Susan is the parent of Mary
parent(susan, michael).  % Susan is the parent of Michael
parent(mary, sophie).    % Mary is the parent of Sophie
parent(mary, daniel).    % Mary is the parent of Daniel
parent(michael, tom).    % Michael is the parent of Tom
parent(michael, emily).  % Michael is the parent of Emily

% Gender facts
male(john).
male(michael).
male(daniel).
male(tom).
female(susan).
female(mary).
female(sophie).
female(emily).

% Rules: Define family relationships

% A child is related to a parent.
child(X, Y) :-
    parent(Y, X).

% A grandparent is a parent of a parent.
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% A sibling shares the same parent.
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% A brother is a male sibling.
brother(X, Y) :-
    sibling(X, Y),
    male(X).

% A sister is a female sibling.
sister(X, Y) :-
    sibling(X, Y),
    female(X).

% An uncle is a brother of a parent.
uncle(X, Y) :-
    parent(Z, Y),
    brother(X, Z).

% An aunt is a sister of a parent.
aunt(X, Y) :-
    parent(Z, Y),
    sister(X, Z).

% A grandchild is a child of a child.
grandchild(X, Y) :-
    grandparent(Y, X).

% A cousin shares a grandparent but not a parent.
cousin(X, Y) :-
    grandparent(Z, X),
    grandparent(Z, Y),
    \+ sibling(X, Y),
    X \= Y.