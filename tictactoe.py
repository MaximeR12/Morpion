l= [ [' ',' ',' '] , [' ',' ',' '] , [' ',' ',' '] ]

def reset_plateau():
    """_summary_ : reset the list that contains all the ' '/'X'/'O'/
    """
    for i in range(3):
        for j in range(3):
            l[i][j]=' '



def afficher_plateau_v2():
    """_summary_ : print the list content with grid
    """
    print(f'   {l[0][0]} | {l[0][1]} | {l[0][2]} ')
    print('  -----------')
    print(f'   {l[1][0]} | {l[1][1]} | {l[1][2]} ')
    print('  -----------')
    print(f'   {l[2][0]} | {l[2][1]} | {l[2][2]} ')
    print('\n')




def placer(joueur):
    """_summary_ : print "joueur X, à vous", ask the user to chose a case and modifies what's inside this case  

    Args:
        joueur (int): count for numbers of play %2+1 to get 1/2
    """
    print('\nJoueur ',joueur % 2 + 1,' à vous :\n')

    afficher_plateau_v2()

    if joueur %2 == 1:
        signe = 'X'
    elif joueur %2 == 0:
        signe = 'O'

    position_user=input('dans quelle case souhaitez vous mettre votre signe ? (pavé numerique) :')
    if not (position_user in ['1','2','3','4','5','6','7','8','9']):
        print('veuillez entrer une case valide (entre 1 et 9)')
        placer(joueur)

    else:
        intpose= int(position_user)
        ligne = 2 - (intpose-1)//3
        colonne = (intpose % 3) - 1
    
        if l[ligne][colonne]==' ':
            l[ligne][colonne]=signe
        
        else:
            print('Veuillez choisir une autre case')



def victoire_colonne(colonne):
    """_summary_ : checks if there is 3 same signs in a row

    Args:
        colonne (int): enter the row to check

    Returns:
        bool : True if there is 3 in a row, else False
    """
    return l[0][colonne]==l[1][colonne]==l[2][colonne]!=' '
        
def victoire_ligne():
    """checks if there is 3 same signs in a line

    Returns:
        bool: True if 3 signs are the same, else False
    """
    for i in l:
        if i[0]==i[1]==i[2]!=' ':
            return True

def victoire_diagonale():
    """check the diagonals

    Returns:
        bool: True is 3 same signs in diagonal, else False
    """
    verif1=l[0][0]==l[1][1]==l[2][2]!=' '
    verif2=l[2][0]==l[1][1]==l[0][2]!=' '
    return verif1 or verif2
            
def victoire(joueur):
    """check if on of the victoire_... function return True

    Returns:
        bool: True if victory or draw, False if game can continue
    """
    if victoire_diagonale():
        return True
    for i in range(3):
        if victoire_ligne() or victoire_colonne(i):
            print('victoire du joueur ',joueur % 2 + 1,' !')
            return True
    if joueur>=10:
        print ('Match nul, reessayez\n')
        return True
    else:
        return False


def main():
    joueur=1
    while not victoire(joueur):
        joueur+=1
        placer(joueur)
    afficher_plateau_v2()
    if input('Souhaitez vous rejouer ? ')in 'OuiouiOUI':
        reset_plateau()
        main()

print("\nBonjour ! Bienvenue dans le morpion, jouez à l'aide des chiffres de votre clavier")
main()