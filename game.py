from game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guessNumber) -> GameResult:
        self.assert_illegal_value(guessNumber)
        if guessNumber == self.question:
            return GameResult(True, 3, 0)
        else:
            strikes = 0
            balls = 0
            for i in range(len(self.question)):
                char = guessNumber[i]
                if self.question.find(char) == i:
                    strikes += 1
                elif self.question.find(char) > -1:
                    balls += 1
            return GameResult(False, strikes, balls)

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if self.is_duplicated_number(guessNumber):
            raise TypeError()

    def is_duplicated_number(self, guessNumber):
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]
