from classes import*


# Μέθοδος παροχής βοήθειας. Θα εμφανίζει τις οδηγίες και θα περιγράφει την υλοποίηση του project.
def guidelines():
    '''
        Scrabble project - Κιζιρίδης Κωνσταντίνος 3566

        Περιβάλλον Ανάπτυξης: To project αναπτύχθηκε στο προγραμματιστικό περιβάλλον "Jupyter Notebook".

        Βιβλιοθήκες:

            Για την υλοποίηση του project χρησιμοποιήθηκαν οι παρακάτω βιβλιοθήκες της Python:
        - math, random : Για την υλοποίση λειτουργιών για το σακουλάκι
        - itertools: Για την εύρεση των συνδυασμών γραμμάτων του υπολογιστή
        - json: Για την αποθήκευση δεδομένων εκτέλεσης του προγράμματος σε log file.

        Κλάσεις:

        Κλάση SakClass: Η κλάση αυτή αναπαριστά το σακουλάκι γραμμάτων του παιχνιδιού. Περιέχει τις παρακάτω μεθόδους.
        Μέθοδος __init__() : Κατασκευαστής της κλάσης. Αρχικοποιεί κατάλληλα τα δεδομένα ενός αντικειμένου της κλάσης.
                             Δηλαδή, τα γράμματά του και τον αρχικό αριθμό γραμμάτων
        Μέθοδος __repr__() : Υπερφόρτωση της μεθόδου repr για να εμφανίζει πιο κατάλληλα δεδομένα για την κλάση
        Μέθοδος __str__()  : Υπερφότωση της μεθόδου str για να εμφανίζει πιο κατάλληλα δεδομένα για την κλάση
        Μέθοδος getLetters : Η μέθοδος αυτή χρησιμοποιείται για τυχαία λήψη 7 γραμμάτων, τα οποία δίνονται στους παίκτες
                             του παιχνιδιού
        Μέθοδος putBackLetters: Η μέθοδος αυτή χρησιμοποιείται για να τοποθετηθούν πίσω τα γράμματα των παικτών αν αυτοί
                                επιλέξουν "πάσο"
        Μέθοδος replenishLetters: Η μέθοδος αυτή συμπληρώνει τα απαραίτητα γράμματα στους παίκτες αφού αυτοί χρησιμοποιή-
                                  σουν κάποια απ' τα διαθέσιμά τους για να παίξουν κάποια λέξη.


        Κλάση Game: Η κλάση αυτή αναπαριστά το ίδιο το παιχνίδι. Δεν έχει ιδιαίτερη λειτουργικότητα πέρα από την αρχικοποίηση
                    του παιχνιδιού και την ανακοίνωση - αποθήκευση των αποτελεσμάτων.
        Μέθοδος __init__(): Κατασκευαστής της κλάσης. Φτιάχνει απλά ένα κενό αντικείμενο.
        Μέθοδος setup: Η μέθοδος αυτή αρχικοποιεί τα γράμματα των παικτών
        Μέθοδος end: Η μέθοδος αυτή χρησιμοποιείται όταν πρόκειται να λήξει το παιχνίδι. Χρησιμοποιείται για την εύρεση του
                     νικητή, την ανακοίνωση των αποτελεσμάτων στους παίκτες και τέλος στο να αποθηκεύσει τις κατάλληλες
                     πληροφορίες του παιχνιδιού σε json log file, για ενδεχόμενη μελλοντική χρήση/λειτουργικότητα, όπως
                     πίνακας highscore.


        Κλάση Player: Η κλάση αυτή αναπαριστά τους παίκτες. Αποτελεί γενική κλάση απ' την οποία κληρονομούν στοιχεία
                      οι κλάσεις Human(Παίκτης-Άνθρωπος) και Computer(Παίκτης-Υπολογιστής)
        Μέθοδος __init__(): Κατασκευαστής της κλάσης. Αρχικοποιεί το όνομα, τους πόντους και τα γράμματα του παίκτη.
                            Η μέθοδος κληρονομείται και απ την κλάση Human
        Μέθοδος __repr__(): Υπερφόρτωση της μεθόδου repr για να εμφανίζει πιο κατάλληλα δεδομένα για την κλάση
        Μέθοδος __srt__(): Υπερφότωση της μεθόδου str για να εμφανίζει πιο κατάλληλα δεδομένα για την κλάση
        Μέθοδος canFormWord(): Μέθοδος που ελέγχει εάν η λέξη που επιλέγει ο παίκτης να παίξει μπορεί να σχηματιστεί από
                               τα διαθέσιμα γράμματα που έχει.
        Μέθοδος isAcceptableWord(): Μέθοδος που ελέγχει εάν μία δοθείσα λέξη βρίσκεται στις αποδεκτές λέξεις.
        Μέθοδος removeUsedWordsAndGiveNew(): Μέθοδος, η οποία χρησιμοποιείται εφόσον βρεθεί ο παίκτης παίξει αποδεκτή λέξη
                                             και πρέπει να αναπληρώσει τα γράμματά του. Συνεργάζεται με την μέθοδο
                                             replenishLetters της κλάσης SakClass.
        Μέθοδος play(): Μέθοδος, η οποία αναπαριστά τις συνθήκες του γύρου για τον παίκτη. Δηλαδή επιλέγεται αν θα πάει πάσο,
                        αν θα παίξει και εφόσον παίξει αν θα δώσει σωστή λέξη κ.τ.λ. Ακόμη, μέσω αυτής ελέγχεται αν ισχύουν
                        συνθήκες τερματισμού του παιχνιδιού, όπως η ανεπάρκεια γραμμάτων στο σακουλάκι.
        Μέθοδος wantToQuit(): Η μέθοδος αυτή χρησιμοποιείται για να ελέγξει την επιθυμία του παίκτη για το τι θέλει να κάνει αν
                              δεν βρίσκει σωστή λέξη, π.χ. να πάει πάσο, να τερματίσει το παιχνίδι ή να ξαναπροσπαθήσει να
                              δώσει σωστή λέξη με τα υπάρχοντα γράμματα που έχει. Η μέθοδος αυτή χρησιμοποιείται μόνο στην περί-
                              πτωση του παίκτη-ανθρώπου, καθώς οι ενέργειες αυτές στον υπολογιστή είναι καθορισμένες μέσα στην
                              δική του μέθοδο play.


        Κλάση Human:  Κλάση που αναπαριστά τον παίκτη - άνθρωπο. Ο,τι χρησιμοποιεί το κληρονομεί απευθείας
                      απ' την κλάση  Player.


        Κλάση Computer: Κλάση που αναπαριστά τον παίκτη - υπολογιστή.
        Μέθοδος __init__(): Η κλάση Χρησιμοποιεί δικό της κατασκευαστή, καθώς έχει fixed όνομα "Computer"
        Μέθοδος isAcceptableWord(): Επέκταση της μεθόδους της κλάσης Player. Αυτό γίνεται καθώς ο υπολογιστής δεν δίνει μία
                                    λέξη και ψάχνει να δει αν είναι έγκυρη, αλλά ψάχνει για έγκυρη λέξη σε ένα σύνολο από
                                    permutations.
        Μέθοδος play(): Επέκταση της μεθόδου της κλάσης Player, καθώς η διαδικασία της γύρας του υπολογιστή είναι διαφορετική
                        απ' αυτήν του παίκτη. Ο υπολογιστής παίζει με βάση τον αλγόριθμο "min-max-smart" που περιγράφεται στην
                        εκφώνηση.
        Μέθοδος findMostValuableWord(): Μέθοδος που υπάρχει μόνο σ' αυτήν την κλάση. Ψάχνει να βρει την πιο κερδοφόρα λέξη
                                        σε ένα σύνολο έγκυρων λέξεων. Χρησιμοποιείται στην λογική παιχνιδιού "smart"
        Η κλάση Computer κληρονομεί και χρησιμοποιεί απ' την κλάση Player τα παρακάτω: __init__(), __repr__(), __str__(),
                                                                                       removeUsedWordsAndGiveNew().

        Συμπληρωματικές συναρτήσεις:

        Function - readfile(): Συνάρτηση που χρησιμοποιείται για να διαβάσει το αρχείο με τις αποδεκτές λέξεις
                               και να το μορφοποιήσει κατάλληλα για χρήση στο πρόγραμμα.
        Function - chechEndConditions(): Συνάρτηση που χρησιμοποιείται για να ελέγξει την επάρκεια γραμμάτων στο σακουλάκι
                                         ώστε να δει αν χρειάζεται να τερματιστεί το παιχνίδι.
        Function - initialize_letters(): Συνάρτηση που φτιάχνει τα την λίστα γραμμάτων και της αξίας τους για να φτιαχτεί το
                                         σακουλάκι
        Function - guidelines(): Συνάρτηση που περιέχει dockstring με το documentation του προγράμματος.
        Function - main(): Συνάρτηση - οδηγός που τρέχει το πρόγραμμα.

    '''


# Μέθοδος που αρχικοποιεί τα γράμματα για το σακουλάκι
def initialize_letters():
    letters = {
        "Α": [12, 1],
        "Β": [1, 3],
        "Γ": [2, 4],
        "Δ": [2, 4],
        "Ε": [8, 1],
        "Ζ": [1, 10],
        "Η": [7, 1],
        "Θ": [1, 10],
        "Ι": [8, 1],
        "Κ": [4, 2],
        "Λ": [3, 3],
        "Μ": [3, 3],
        "Ν": [6, 1],
        "Ξ": [1, 10],
        "Ο": [9, 1],
        "Π": [4, 2],
        "Ρ": [5, 2],
        "Σ": [7, 1],
        "Τ": [8, 1],
        "Υ": [4, 2],
        "Φ": [1, 8],
        "Χ": [1, 8],
        "Ψ": [1, 10],
        "Ω": [3, 3],
    }

    return letters


# Μέθοδος η οποία διαβάζει το αρχείο των αποδεκτών λέξεων χρησιμοποιώντας το κατάλληλο encoding
# και κάνοντας την κατάλληλη μορφοποίηση.
def readfile():
    # Άνοιγμα του αρχείου
    file = open("greek7.txt", encoding="utf8")
    # Διάβασμά του γραμμή - γραμμή
    words = file.readlines()
    # Αφαίρεση του χαρακτήρα αλλαγής γραμμής.
    i = 0
    for i in range(len(words)):
        words[i] = words[i].strip('\n')
    return words


# Συνάρτηση που ελέγχει συνθήκες τερματισμού για το σακουλάκι στο κυρίως πρόγραμμα.
def checkEndConditions(s: SakClass):
    if len(s.letters) < 7:
        return True
    else:
        return False


# Συνάρτηση main. Η συνάρτηση-οδηγός του προγράμματος.
def main():
    # Αρχικοποίηση για το σακουλάκι.
    letters = initialize_letters()
    sakoulaki = SakClass(letters)

    # Αρχικοποίηση του παιχνιδιού
    game = Game()
    name = input("Insert your name: ")
    human = Human(name)
    computer = Computer()
    game.setup(human, computer, sakoulaki)

    # Initializing the acceptable words for the game
    words = readfile()
    mode = 'min'
    print("WELCOME TO SCRABBLE GAME!")
    print("Default computer mode is 'min'. If you want to change it go to options. Else start playing!")
    print("If you want to read the documentation type 'help'. Else type 'c' for continue: ")
    documentation = input()
    if documentation.lower() == "help":
        print(guidelines.__doc__)
    else:
        pass

    choice = input("Type 'p' for play or 'o' for options: ")
    if choice.lower() == 'o':
        print('Choose game mode "min, max or smart: "')
        mode = input().lower()
        print("Computer mode set to " + mode)

    turn = 0
    print(human)
    while True:
        if checkEndConditions(sakoulaki):
            break
        if turn == 0:
            turn = human.play(sakoulaki, turn, words)
        elif turn == 1:
            turn = computer.play(sakoulaki, mode, words, turn)
        elif turn == "quit":
            break

    game.end(human, computer, sakoulaki)


if __name__ == "__main__":
    main()