# https://www.hackerrank.com/challenges/balanced-brackets/problem


def isBalanced(s):
    opens = ['(','[','{']
    closes = [')',']','}']
    stack = []
    
    if len(s) == 0:
        return 'YES'

    for bracket in s:
        if bracket in opens:
            stack.append(bracket)
        elif bracket in closes:
            if len(stack) == 0:
                return 'NO'
            if stack[-1] in closes:
                stack.append(bracket)
            else:
            # The last bracket was an open, does it match? 
            # yes? pop it off stack, no? quit with a NO
                if bracket == closes[0] and stack[-1] == opens[0]:
                    stack.pop()
                elif bracket == closes[1] and stack[-1] == opens[1]:
                    stack.pop()
                elif bracket == closes[2] and stack[-1] == opens[2]:
                    stack.pop()
                else:
                    return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


print('expecting YES..', isBalanced('((()))[]{[(()({[()({[]}{})]}))]}{[]}{{({}{})[{}{}]{()([()])[{()}()[[]{}()]{}{}[]()]}[[]{[]}([])]}}') )
print('expecting NO...',isBalanced('){[]()})}}]{}[}}})}{]{](]](()][{))])(}]}))(}[}{{)}{[[}[]'))
print('expecting NO...',isBalanced('}][[{[((}{[]){}}[[[)({[)}]]}(]]{[)[]}{}(){}}][{()]))})]][(((}}'))
print('expecting YES..',isBalanced('(){[{({})}]}'))
print('expecting NO...',isBalanced('{{}('))
print('expecting YES..',isBalanced('{[{((({}{({({()})()})[]({()[[][][]]}){}}))){}}]}{}{({((){{}[][]{}[][]{}}[{}])(())}[][])}'))


