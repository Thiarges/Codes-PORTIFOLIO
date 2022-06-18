from enum import Enum


class TokenType(Enum):
    NOT = 0
    AND = 1
    OR = 2
    IMPLICATION = 3
    EQUIVALENCE = 4
    LPAREN = 5
    RPAREN = 6
    VARIABLE = 7
    EOF = 8


class Token:
    def __init__(self, type, lexeme, literal):
        self.type = type;
        self.lexeme = lexeme;
        self.literal = literal;

    def __repr__(self) -> str:
        return f'TYPE: {self.type} LEXEME: {self.lexeme} LITERAL {self.literal}';


class Lexer:
    availableTokens = ['~', '&', '|', '>', '=', '(', ')'];
    tokens = list();
    start = 0;
    current = 0;

    def __init__(self, source):
        self.source = source.replace(" ", "");

    def isAtEnd(self):
        return self.current == len(self.source);

    def scanTokens(self):
        while (not self.isAtEnd()):
            self.start = self.current;
            self.scanToken();

        self.tokens.append(Token(TokenType.EOF, "", None));

        return self.tokens

    def advance(self):
        self.current += 1;
        return self.source[self.current - 1];

    def scanToken(self):
        c = self.advance();

        if (c.isalpha()):
            self.addToken(TokenType.VARIABLE, self.source[self.start]);
        elif (c in self.availableTokens):
            self.addToken(TokenType(self.availableTokens.index(c)));
        else:
            raise Exception(f"Illegal character {c}");

    def addToken(self, type, literal=None):
        lexeme = self.source[self.start:self.current];
        self.tokens.append(Token(type, lexeme, literal));


from abc import abstractmethod


class Visitor():
    @abstractmethod
    def visitLiteralExpression(self, element):
        pass;

    @abstractmethod
    def visitBinaryExpression(self, element):
        pass;

    @abstractmethod
    def visitUnaryExpression(self, element):
        pass;

    @abstractmethod
    def visitGroupingExpression(self, element):
        pass;


class Literal():
    def __init__(self, value):
        self.value = value;

    def accept(self, visitor):
        return visitor.visitLiteralExpression(self);


class Binary():
    def __init__(self, left, operator, right):
        self.left = left;
        self.operator = operator;
        self.right = right;

    def accept(self, visitor):
        return visitor.visitBinaryExpression(self);


class Unary():
    def __init__(self, operator, right):
        self.operator = operator;
        self.right = right;

    def accept(self, visitor):
        return visitor.visitUnaryExpression(self);


class Grouping():
    def __init__(self, expression):
        self.expression = expression;

    def accept(self, visitor):
        return visitor.visitGroupingExpression(self);


# Grammar Rules:
# expression = equivalence;
# equivalence = implication ("=" implication)*;
# implication = or (">" or)*;
# or = and ("|" and)*;
# and = not ("&" not)*;
# not = (~) not | primary
# primary = VARIABLE | "(" expression ")";

class Parser:
    current = 0;

    def __init__(self, tokens):
        self.tokens = tokens;

    def parse(self):
        return self.expression();

    def expression(self):
        return self.equivalenceNode();

    def equivalenceNode(self):
        expression = self.implicationNode();

        while (self.match(TokenType.EQUIVALENCE)):
            operator = self.previous();
            right = self.implicationNode();
            expression = Binary(expression, operator, right);

        return expression;

    def implicationNode(self):
        expression = self.orNode();

        while (self.match(TokenType.IMPLICATION)):
            operator = self.previous();
            right = self.orNode();
            expression = Binary(expression, operator, right);

        return expression;

    def orNode(self):
        expression = self.andNode();

        while (self.match(TokenType.OR)):
            operator = self.previous();
            right = self.andNode();
            expression = Binary(expression, operator, right);

        return expression;

    def andNode(self):
        expression = self.notNode();

        while (self.match(TokenType.AND)):
            operator = self.previous();
            right = self.notNode();
            expression = Binary(expression, operator, right);

        return expression;

    def notNode(self):
        if (self.match(TokenType.NOT)):
            operator = self.previous();
            right = self.notNode();
            return Unary(operator, right);

        return self.primaryNode();

    def primaryNode(self):
        if (self.match(TokenType.VARIABLE)):
            return Literal(self.previous().literal);

        if (self.match(TokenType.LPAREN)):
            expression = self.expression();

            if (self.check(TokenType.RPAREN)):
                self.advance()
                return Grouping(expression);
            raise Exception(f"Expected )");

        raise Exception(f"Expected expression");

    def match(self, type):
        if (self.check(type)):
            self.advance();
            return True;
        return False;

    def check(self, type):
        if (self.isAtEnd()): return False;
        return self.peek().type == type;

    def advance(self):
        self.current += 1;

    def isAtEnd(self):
        return self.peek().type == TokenType.EOF;

    def peek(self):
        return self.tokens[self.current];

    def previous(self):
        return self.tokens[self.current - 1];


class Interpreter(Visitor):
    def interpret(self, expression):
        value = self.evaluate(expression);
        return value;

    def evaluate(self, expression):
        return expression.accept(self);

    def visitLiteralExpression(self, element):
        return element.value;

    def visitBinaryExpression(self, element):
        left = self.evaluate(element.left);
        right = self.evaluate(element.right);

        operator = element.operator.type;

        if (operator == TokenType.AND):
            return int(left and right);
        elif (operator == TokenType.OR):
            return int(left or right);
        elif (operator == TokenType.EQUIVALENCE):
            return int(left == right);
        elif (operator == TokenType.IMPLICATION):
            return int(not (left == 1 and right == 0));

    def visitUnaryExpression(self, element):
        right = self.evaluate(element.right);

        operator = element.operator.type;

        if (operator == TokenType.NOT):
            return int(not right);

    def visitGroupingExpression(self, element):
        return self.evaluate(element.expression);


class Minterm:
    def __init__(self, values, value):
        # (0, 1, 2, 3)
        self.values = values
        # -001
        self.value = value;
        self.used = False;

        self.values.sort()

    def __str__(self):
        values = ", ".join(str(value) for value in self.values);
        return f"m({values}) = {self.value}";

    def __eq__(self, minterm):
        if (type(minterm) != Minterm):
            return False;

        return self.value == minterm.value and self.values == minterm.values;

    def combine(self, minterm):
        # combine minterms if possible

        diff = 0;
        result = ""

        for char in range(len(self.value)):
            if (self.value[char] != minterm.value[char]):
                diff += 1;
                result += "-";
            else:
                result += self.value[char];

        if (diff > 1):
            return None;

        return Minterm(self.values + minterm.values, result);


class QuineMcCluskey:
    def __init__(self, variables, values):
        self.variables = variables;
        # list with str binary values of positives
        self.values = values;

    def simplify(self):
        # get the initial grouping
        group = self.initialGrouping();
        # get the prime implicants
        primeImplicants = self.getPrimeImplicants(group);
        # essentialPrimeImplicants
        essentialPrimeImplicants = self.essentialPrimeImplicants(primeImplicants);

        # form string
        return self.makeString(essentialPrimeImplicants);

    def initialGrouping(self):
        groups = [];

        # number of groups
        for count in range(len(self.variables) + 1):
            groups.append([]);

        for value in self.values:
            count = value.count("1");
            groups[count].append(Minterm([int(value, 2)], value));

        return groups

    def getPrimeImplicants(self, groups):
        unused = [];
        # make a group with one less group
        comparisons = range(len(groups) - 1);
        newGroups = [[] for c in comparisons];

        if (len(groups) == 1):
            return groups[0];

        for compare in comparisons:
            group1 = groups[compare];
            group2 = groups[compare + 1];

            for term1 in group1:
                for term2 in group2:
                    term3 = term1.combine(term2);

                    # if they could not be combine term3 is none
                    if term3 != None:
                        term1.used = True;
                        term2.used = True;

                        newGroups[compare].append(term3);
        # store unused
        for group in groups:
            for term in group:
                if (term.used == False and term not in unused):
                    unused.append(term);

        # Recursive call
        for term in self.getPrimeImplicants(newGroups):
            if (term.used == False and term not in unused):
                unused.append(term);

        return unused

    def essentialPrimeImplicants(self, primeImplicants):
        # keep track of values with only one implicant
        essentialPrimeImplicants = [];
        valuesCovered = [False] * len(self.values);

        # essential primes
        for i in range(len(self.values)):
            value = self.values[i];
            value = int(value, 2)

            uses = 0;
            last = None;

            # go column by column and check the value against all primeImplicants
            for minterm in primeImplicants:
                if value in minterm.values:
                    uses += 1;
                    last = minterm;
            # make sure we only add the essentialPrime once
            if uses == 1 and last not in essentialPrimeImplicants:
                for v in last.values:
                    v = format(v, f'#0{len(self.variables) + 2}b')[2:];
                    valuesCovered[self.values.index(v)] = True;
                essentialPrimeImplicants.append(last)

        # take out the essentialPrimeImplicants in primeImplicants
        # only leave the numbers we have no coverage for
        primeImplicants = [primeImplicants for primeImplicants in primeImplicants if
                           primeImplicants not in essentialPrimeImplicants];

        # create a power set from the remaining prime implicants and check which combination gets the simplest form
        # passing numbers we have no coverage
        # only execute if there are values not covered
        if valuesCovered.count(False) >= 1:
            notCovered = self.petricksMethod(
                [self.values[index] for index in range(len(self.values)) if not valuesCovered[index]], primeImplicants);
            essentialPrimeImplicants += notCovered

        return essentialPrimeImplicants

    # creates power set to cover the rest of the expression
    def petricksMethod(self, values, primeImplicants):
        # values = values not covered transform into an int
        for v in range(len(values)):
            values[v] = int(values[v], 2)

        powerSet = [];

        # number of sets we can have
        for i in range(1, 2 ** len(primeImplicants)):
            currentSet = [];

            binValue = bin(i)[2:].rjust(len(primeImplicants), "0")

            # take binValue which is all possible combinations we have and make subsets
            for index in range(len(binValue)):
                if binValue[index] == "1":
                    currentSet.append(primeImplicants[index]);
            powerSet.append(currentSet);

        # go in each subset and check if it covers all the not covered values
        minSet = powerSet
        for subset in powerSet:
            # all the values that set covers
            tempValue = [];

            for implicant in subset:
                # primeimplicant values
                for value in implicant.values:
                    # values = values not covered
                    if value not in tempValue and value in values:
                        tempValue.append(value);
            tempValue.sort()

            # check if this subset covers the not covered values and if it is the smallest one
            if tempValue == values:
                if (len(subset) < len(minSet)):
                    minSet = subset;
        return minSet;

    def makeString(self, primeImplicants):
        result = "";
        for j in range(len(primeImplicants)):
            implicant = primeImplicants[j];

            for i in range(len(implicant.value)):
                if implicant.value[i] == "0":
                    result += "~";
                if implicant.value[i] != "-":
                    result += self.variables[i];
                if implicant.value.count("-", i + 1) < len(implicant.value) - i - 1 and implicant.value[i] != "-":
                    result += " & "

            if j < len(primeImplicants) - 1:
                result += " | "

        return result;


def instructions():
    print('''instructions:
~ not
& and
| or
> implication
= equivalence
            ''')


def main():
    instructions();

    text = input("expression > ");

    lexer = Lexer(text);
    tokensList = lexer.scanTokens();

    parser = Parser(tokensList);
    ast = parser.parse();

    interpreter = Interpreter();

    variables = list();
    minterm = list();

    table = "";

    for t in tokensList:
        if (t.type == TokenType.VARIABLE and t.lexeme not in variables):
            variables.append(t.lexeme);

    ##table string
    string = "|"

    for i in range(len(variables)):
        string += "  " + variables[i] + "  |";
    string += "  " + "=" + "  |";
    table += string;

    for i in range(0, 1 << len(variables)):
        inputNum = format(i, f'#0{len(variables) + 2}b')[2:];

        for t in tokensList:
            if (t.type == TokenType.VARIABLE):
                index = variables.index(t.lexeme);
                t.literal = int(inputNum[index]);

        parser = Parser(tokensList);
        ast = parser.parse();

        value = interpreter.interpret(ast)

        if (value == 1):
            minterm.append(inputNum);

        # table string
        string = "|";
        for j in range(len(inputNum)):
            string += "  " + inputNum[j] + "  |";
        string += "  " + str(value) + "  |";
        table += "\n" + string;

    print(table);

    # Quine-McCluskey
    if (len(minterm) == 1 << len(variables)):
        # it just generates one big essential prime
        print("TAUTOLOGY: all values evaluate to 1")
    elif (not len(minterm)):
        # it doesn't generate anything
        print("CONTRADICTION: all values evaluate to 0")
    else:
        qm = QuineMcCluskey(variables, minterm);
        simplification = qm.simplify();
        print("SIMPLIFIED VERSION: ")
        print(simplification);


if __name__ == "__main__":
    main()
