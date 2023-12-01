import random 

#Step 1: Deal the cards 
def DealCards():
    cards = [11, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#Step 2: Calculate the score
def CalcScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Step 3: Compare scores to delcare a winner
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

#Set up rules for players
def displayRules():
    print("\nWELCOME TO BLACKJACK!")
    print("\nRULES:")
    print("1. TRY TO GET AS CLOSE TO 21 WITHOUT GOING OVER.")
    print("2. ACES ARE WORTH EITHER 1 OR 11. FACE CARDS ARE WORTH 10.")
    print("3. A BLACKJACK (TWO-CARD HAND TOTALING 21) BEATS THE OTHER HAND.")
    print("4. TYPE 'x' TO GET ANOTHER CARD,'y' TO PASS, OR 'q' TO QUIT THE GAME.")
    print("5. HAVE FUN!")
    print("\n...COMMENCING GAME...")
    
#Step 4: make a function to start the game:
def goplay():
    displayRules()

    playerCards = []
    computerCards = []
    gameOver = False

    for _ in range(2):
        playerCards.append(DealCards())
        computerCards.append(DealCards())
    
    while not gameOver:
        playerScore = CalcScore(playerCards)
        computerScore = CalcScore(computerCards)

        print(f"YOUR CARDS: {playerCards} CURRENT SCORE: {playerScore}")
        print(f"COMPUTER'S 1ST CARD: {computerCards[0]}")
        
        if playerScore == 0 or computerScore == 0 or playerScore > 21:
            gameOver = True
        else:
            continueGame = input("ENTER 'x' TO GET ANOTHER CARD, 'y' TO PASS, OR 'q' TO QUIT.")
            if continueGame == 'x':
                playerCards.append(DealCards())
            elif continueGame == 'q':
                print("YOU LEFT THE GAME...COWARD")
                gameOver = True
                quit()
            else:
                print("INVALID INPUT. PLEASE TRY AGAIN.")
                continueGame
    
    while computerScore != 0 and computerScore < 17:
        computerCards.append(DealCards())
        computerScore = CalcScore(computerCards)

    print(f"YOUR FINAL HAND: {playerCards}, FINAL SCORE: {playerScore}")
    print(f"COMPUTER'S FINAL HAND: {computerCards}, FINAL SCORE: {computerScore}")
    print(CompareScore(playerScore, computerScore))

#play the game  
goplay()

