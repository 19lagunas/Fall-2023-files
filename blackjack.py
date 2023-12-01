import random 

#Step 1:
def DealCards():
    cards = [11, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#Step 2: 
def CalcScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Step 3:
def CompareScore(playerScore, computerScore):
    if playerScore > 21 and computerScore > 21:
        return "YOU EXCEEDED 21. YOU LOSE!"
    if playerScore == computerScore:
        return "IT'S A TIE!"
    elif playerScore == 0:
        return "YOU GOT BLACKJACK! YOU WIN THE GAME!"
    elif computerScore == 0:
        return "YOU LOSE! COMPUTER HAS BLACKJACK!"
    elif playerScore > 21:
        return "YOU EXCEEDED THE LIMIT! YOU LOSE!"
    elif computerScore > 21:
        return "COMPUTER WENT OVER! YOU WIN THE GAME!"
    elif playerScore > computerScore:
        return "YOU WIN!"
    else:
        return "GAME OVER. YOU LOSE!"
    
#Step 4:
def goplay():
    playerCards = []
    computerCards = []
    gameOver = False

    for _ in range(2):
        playerCards.append(DealCards())
        computerCards.append(DealCards())
    
    while gameOver == False:
        playerScore = CalcScore(playerCards)
        computerScore = CalcScore(computerCards)
        print(f"YOUR CARDS: {playerCards} CURRENT SCORE: {playerScore}")
        print(f"COMPUTER'S 1ST CARD: {computerCards[0]}")
        
    if playerScore == 0 or computerScore == 0 or playerScore > 21:
        gameOver = True
    else:
        continueGame = input("ENTER 'c' TO GET ANOTHER CARD OR 'p' TO PASS. TO QUIT, ENTER 'q'.")
    if continueGame == 'c':
        playerCards.append(DealCards())
    if continueGame == 'q':
        print("YOU LEFT THE GAME.")
        gameOver = True
    else: 
        print("INVALID INPUT. PLEASE TRY AGAIN..")
        continueGame
    
    while computerScore != 0 and computerScore < 17:
        computerCards.append(DealCards())
        computerScore = CalcScore(computerCards)
    print(f"YOUR FINAL HAND: {playerCards}, FINAL SCORE: {playerScore}")
    
