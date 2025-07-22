# Ryan Lopez & Ysani Pena
# _____________________
# Fundamentals of Software Design 215
# _____________________
# Project - Poker Hand Calculator
# _____________________
# Setup instructions:
#All you will need to download is PySide6 on your computer 
# _____________________
# Sources:
#https://realpython.com/python-sockets/#:~:text=The%20.accept()%20method%20blocks,flowinfo%2C%20scopeid)%20for%20IPv6.
#https://www.pythonguis.com/tutorials/pyside6-widgets/
#https://www.pythonguis.com/tutorials/pyside6-layouts/
# APP WE WERE INSPIRED BY: https://apps.apple.com/us/app/evenbet-poker-calculator/id1445519206
#Previous personal code of ours
# _____________________
# 11/19/23 - Start structure
# 11/20/23 - worked PHC_Display()
# 11/21/23 - worked PHC_Display()
# 11/26/23 - worked PHC_Display()
# 11/27/23 - worked PHC_Display()
# 11/29/23 - created Class Cardpop for the card numbers popup
# 11/30/23 - worked on Class Cardpop
# 12/1/23 - worked on Class Cardpop and card_button_clicked()
# 12/2/23 - worked on Class Cardpop, card_button_clicked() and accept_card()
# 12/4/23 - worked on reset_cards() and calculate_winner()
# 12/5/23 - worked on calculate_winner()
# 12/6/23 - worked on figuring royal flush, straight flush and flush in determine_hand()
# 12/7/23 - worked on calculate_winner() and determine_hand()
# 12/8/23 - worked on calculate_winner() and determine_hand() 
# 12/10/23 - worked on calculate_winner() and determine_hand() 
# 12/11/23 - worked on calculate_winner() and determine_hand() 
# 12/12/23 - wrapped up and finalized calculate_winner() and determine_hand() and made some color adjustements 
# 12/13/23 - finished doctesting 


from collections import Counter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, \
    QGridLayout, QLabel, QDialog, QHBoxLayout, QMessageBox


class PokerHandCalculator(QMainWindow):
    def __init__(self):
        super(PokerHandCalculator, self).__init__()
        self.setWindowTitle("Poker Hand Calculator")
        self.PHC_Display()
        self.setFixedSize(500, 700)
        # background color for the main window
        self.setStyleSheet("background-color: black;")
        # Set content margins for the grid layout
        self.setContentsMargins(5, 5, 5, 5)
        self.used_cards = []
        self.used_buttons = []
     
    def PHC_Display(self):
       
        # This creates a central widget to hold the layout for Poker Hand Calculator
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # This will create the horizontal layout
        top_overall_layout = QVBoxLayout()

        board_names = QHBoxLayout()
        cards = QHBoxLayout()

        player1_name = QHBoxLayout()
        player1_cards = QHBoxLayout()
        player2_name = QHBoxLayout()
        player2_cards = QHBoxLayout()

        # Add label widgets
        board_names.addStretch(2)
        self.flop = QLabel('FLOP')
        self.flop.setStyleSheet("color: white; font-size: 10px; font-weight: bold; ")
        board_names.addWidget(self.flop)
        board_names.addStretch(3)

        self.turn = QLabel('TURN')
        self.turn.setStyleSheet("color: white;font-size: 10px; font-weight: bold; ")
        board_names.addWidget(self.turn)
        board_names.addStretch(1)
       
        self.river = QLabel('RIVER')
        self.river.setStyleSheet("color: white;font-size: 10px; font-weight: bold; ")
        board_names.addWidget(self.river)
        board_names.addStretch(1)
   
        player1_name.addStretch(1)
        self.player1_heading = QLabel('PLAYER 1')
        self.player1_heading.setStyleSheet("color: white;font-size: 10px; font-weight: bold; ")
        player1_name.addWidget(self.player1_heading)
        player1_name.addStretch(1)

        player2_name.addStretch(1)
        self.player2_heading = QLabel('PLAYER 2')
        self.player2_heading.setStyleSheet("color: white; font-size: 10px; font-weight: bold; ")
        player2_name.addWidget(self.player2_heading)
        player2_name.addStretch(1)
       
        # Add card widgets
        self.flop1 = QLabel(self)
        self.flop1.setFixedSize(75, 100)
       
        self.flop1.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2; ")
        cards.addWidget(self.flop1)
       
        self.flop2 = QLabel(self)
        self.flop2.setFixedSize(75, 100)
        self.flop2.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2;")  
        cards.addWidget(self.flop2)
       
        self.flop3 = QLabel(self)
        self.flop3.setFixedSize(75, 100)
        self.flop3.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2;")
        cards.addWidget(self.flop3)
        cards.addStretch(1)
       
        self.turn = QLabel(self)
        self.turn.setFixedSize(75, 100)
        self.turn.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2;")
        cards.addWidget(self.turn)
        cards.addStretch(1)
       
        self.river = QLabel(self)
        self.river.setFixedSize(75, 100)
        self.river.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2;")
        cards.addWidget(self.river)
        cards.addStretch(1)

        player1_cards.addStretch(1)
        self.player1_card1 = QLabel(self)
        self.player1_card1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.player1_card1.setFixedSize(75, 100)
        self.player1_card1.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2;")
        player1_cards.addWidget(self.player1_card1)

        self.player1_card2 = QLabel(self)
        self.player1_card2.setFixedSize(75, 100)
        self.player1_card2.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2;")
        player1_cards.addWidget(self.player1_card2)
        player1_cards.addStretch(1)

        player2_cards.addStretch(1)
        self.player2_card1 = QLabel(self)
        self.player2_card1.setFixedSize(75, 100)
        self.player2_card1.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2;")
        player2_cards.addWidget(self.player2_card1)

        self.player2_card2 = QLabel(self)
        self.player2_card2.setFixedSize(75, 100)
        self.player2_card2.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2;")
        player2_cards.addWidget(self.player2_card2)
        player2_cards.addStretch(1)

        # This will hold a master list of all the locations of the buttons
        calc_buttons = QGridLayout(central_widget)

        # This will set the spacing between the buttons
        calc_buttons.setHorizontalSpacing(10)
        calc_buttons.setVerticalSpacing(20)

        # This will make the grid layout with buttons in the 3 x 3
        self.buttons = []

        # This will create the buttons for the main calculator
        for i in range(2):
            self.row_buttons = []  # this is to capture what position in the row the button is on
            for n in range(4):
                self.button = QPushButton()
                self.button.setFixedSize(50, 50)  # This will set a fixed size
                # This will set the background color of the button
                self.button.setStyleSheet("background-color: gray;")
                calc_buttons.addWidget(self.button, i, n)
                self.row_buttons.append(self.button)  # assigns the button to the row list

            self.buttons.append(self.row_buttons)  # assigns the button on the row to the master list

        # Nums/Text on the calculator buttons
        self.buttons[0][0].setText('\u2660')
        self.buttons[0][0].setStyleSheet("font-size: 30px; background-color: gray;")
        self.buttons[0][0].clicked.connect(lambda: self.show_card_popup('Spades'))
        self.buttons[0][1].setText('\u2665')
        self.buttons[0][1].setStyleSheet("color: red; background-color: gray; font-size: 30px;")
        self.buttons[0][1].clicked.connect(lambda: self.show_card_popup('Hearts'))
        self.buttons[0][2].setText('\u2666')
        self.buttons[0][2].setStyleSheet("color: red; background-color: gray; font-size: 30px;")
        self.buttons[0][2].clicked.connect(lambda: self.show_card_popup('Diamonds'))
        self.buttons[0][3].setText('\u2663')
        self.buttons[0][3].setStyleSheet("font-size: 30px; background-color: gray;")
        self.buttons[0][3].clicked.connect(lambda: self.show_card_popup('Clubs'))

        self.buttons[1][1].setText('Reset')
        self.buttons[1][1].clicked.connect(self.reset_cards)
        self.buttons[1][2].setText('Compute')
        self.buttons[1][2].clicked.connect(self.calculate_winner)

        self.buttons[1][0].setVisible(False)
        self.buttons[1][3].setVisible(False)

        # adds the flop_w_cards layout to the top_overall_layout
        top_overall_layout.addLayout(board_names)
        top_overall_layout.addLayout(cards)

        top_overall_layout.addLayout(player1_name)
        top_overall_layout.addLayout(player1_cards)

        top_overall_layout.addLayout(player2_name)
        top_overall_layout.addLayout(player2_cards)

        main_layout.addLayout(top_overall_layout)

        main_layout.addLayout(calc_buttons)

        # This sets the layout for the central widget
        self.setLayout(main_layout)

    # this function is used for when the user needs to customize which card they have
    def show_card_popup(self, suit):
        popup = CardPopup(suit, self.used_cards, self.used_buttons) #will pass used_cards to the popup
        result = popup.exec()
        if result:
            selected_card = popup.selected_card

            # Updates the label on the main window with the selected card information
            all_cards = [self.flop1, self.flop2, self.flop3, self.turn, self.river, self.player1_card1, self.player1_card2, self.player2_card1, self.player2_card2]

            if suit == 'Spades':
                suit_symbol = '\u2660'
            elif suit == 'Hearts':
                suit_symbol = '\u2665'
            elif suit == 'Diamonds':
                suit_symbol = '\u2666'
            else:
                suit_symbol = '\u2663'

            for card in all_cards:
                if card.text() == "":
                    if suit_symbol == '\u2665' or suit_symbol == '\u2666':
                        card.setText(f'<html><head/><body>'
                                    f'<div style="text-align: left; color: red;">{selected_card}</div>'
                                    f'<div style="font-size: 40px; text-align: center; color: red;">{suit_symbol}</div>'
                                    f'<div style="text-align: right; color: red;">{selected_card}</div>'
                                    f'</body></html>')
                        card.setStyleSheet("background-color: white; border: 3px solid #ccc; height: 5; width: 2; ")
                        break
                    else:# Use HTML formatting to customize the text placement
                        card.setText(f'<html><head/><body>'
                                    f'<div style="text-align: left;">{selected_card}</div>'
                                    f'<div style="font-size: 40px; text-align: center;">{suit_symbol}</div>'
                                    f'<div style="text-align: right;">{selected_card}</div>'
                                    f'</body></html>')
                        card.setStyleSheet("background-color: black; border: 3px solid #ccc; height: 5; width: 2; ")
                        break

    def reset_cards(self):
        self.used_cards = []
        all_cards = [self.flop1, self.flop2, self.flop3, self.turn, self.river, self.player1_card1, self.player1_card2, self.player2_card1, self.player2_card2]

        for card in all_cards:
            card.setText("")
            card.setStyleSheet("background-color: gray; border: 3px solid #ccc; height: 5; width: 2;")

    def calculate_winner(self):
       
        if len(self.used_cards) != 9:
            message = QMessageBox()
            message.setText("Cannot calculate! Need more information")
            message.exec_()
        else:
            player1_list = []
            for n in range(7):
                player1_list.append(self.used_cards[n])
            player1_hand = self.determine_hand(player1_list)

            player2_list = []
            for m in range(9):
                if m == 5 or m == 6:
                    continue
                else:
                    player2_list.append(self.used_cards[m])

            player2_hand = self.determine_hand(player2_list)


        hands = {
                'royal_flush': 10,
                'straight_flush': 9,
                'four_of_a_kind': 8,
                'full_house': 7,
                'flush': 6,
                'straight': 5,
                'three_of_a_kind': 4,
                'two_pair': 3,
                'one_pair': 2,
                'high_card': 1
            }

        messageBox = QMessageBox()
        messageBox.setWindowTitle("Calculated")
        
        #These sets of conditionals will calculate the winner between player1's hand and player2's hand
        if player1_hand == player2_hand:
            messageBox.setText("Split pot!")
        else:
            player1_h_list = player1_hand.split()
            player2_h_list = player2_hand.split()
            player1_hand_string = player1_h_list[0]
            player2_hand_string = player2_h_list[0]
           
            if player1_h_list[0] == player2_h_list[0]:
                player1_score1 = int(player1_h_list[1])       # Assigns the initial strength of the hand (first number)
                player2_score1 = int(player2_h_list[1])
               
                if player1_score1 == player2_score1:
                    player1_score2 = int(player1_h_list[2])
                    player2_score2 = int(player2_h_list[2])
                    if player1_score2 > player2_score2:       # Checks if the first number strenth is the same, if it is, must check the second 
                        messageBox.setText(f"Player 1 is the winner with {player1_hand_string}")
                    elif player1_score2 < player2_score2:
                        messageBox.setText(f"Player 2 is the winner with {player2_hand_string}")
                    else:
                        player1_score3 = int(player1_h_list[3])
                        player2_score3 = int(player2_h_list[3])
                        if player1_score3 > player2_score3:
                            messageBox.setText(f"Player 1 is the winner with {player1_hand_string}")       
                        elif player1_score3 < player2_score3:
                            messageBox.setText(f"Player 2 is the winner with {player2_hand_string}")                    
                        else:
                            player1_score4 = int(player1_h_list[4])
                            player2_score4 = int(player2_h_list[4])
                            if player1_score4 > player2_score4:
                                messageBox.setText(f"Player 1 is the winner with {player1_hand_string}")
                            elif player1_score4 < player2_score4:
                                messageBox.setText(f"Player 2 is the winner with {player2_hand_string}")
                            else:
                                player1_score5 = int(player1_h_list[5])
                                player2_score5 = int(player2_h_list[5])
                                if player1_score5 > player2_score5:
                                    messageBox.setText(f"Player 1 is the winner with {player1_hand_string}")
                                elif player1_score5 < player2_score5:
                                    messageBox.setText(f"Player 2 is the winner with {player2_hand_string}")
                elif player1_score1 > player2_score1:
                    messageBox.setText(f"Player 1 is the winner with {player1_hand_string}")
                else:
                    messageBox.setText(f"Player 2 is the winner with {player2_hand_string}")
            else:
                if hands[player1_hand_string] > hands[player2_hand_string]:
                    messageBox.setText(f"Player 1 is the winner with {player1_hand_string}")
                else:
                    messageBox.setText(f"Player 2 is the winner with {player2_hand_string}")
        messageBox.exec()

    def determine_hand(self, cards : list):
        """ Determines the hand of the player
        >>> PokerHandCalculator().determine_hand(['JSpades', '8Hearts', '10Spades', '4Diamonds', 'QSpades', 'KSpades', 'ASpades'])
        'royal_flush 0 0 0'
        >>> PokerHandCalculator().determine_hand(['JSpades', '8Hearts', '10Spades', '4Diamonds', 'QSpades', '8Spades', '9Spades'])
        'straight_flush 12 0 0'
        >>> PokerHandCalculator().determine_hand(['4Spades', '4Hearts', '9Diamonds', '2Clubs', '4Diamonds', '4Clubs', '3Diamonds'])
        'four_of_a_kind 4 9'
        >>> PokerHandCalculator().determine_hand(['4Hearts', '9Clubs', '6Spades', '4Spades', '9Diamonds', '9Hearts', '2Spades'])
        'full_house 9 4'
        >>> PokerHandCalculator().determine_hand(['7Hearts', '8Hearts', '2Clubs', '5Spades', 'KHearts', '3Hearts', '4Hearts'])
        'flush 13 8 7'
        >>> PokerHandCalculator().determine_hand(['3Spades', '5Hearts', '7Diamonds', 'KClubs', '10Spades', '4Hearts', '6Spades'])
        'straight 7'
        >>> PokerHandCalculator().determine_hand(['9Spades', 'JDiamonds', '4Clubs', '3Spades', '4Diamonds', 'KSpades', '4Hearts'])
        'three_of_a_kind 4 13 11'
        >>> PokerHandCalculator().determine_hand(['9Clubs', '7Diamonds', '3Hearts', '3Diamonds', '6Spades', '6Clubs', '5Spades'])
        'two_pair 6 3 9'
        >>> PokerHandCalculator().determine_hand(['KClubs', '5Spades', '10Diamonds', '7Hearts', 'JSpades', '5Hearts', '9Diamonds'])
        'one_pair 5 13 11 10'
        >>> PokerHandCalculator().determine_hand(['KClubs', 'JDiamonds', '9Hearts', '4Spades', '10Spades', '5Diamonds', '7Clubs'])
        'high_card 13 11 10 9 7'
        """
        #royal flush, straight flush, four of a kind, full house, flush, straight, three of a kind, two pair, one pair, high card.
        has_flush = False
        flushed_suit = ''
        #Check if there is a flush
        spade_count, heart_count, diamond_count, club_count = 0, 0, 0, 0
        for card in cards:
            if 'Spades' in card:
                spade_count += 1
            elif 'Hearts' in card:
                heart_count += 1
            elif 'Diamonds' in card:
                diamond_count += 1
            elif 'Clubs' in card:
                club_count += 1

        if spade_count >= 5:
            has_flush = True
            flushed_suit = 'Spades'
        elif heart_count >= 5:
            has_flush = True
            flushed_suit = 'Hearts'
        elif diamond_count >= 5:
            has_flush = True
            flushed_suit = 'Diamonds' 
        elif club_count >= 5:
            has_flush = True
            flushed_suit = 'Clubs'

        #Check if there is a royal or straight flush
        if has_flush == True:
            # Check for Royal Flush
            if '10' + flushed_suit in cards and 'J' + flushed_suit in cards and 'Q' + flushed_suit in cards and 'K' + flushed_suit in cards and 'A' + flushed_suit in cards:
                return f"royal_flush {0} {0} {0}"    
            else:
                # Check for Straight Flush
                potential_SF = []
                for card in cards:
                    if flushed_suit in card:
                        potential_SF.append(card)

                card_values = {'A_1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

                potential_SF_values = []
                for card in potential_SF:
                    if 'A' in card:
                        # Check if there is a 2, 3, 4, 5 in the cards
                        if all(str(value) in ''.join(potential_SF) for value in range(2, 6)):
                            potential_SF_values.append(card_values['A_1'])  # Append 1 for 'A' in the special straight
                        else:
                            potential_SF_values.append(card_values['A'])  # Append 14 for 'A' in any other occurence
                    elif card[:2] == '10':
                        temp_num = card[:2]
                        potential_SF_values.append(card_values[temp_num])
                    else:
                        temp_num = card[0]
                        potential_SF_values.append(card_values[temp_num])

                potential_SF_values.sort()
               
                count = 0
                straight_flush = []
               
                #this for loop checks of its a straight flush or not
                for index, value in enumerate(potential_SF_values):
                    if index == (len(potential_SF_values) -  1):
                        if (value - 1) == potential_SF_values[index - 1]:
                            count +=1
                            straight_flush.append(potential_SF_values[index])
                        else:
                            break
                    else:
                        if (value + 1) == potential_SF_values[index + 1]:
                            count += 1
                            straight_flush.append(potential_SF_values[index])
                        else:
                            break

                if count >= 5:
                    return f"straight_flush {straight_flush[-1]} {0} {0}"
                else:
                    large_val = 0
                    for val in potential_SF_values:
                        if val > large_val:
                            large_val = val
                    
                     #this will remove the highest card value from the list in case of the same high card for flush
                    second_temp_list = potential_SF_values
                    second_temp_list = [val for val in second_temp_list if val != large_val]

                    sec_highest_card_val = 0
                    for val in second_temp_list:
                        if val > sec_highest_card_val:
                            sec_highest_card_val = val
                    
                    second_temp_list = [val for val in second_temp_list if val != sec_highest_card_val]

                    third_highest_card_val = 0
                    for val in second_temp_list:
                        if val > third_highest_card_val:
                            third_highest_card_val = val

                    return f"flush {large_val} {sec_highest_card_val} {third_highest_card_val}"

        # No flush, now checks for all the remaining hands
        elif not has_flush:
           
            card_values = {'A_1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
            rank_list = []

            for card in cards:
                if 'A' in card:
                    # Check if there is a 2, 3, 4, 5 in the cards
                    if all(str(value) in ''.join(cards) for value in range(2, 6)):
                        rank_list.append(card_values['A_1'])  # Append 1 for 'A' in the special straight
                    else:
                        rank_list.append(card_values['A'])  # Append 14 for 'A' in any other occurence
                elif card[:2] == '10':
                    temp_num = card[:2]
                    rank_list.append(card_values[temp_num])
                else:
                    temp_num = card[0]
                    rank_list.append(card_values[temp_num])

            straight_list = rank_list
            
            #the counter method will check through the rank_list to identify which values are repeated the most
            #Counter is a class from the collections module that is used for counting the occurrences of elements in a collection, typically in a list or string
            vals = Counter(rank_list)

            max_count = 0
            repeated_val = None

            #this will loop through the dictionary 'vals' that iterates over the items of a dictionary using items()
            #The items() method is used in for loops to iterate over the keys and values of a dictionary simultaneously.
            #This will assign the most repeated value to repeated_val and the amount of times that value repeated to max_count
            for number, count in vals.items():
                if count >= max_count:
                    #this will replace the repeated val if theres one that is greater with the same count
                    if count == max_count:
                        if number > repeated_val:
                            repeated_val = number
                    else:
                        #this is simply for the first iteraton when max_count and repeated val is set to 0
                        max_count = count
                        repeated_val = number

            #Lines 436 - 451 is similar to the code above but will be used to find the second most repeated value in the rank_list
            sec_max_count = 0
            sec_repeated_val = None
            temp_list = rank_list

            #will get rid of the highest repeated value from this temp_list to find the second highest repeated value
            temp_list = [val for val in temp_list if val != repeated_val]
      

            updated_vals = Counter(temp_list)

            for number, count in updated_vals.items():
                if count >= sec_max_count:
                     #this will replace the repeated val if theres one that is greater with the same count
                    if count == sec_max_count:
                        if number > sec_repeated_val:
                            sec_repeated_val = number
                    else:
                        #this is simply for the first iteraton when sec_max_count and sec_repeated val is set to 0
                        sec_max_count = count
                        sec_repeated_val = number
            
            highest_card_val = 0
            sec_highest_card_val = 0
            third_highest_card_val = 0
            fourth_highest_card_val = 0
            fifth_highest_card_val = 0
            second_temp_list = rank_list

            #4 of a kind
            if max_count == 4:

                #this will remove the highest repeated card value from the list
                second_temp_list = [val for val in second_temp_list if val != repeated_val]

                for vals in second_temp_list:
                    if vals > highest_card_val:
                        highest_card_val = vals

                  
            #FULL HOUSE WITH 2 three of a kinds (to find the higher three of a kind needed for the full house)
            elif max_count == 3 and sec_max_count >= 2:
                #this will find the higher three of a kind

                if repeated_val > sec_repeated_val:
                    highest_card_val = repeated_val
                    sec_highest_card_val = sec_repeated_val
                else:
                    highest_card_val = sec_repeated_val
                    sec_highest_card_val = repeated_val


            # CHECKS FOR STRAIGHT HAND (max_count is >=1 because there could still be a straight with a 2 pair or 3 pair on the board)
            elif max_count >= 1:
                straight_list.sort()
                count = 1
                max_straight = 0

                for n in range(6):
                    if straight_list[n] + 1 == straight_list[n + 1]:
                        count += 1
                        if count >= 5:
                            max_straight = straight_list[n + 1]
                            if straight_list[n] + 2 == straight_list[-1]:
                                max_straight = straight_list[-1]
                            else:
                                break  
                    else:
                        count = 1
                    
                if max_straight != 0 and count >= 5:
                    return f"straight {max_straight}"
                else:
                
                    #THREE OF A KIND
                    if max_count == 3:

                        #this will remove the highest repeated card value from the list
                        second_temp_list = [val for val in second_temp_list if val != repeated_val]
                        
                        for vals in second_temp_list:
                            if vals > highest_card_val:
                                highest_card_val = vals
                        
            
                        second_temp_list.remove(highest_card_val)

                        #this will find the second highest_card value
                        for vals in second_temp_list:
                            if vals > sec_highest_card_val:
                                sec_highest_card_val = vals

                    # TWO PAIR
                    elif (max_count == 2) and (sec_max_count == 2):

                        #this will remove the highest and second highest repeated card value from the list
                        second_temp_list = [val for val in second_temp_list if val != repeated_val]
                        second_temp_list = [val for val in second_temp_list if val != sec_repeated_val]
                        
                        for vals in second_temp_list:
                            if vals > highest_card_val:
                                highest_card_val = vals
                        highest_card_extra = highest_card_val


                    #ONE PAIR
                    elif max_count == 2:

                        #this will remove the highest repeated card value from the list
                        second_temp_list = [val for val in second_temp_list if val != repeated_val]

                        #finds the highest_card_value
                        for vals in second_temp_list:
                            if vals > highest_card_val:
                                highest_card_val = vals

                        second_temp_list.remove(highest_card_val)


                        #this will find the second highest_card value
                        for vals in second_temp_list:
                            if vals > sec_highest_card_val:
                                sec_highest_card_val = vals

                        second_temp_list.remove(sec_highest_card_val)

                        #this will find the third highest_card value
                        for vals in second_temp_list:
                            if vals > third_highest_card_val:
                                third_highest_card_val = vals

                    #HIGH CARD
                    elif max_count == 1:

                        #finds the highest_card_value
                        for vals in second_temp_list:
                            if vals > highest_card_val:
                                highest_card_val = vals

                        second_temp_list.remove(highest_card_val)


                        #this will find the second highest_card value
                        for vals in second_temp_list:
                            if vals > sec_highest_card_val:
                                sec_highest_card_val = vals

                        second_temp_list.remove(sec_highest_card_val)

                        #this will find the third highest_card value
                        for vals in second_temp_list:
                            if vals > third_highest_card_val:
                                third_highest_card_val = vals
                        
                        second_temp_list.remove(third_highest_card_val)

                        #this will find the fourth highest_card value
                        for vals in second_temp_list:
                            if vals > fourth_highest_card_val:
                                fourth_highest_card_val = vals

                        second_temp_list.remove(fourth_highest_card_val)

                        #this will find the fifth highest_card value
                        for vals in second_temp_list:
                            if vals > fifth_highest_card_val:
                                fifth_highest_card_val = vals


            #Here the following conditionals check for hands
            if max_count == 4:
                return f"four_of_a_kind {repeated_val} {highest_card_val}"
            elif max_count == 3 and sec_max_count == 3:
                return f"full_house {highest_card_val} {sec_highest_card_val}"
            elif max_count == 3 and sec_max_count == 2:
                return f"full_house {repeated_val} {sec_repeated_val}"
            elif max_count == 3:
                return f"three_of_a_kind {repeated_val} {highest_card_val} {sec_highest_card_val}"
            elif max_count == 2 and sec_max_count == 2:
                #Sets the order of the strength of two pair (highest pair, second pair, high card)
                if sec_repeated_val > repeated_val:
                    return f"two_pair {sec_repeated_val} {repeated_val} {highest_card_extra}"
                else:
                    return f"two_pair {repeated_val} {sec_repeated_val} {highest_card_extra}"
            elif max_count == 2:
                return f"one_pair {repeated_val} {highest_card_val} {sec_highest_card_val} {third_highest_card_val}"
            elif max_count == 1:
                return f"high_card {highest_card_val} {sec_highest_card_val} {third_highest_card_val} {fourth_highest_card_val} {fifth_highest_card_val}"

#class needed for the card pop up
class CardPopup(QDialog):
    def __init__(self, suit, used_cards, used_buttons):
        super(CardPopup, self).__init__()
        self.used_cards = used_cards
        self.used_buttons = used_buttons
       

        self.setWindowTitle(f"Select Card for {suit}")
        self.setGeometry(300, 300, 300, 300)
        self.setStyleSheet("background-color: black;")

        layout = QGridLayout(self)

        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # i = index of card, card = literal value of card
        for i, card in enumerate(cards):
            full_card = card + suit
            if full_card in self.used_cards:
                button = QPushButton(card)
                button.setStyleSheet("color: red; border: 4px solid red;")
                button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                button.clicked.connect(self.card_button_clicked)
                layout.addWidget(button, i // 4, i % 4)
                button.setEnabled(False)
                continue
           
            button = QPushButton(card)
            button.setStyleSheet("color: white; border: 4px solid white;")
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus) #This makes sure none of the buttons are highlighted/selected
            button.clicked.connect(self.card_button_clicked) # Connect the slot method
            layout.addWidget(button, i // 4, i % 4) #this creates the grid for the numbers in the pop up

        self.selected_card = None

    def card_button_clicked(self):
        sender_button = self.sender()  # Get the button that emitted the signal
        card_num = sender_button.text()
        suit_name = self.windowTitle().split()[-1]  # Extract suit from the window title
        card = card_num + suit_name

        if card not in self.used_cards:
            self.used_cards.append(card)
            # Change appearance
            self.accept_card(sender_button.text())
           
    def accept_card(self, card):
        self.selected_card = card
        self.accept()  # This will close the dialog

app = QApplication()
window = PokerHandCalculator()
window.show()
app.exec()


if __name__ == "__main__":
    import doctest
    doctest.testmod()





