#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.roles = 'Human Player'


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            result = moves.index(self.my_moves) + 1
            if result != len(moves):
                return moves[result]
            else:
                result = 0

    def move(self):
        while True:
            move = input("WHAT IS YOUR MOVE:
                         "[ROCK | PAPER | SCISSORS]\n").lower()
            if move in moves:
                return move
            else:
                print('Incorrect! Try again!')


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def not_beat(one, two):
    return ((one == 'scissors' and two == 'rock') or
            (one == 'paper' and two == 'scissors') or
            (one == 'rock' and two == 'paper'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True and not_beat(move1, move2) is False:
            self.p1.score += 1
            print("+++ Winner! +++\n")
        elif not_beat(move1, move2) is True and beats(move1, move2) is False:
            self.p2.score += 1
            print("+++ Winner +++\n")
        else:
            print("+++ STALEMATE +++\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print("Human: {} | Computer:"
              "{}\n" .format(self.p1.score, self.p2.score))

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    roles = {"human": HumanPlayer(),
             "random": RandomPlayer(),
             "cycle": CyclePlayer(),
             "reflect": ReflectPlayer()
             }

    while True:
        participant = input("What is your name ?\n")
        print("WELCOME {}!\n Below are the rules of"
              "the game, best of luck" .format(participant))
        print("Rules are: Scissors cuts paper."
              "Paper covers rock. Rock crushes scissors.\n")
        choice = input("CHOOSE AN OPPONENT:"
                       "[RANDOM | HUMAN | CYCLE | REFLECT]\n").lower()
        if choice in roles:
            game = Game(roles['human'], roles[choice])
            game.play_game()
        else:
            print('Wrong player. Try again!')