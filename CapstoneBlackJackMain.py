import random
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())



  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:

      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True


  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()





#MY ROUGH WORK BELOW - aabove is more fine tuned, below works fine too, just missing some edge cases, which can be easily added

#from replit import clear
# from art import logo
# import random
# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# playerList = []
# dealerList = []
# playerScore = 0
# dealerScore = 0
# gameOn = True

# def randomCardGenerator(ncards):
#   return(random.choice(ncards))

# def addScore(cards):
#   return(sum(cards))

# wantToPlay = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")
# clear()
# print(logo)
# card = randomCardGenerator(cards)
# playerList.append(card)
# card = randomCardGenerator(cards)
# playerList.append(card)
# print(playerList)
# #print(f"Your cards [{playerhand}], your current score: {score}\n")
# card = randomCardGenerator(cards)
# dealerList.append(card)
# print(dealerList)
# playerScore = addScore(playerList)
# dealerScore = addScore(dealerList)
# print(playerScore)
# print(dealerScore)
# while gameOn == True:
#   inputNew = input("'y' or 'n'")
#   if inputNew == 'y':
#     card = randomCardGenerator(cards)
#     playerList.append(card)
#     print(playerList)
#     playerScore = addScore(playerList)
#     print(playerScore)
#     if playerScore > 21:
#       print("You lost!!! Dealer wins hand")
#       gameOn = False
#   elif inputNew == 'n':
#     while dealerScore <= 21:
#       card = randomCardGenerator(cards)
#       dealerList.append(card)
#       print(dealerList)
#       dealerScore = addScore(dealerList)
#       print(dealerScore)
#       if dealerScore > playerScore and dealerScore <= 21:
#         print("You lost!! Dealer wins")
#         gameOn = False
#       elif dealerScore > 21:
#         print("You win!! Dealer lost")
#         gameOn = False