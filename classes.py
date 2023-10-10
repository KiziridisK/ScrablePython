import math as m
import random as r
import itertools as it
import json


class Player:
    pass


# Η κλάση που αναπαριστά το σακουλάκι των γραμμάτων
class SakClass:

    # Κατασκευαστής της κλάσης
    def __init__(self, letters):
        self.letters = letters
        self.numOfLetters = 104

    # Μέθοδος η οποία δίνει γράμματα στους παίκτες (είτε τα αρχικα είτε τα αλλάζει στο 'πάσο')
    def getletters(self):

        i = 0
        player_letters = []
        keys = list(self.letters)

        for i in range(7):
            temp = r.randint(0, 23)
            key = keys[temp]
            player_letters.append([key, self.letters[key][1]])
            self.letters[key][0] -= 1

        # print('Remaining letters in the sack: ', self.numOfLetters - 7)
        self.numOfLetters -= 7
        return player_letters

    # Μέθοδος που επιστρέφει τα γράμματα στο σακουλάκι αν ο πα΄ίκτης επιλέξει 'πάσο'
    def putbackletters(self, v: Player):

        i = 0
        for i in range(len(v.letters)):
            self.letters[v.letters[i][0]][0] += 1

        print('Letters were put back to the sack. Remaining letters: ', self.numOfLetters + len(v.letters))
        self.numOfLetters += len(v.letters)
        v.letters = []

    # Μέθοδος που συμπληρώνει τα γράμματα των παικτών αφού βρούνε επιτυχώς λέξη
    def replenishLetters(self, numOfLettersToGive):
        i = 0
        player_letters = []
        keys = list(self.letters)

        for i in range(numOfLettersToGive):
            temp = r.randint(0, 23)
            key = keys[temp]
            player_letters.append([key, self.letters[key][1]])
            self.letters[key][0] -= 1

        print('Remaining letters in the sack: ', self.numOfLetters - numOfLettersToGive)
        self.numOfLetters -= numOfLettersToGive
        return player_letters

    # Επέκταση της μεθόδου repr για να εμφανίζει κατάλληλα δεδομένα για την κλάση
    def __repr__(self):

        return f'Object from Class: {self.__class__}, containing: {self.numOfLetters} letters'

    # Επέκταση της μεθόδου str για να εμφανίζει κατάλληλα δεδομένα για την κλάση
    def __str__(self):

        return f' Object from class: {self.__class__}, containing {self.numOfLetters} letters'


# Κλάση που αναπαριστά τους παίκτες
class Player:

    # Κατασκευαστής της κλάσης που αρχικοποιεί τα αντικείμενα
    def __init__(self, name):
        self.points = 0
        self.letters = []
        self.name = name

    # Υπερφόρτωση της μεθόδου repr (represent)
    def __repr__(self):
        return f'Class: {self.__class__}, Name: {self.name}, Points: {self.points}, Letters: {self.letters}'

    # Υπερφόρτωση της μεθόδου srt
    def __str(self):
        return f'Player name: {self.name}, Player points: {self.points}, Player letters: {self.letters}'

    # Μέθοδος που ελέγχει εάν ο παίκτης μπορεί να σχηματίσει μία λέξη με βάση τα γράμματά του (χρειάζεται μόνο στον άνθρωπο)
    def canFormWord(self, word):

        i = 0
        lettersAlone = []

        # Από τα γράμματα του παίκτη κρατούνται μόνο τα γράμματα (χωρίς την αξία τους).
        for i in range(len(self.letters)):
            lettersAlone.append(self.letters[i][0])

        for i in range(len(word)):
            if word[i] in lettersAlone:
                continue
            else:
                return False

        return True

    # Μέθοδος που ελέγχει εάν μία λέξη η οποία μπορεί να σχηματιστεί βρίσκεται εντός των αποδεκτών
    def isAcceptableWord(self, word, words):

        if word in words:
            return True
        else:
            return False

    # Μέθοδος που σβήνει τα χρησιμοποιημένα γράμματα και συμπληρώνει με άλλα αφού βρεθεί επιτυχώς μία λέξη
    def removeUsedLettersAndGiveNew(self, word, s: SakClass):
        # Get new letters
        newLetters = s.replenishLetters(7 - len(word))
        lettersToDelete = []

        # Delete used letters
        i = 0
        for i in range(len(word)):
            for j in range(len(self.letters)):
                if word[i] == self.letters[j][0]:
                    lettersToDelete.append(word[i])

        lettersOnly = []
        indexes = []
        i = 0
        for i in range(len(self.letters)):
            lettersOnly.append(self.letters[i][0])

        i = 0
        for i in range(len(lettersToDelete)):
            if lettersToDelete in lettersOnly:
                indexes[i] = lettersOnly.index(lettersToDelete[i])

        i = 0
        for i in range(len(indexes)):
            del self.letters[i]

        # Insert new letters
        self.letters.extend(newLetters)

    def wantToQuit(self):

        print('Would you like to end the game or pass?')
        quit = input("Type 'p' for pass, 'quit' for quit: ")
        return quit

    # Μέθοδος που υλοποιεί τις συνθήκες του γύρου για τον παίκτη (Χρησιμοποιείται για τον άνθρωπο)
    def play(self, s: SakClass, turn, words):

        # Ερώτηση προς τον παίκτη για το αν θα παίξει ή θα πάει "πάσο"
        print('Choose your next move. Play or Pass or End Game? Type play or p or quit.')
        choice = input("Player's choice: ")
        points = 0
        i = 0
        flag = True

        # Πράξεις προγράμματος αν ο πα΄ίκτης πάει πάσο
        if choice.lower() == "p":
            # Επιστρέφονται τα γράμματα, δίνονται καινούρια, αλλαγή σειράς και ενημέρωση για νέα γράμματα.
            s.putbackletters(self)
            if s.numOfLetters > 7:
                self.letters = s.getletters()
                print('Player ', self.name, 'you have lost your turn. Now Computer is playing.')
                print(self)
                turn = 1
                return turn
            else:
                print('There are not enough letters to change. The game is over')
                turn = "quit"
                return turn
        elif choice.lower() == "play":
            # Πράξεις προγράμματος αν ο παίκτης επιλέξει να παίξει.
            while flag:
                # Ο παίκτης γράφει την λέξη του, ελέγχεται αρχικά αν μπορεί να σχηματιστεί και έπειτα αν είναι αποδεκτή.
                word = input('Type your word: ')
                upperWord = word.upper()
                if self.canFormWord(upperWord):
                    if self.isAcceptableWord(upperWord, words):
                        # Αν είναι έγκρυση δίνονται υπολογίζονται οι νέοι πόντοι και δίνεται σχετικό μήνυμα.
                        for i in range(len(upperWord)):
                            points += s.letters[upperWord[i]][1]
                        print("Correct word. You win ", points, 'points!')
                        # Δίνονται νέα γράμματα, αλλαγή σειράς, ενημέρωση μεταβλητών
                        self.removeUsedLettersAndGiveNew(upperWord, s)
                        self.points += points
                        print(self)
                        turn = 1
                        flag = False
                        break
                    else:
                        print("The given word was not valid.")
                        quit = self.wantToQuit()
                        print(quit)
                        if quit.lower() == "quit":
                            turn = "quit"
                            flag = False
                            break
                        elif quit.lower() == "p":
                            if s.numOfLetters > 7:
                                self.letters = s.getletters()
                                print('Player ', self.name, 'you have lost your turn. Now Computer is playing.')
                                print(self)
                                turn = 1
                                return turn
                            else:
                                print('There are not enough letters to change. The game is over')
                                turn = "quit"
                                return turn
                        elif quit.lower() == "c":
                            flag = True
                else:
                    print("This word cannot be formed. You have lost your turn.")
                    if s.numOfLetters > 7:
                        self.letters = s.getletters()
                        print('Player ', self.name, 'you have lost your turn. Now Computer is playing.')
                        print(self)
                        turn = 1
                        return turn
                    else:
                        print('There are not enough letters to change. The game is over')
                        turn = "quit"
                        return turn
                    turn = 1
                    return turn
        elif choice.lower() == "quit":
            turn = "quit"

        return turn


# Η κλάση του παίκτη - ανθρώπου.
# Η κλάση αυτή κληρονομεί ο,τι χρειάζεται απ' την κλάση Player.
class Human(Player):
    pass


# Η κλάση του υπολογιστή. Κληρονομεί την κλάση Player, αλλά καθώς είναι πιο ιδιαίτερη έχει και δικές τις μεθόδους
class Computer(Player):

    # Κατασκευαστής της κλάσης
    def __init__(self):
        self.points = 0
        self.letters = []
        # Το όνομα είναι σταθερά "Computer"
        self.name = 'Computer'

    # Μέθοδος που ελέγχει εάν μία λέξη είναι μεταξύ των αποδεκτών. Λειτουργεί με διαφορετικό τρόπο απ' αυτήν της
    # μητέρας κλάσης λόγω σχεδιασμού της μεθόδου Play. Ο υπολογιστής βρίσκει όλα τα δυνατά permutations των γραμμάτων του
    # και γι αυτό δεν χρειάζεται έλεγχος αν μπορεί να σχηματιστεί η λέξη που δίνει. Έπειτα ελέγχεται αν στα permutations
    # υπάρχει αποδεκτή λέξη.
    def isAcceptableWord(self, words, permutations):

        i = 0
        word = ''
        for i in range(len(permutations)):
            if permutations[i] in words:
                # Αν υπάρχει αποδεκτή λέξη τότε επιστρέφεται
                word = permutations[i]
                return word
            else:
                # Αν δεν υπάρχει αποδεκτή λέξη επιστρέφεται κενή συμβολοσειρά που υπόκειται σε έλεγχο στην μέθοδο play
                return word

    # Μέθοδος που ελέγχει την επάρκεια γραμμάτων στο σακουλάκι
    def checkEnd(self, s: SakClass):

        if s.numOfLetters >= 7:
            return True
        else:
            return False

    # Μέθοδος που αναπαριστά τις συνθήκες του παιχιδιού για τον υπολογιστή. Υλοποιήθηκε με την προσέγγιση min-max-smart
    def play(self, s: SakClass, mode, words, turn):

        flag = False
        i = 0
        lettersOnly = []
        points = 0
        foundWord = ''
        for i in range(len(self.letters)):
            lettersOnly.append(self.letters[i][0])

        # Πράξεις προγράμματος αν επιλεχθεί το mode "min" όπου αναζητούνται λέξεις μικρότερου μεγέθους πρ΄ω΄τα.
        if mode == 'min':
            wordLenght = 3
            # Αυξάνοντας το μέγεθος βρίσκουμε όλα τα δυνατά permutations
            while wordLenght < 8:
                permutations = []
                for permutation in it.permutations(lettersOnly, wordLenght):
                    permutations.append(permutation)
                for i in range(len(permutations)):
                    permutations[i] = ''.join(permutations[i])
                i = 0
                # Έλεγχος αν υπάρχει αποδεκτή λέξη ορισμένου μεγέθους
                foundWord = self.isAcceptableWord(words, permutations)
                if len(foundWord) > 0:
                    # Αν υπάρχει υπολογίζονται οι νέοι πόντοι, δίνεται σχετικό μήνυμα και ανανεώνονται τα γράμματα.
                    for i in range(len(foundWord)):
                        points += s.letters[foundWord[i]][1]
                    print("The computer plays word ", foundWord, "and wins ", points, 'points!')
                    self.points += points
                    self.removeUsedLettersAndGiveNew(foundWord, s)
                    print(self)
                    turn = 0
                    flag = True
                    break
                # Αν δεν υπάρχει αποδεκτή λέξη αυξάνουμε το μέγεθος.
                wordLenght += 1

            # Αν δεν βρεθεί αποδεκ΄τή λέξη σε κανένα πιθανό μέγεθος, τότε ο υπολογιστής αλλάζει γράμματα και την σειρά.
            if (flag == False):
                print('None acceptable words can be played by the computer')
                if self.checkEnd(s):
                    s.putbackletters(self)
                    self.letters = s.getletters()
                    turn = 0
                else:
                    print('There are not enough letters to change. The game is over')
                    turn = "quit"
            return turn
        # Πράξεις προγράμματος για mode "max". Όμοιο με το min αλλά οι λέξεις μεγαλύτερου μεγέθους αναζητούνται πρώτες.
        elif mode == 'max':
            wordLenght = 7
            while wordLenght > 2:
                permutations = []
                for permutation in it.permutations(lettersOnly, wordLenght):
                    permutations.append(permutation)
                for i in range(len(permutations)):
                    permutations[i] = ''.join(permutations[i])
                i = 0
                foundWord = self.isAcceptableWord(words, permutations)
                if len(foundWord) > 0:
                    for i in range(len(foundWord)):
                        points += s.letters[foundWord[i]][1]
                    print("The computer plays word ", foundWord, "and wins ", points, 'points!')
                    self.points += points
                    self.removeUsedLettersAndGiveNew(foundWord, s)
                    print(self)
                    turn = 0
                    break
                wordLenght -= 1
            if (flag == False):
                if self.checkEnd(s):
                    s.putbackletters(self)
                    self.letters = s.getletters()
                    turn = 0
                else:
                    print('There are not enough letters to change. The game is over')
                    turn = "quit"
            return turn
        # Πράξεις προγράμματος για το mode "smart". Εδώ υπάρχει διαφοροποίηση, καθώς αναζητούνται όλες οι έγκυρες λέξεις
        # που μπορούνα να σχηματιστούν και έπειτα επιλέγεται η πιο κερδοφόρα.
        elif mode == 'smart':
            wordLenght = 3
            # Αρχικοποίηση πινακα αποδεκτών λέξεων
            acceptableWords = []

            # Αναζήτηση έγκυρων λέξεων.
            while wordLenght < 8:
                permutations = []
                for permutation in it.permutations(lettersOnly, wordLenght):
                    permutations.append(permutation)
                for i in range(len(permutations)):
                    permutations[i] = ''.join(permutations[i])
                i = 0
                foundWord = self.isAcceptableWord(words, permutations)

                # Αν βρεθεί αποδεκτή λέξη αποθηκεύται για μετέπειτα αξιολόγηση.
                if len(foundWord) > 0:
                    acceptableWords.append(foundWord)
                    print(foundWord)
                wordLenght += 1
                foundWord = ''

            # Εφόσον έχει βρεθεί έστω και μία αποδεκτή λέξη
            if len(acceptableWords) > 0:
                # Βρίσκεται η πιο κερδοφόρα, υπολογίζονται οι νέοι πόντοι, ανανεώνονται τα γράμματα και αλλάζει η σειρά.
                wordAndPoints = self.findMostValueableWord(acceptableWords, s)
                print('Computer plays word: ', wordAndPoints[0], '. It wins ', wordAndPoints[1], 'points!')
                self.points += wordAndPoints[1]
                self.removeUsedLettersAndGiveNew(foundWord, s)
                turn = 0
            # Αν δεν έχει βρεθεί καμία αποδεκτή λέξη αλλάζουν τα γράμματα του υπολογιστή και η σειρά.
            elif len(acceptableWords) == 0:
                if self.checkEnd(s):
                    s.putbackletters(self)
                    self.letters = s.getletters()
                    turn = 0
                else:
                    print('There are not enough letters to change. The game is over')
                    turn = "quit"
            return turn

        return turn

    # Μέθοδος που εντοπίζει την πιο κερδοφόρα λέξη από ένα σύνολο αποδεκτών λέξεων (χρησιμοποιείται στην περίπτωση 'Smart')
    def findMostValueableWord(self, acceptableWords, s: SakClass):

        word = ''
        i = 0
        j = 0
        points = [0] * len(acceptableWords)

        # Πίνακας 2 θέσεων που στην πρώτη αποθηκεύεται η πιο κερδοφόρα λέξη και στην δεύτερη οι πόντοι που προσφέρει.
        wordAndPoints = [0] * 2

        for i in range(len(acceptableWords)):
            ith_word = acceptableWords[i]
            for j in range(len(ith_word)):
                points[i] += s.letters[ith_word[j]][1]

        wordAndPoints[0] = acceptableWords[points.index(max(points))]
        wordAndPoints[1] = max(points)

        i = 0
        # for i in range(len(acceptableWords)):
        # print(points[i])

        # Επιστρέφεται η πιο κερδοφόρα λέξη και οι πόντοι της
        return wordAndPoints


# Κλάση που αναπαριστά το παιχνίδι.
class Game:

    # Κατασκευαστής της κλάσης. Αρχικοποιεί το αντικείμενο.
    def __init__(self):
        pass

    # Μέθοδος που ετοιμάζει το παιχνίδι δίνοντας γράμματα στους παίκτες
    def setup(self, h: Human, c: Computer, s: SakClass):
        h.letters = s.getletters()
        c.letters = s.getletters()

    # Μέθοδος που βρίσκει τον νικητή, δίκει τα σχετικά αποτελέσματα και τα αποθηκεύει σε json format
    def end(self, h: Human, c: Computer, s: SakClass):

        filename = "data_js.json"
        winner = ''
        # Εύρεση του νικητή και εκτύπωση κατάλληλου μηνύματος
        if h.points > c.points:
            print(h.name + " is the winner with " + str(h.points) + " Congratulations!")
            winner = 'human'
        elif h.points < c.points:
            print(c.name + " is the winner with " + str(c.points) + " Congratulations!")
            winner = 'computer'
        elif h.points == c.points:
            print("The game is a tie! Both players had " + str(h.points) + " points. Congratulations!")
            winner = 'tie'

        # Διαδικασία αποθήκευσης αποτελεσμάτων σε json μορφή για πιθανή μελλοντική χρήση
        if winner == "human":
            data_set = [{"Player1": h.name, "Player2": c.name, "winner": h.name, "P1pts": h.points, "P2pts": c.points}]
            with open(filename, "r") as file:
                data = json.load(file)
            data.append(data_set)
            with open(filename, "w") as file:
                json.dump(data, file)
        elif winner == "computer":
            data_set = [{"Player1": h.name, "Player2": c.name, "winner": c.name, "P1pts": h.points, "P2pts": c.points}]
            with open(filename, "r") as file:
                data = json.load(file)
            data.append(data_set)
            with open(filename, "w") as file:
                json.dump(data, file)
        elif winner == "tie":
            data_set = [{"Player1": h.name, "Player2": c.name, "winner": "Tie", "P1pts": h.points, "P2pts": c.points}]
            with open(filename, "r") as file:
                data = json.load(file)
            data.append(data_set)
            with open(filename, "w") as file:
                json.dump(data, file)