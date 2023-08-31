class MatrixCharacter:
    """
    make a decision on what pill to take
    upon red pill wake up
    receive training
    enter Matrix                 0=asleep 1-awake
    exit Matrix
    do while
    """
    
    def __init__(self, name):
        self.name = name
        self.fighting_styles = fighting_styles
        self.awake = False
        self.trained = False
        self.location = 1
        
    def driver(self):
        while self.awake:
            if not self.trained:
                self.receive_training()
            while True:
                user_training = input("Do you need additonal training? [y]/[n]")
                if user_training = "y":
                    self.addtional_training
            self.additonal.training()    
            self.update_location()
            self.pill_decision()
            
    def pill_decision(self):
        pill = input('[Red] pill to go down the rabbit hole or [Blue] pill to stay where you are? ')

        else:
            print('Phone ringing')
            self.location = 0
            
#         print(self.location)
        
        
# matrix_character.update.location()    
matrix_character = MatrixCharacter('Neo', ['boxing', 'wrestling'])

# matrix_character.receive_training()

matrix.character.driver()
        if pill == 'red':
            self.awake = True
        else:
            self.awake = False
            
    def revieve_training(self):
        self.fighting_styles += ['kung fu', 'taekwondo','aikido','drunken monk']
        print(f'you now know {" ".join(self.fighting_styles)}')
    
    def additional_training(self, fighting_style):
        self.fighting_styles.append(fighting_style)
        self.display_fighting_style()
        
    def update_location(self):
        if not self.location:
            input('Agents attacking, are you ready to enter the Matrix? [y]es/[n]o: ').lower()
            if user_ready == "y"
            print('Plugging into the Matrix')
            self.location = 1