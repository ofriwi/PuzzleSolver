# PuzzleSolver

Class Summary:
Piece
    Represents a single puzzle piece.
    Functions include: distance calculation

DistanceMatrix
    Receives a list of pieces and constructs a distance table

Organize
    Receives a distance matrix and a corresponding list of pieces.
    Organizes them using the Hungarian method.

Main
    1) Read picture and transform it into a matrix
    2) divide matrix to smaller matrices, construct pieces, and create a suitable
    list.
    3) Call DistanceMatrix
    4) Call Organize
    5) Turn receives matrix into a picture and save it