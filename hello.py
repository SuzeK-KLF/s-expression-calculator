import sys

class SExpression:
    # prepare a container to store computed values
    precalculate = {}

    def calculate(self, expression):
        while ')' in expression:

            if expression in self.precalculate:
                return self.precalculate[expression]

            right_bound = expression.index(')')
            # find the last occurrence '(' in first function ')'
            left_bound = expression[:right_bound].rindex('(')

            value = self.calculateAtom(expression[left_bound + 1:right_bound])

            if left_bound == 0:
                return value

            else:
                expression = expression[:left_bound] + str(value) + expression[right_bound+1:]

        return int(expression)

    def calculateAtom(self, expression):
        if expression in self.precalculate:
            return self.precalculate[expression]

        pieces = expression.split()

        if pieces[0] == 'add':
            answer = int(pieces[1]) + int(pieces[2])

        elif pieces[0] == 'multiply':
            answer = int(pieces[1]) * int(pieces[2])

        else:
            answer = int(expression)

        # Add to pre calculated dict
        self.precalculate[expression] = answer
        return answer


def main():
    if len(sys.argv) <=2:
        print("Please give enough info")
    else:
        print(SExpression().calculate(sys.argv[1]))


if ( __name__ == "__main__"):
    main()