import random
import time
import sys

CHOIX_POSSIBLES = ("pierre", "feuille", "ciseau")

REGLES_GAIN = {
    "pierre": "ciseau",
    "feuille": "pierre",
    "ciseau": "feuille"
}

RESET = "\033[0m"
RED = "\033[31m"
BLACK = "\033[30m"
BLUE = "\033[34m"
WEB = "🕸️"
SPIDER = "🕷️"
FAT_TEXT = "\033[1m"
YELLOW = "\033[33m"

def write_machine(text: str, play_time: float):
    """ write machine for write any text you want
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(play_time)
    print('\n')

def computer() -> str:
    """ Get previews movement for predict new
    """
    return random.choice(CHOIX_POSSIBLES)


def interface_game():
    """ Interface for game
    """
    print(
        f"""{BLUE}
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│          WELCOME TO ROCK PAPER SCISSOR VEERRSSUUUUUUUUUUUUUUUUSSSSSS                           {WEB}  │
│                                                                                                   │
│{RED}     d888888o.   {BLUE}8 888888888o    {RED}8 8888 8 {BLUE}888888888o.      {RED}8 8888888888 {BLUE}`8.`8888.      ,8'         │
│{RED}   .`8888:' `88. {BLUE}8 8888    `88.  {RED}8 8888 8 {BLUE}8888    `^888.   {RED}8 8888       {BLUE} `8.`8888.    ,8'          │
│{RED}   8.`8888.   Y8 {BLUE}8 8888     `88  {RED}8 8888 8 {BLUE}8888        `88. {RED}8 8888       {BLUE}  `8.`8888.  ,8'           │
│{RED}   `8.`8888.     {BLUE}8 8888     ,88  {RED}8 8888 8 {BLUE}8888         `88 {RED}8 8888        {BLUE}  `8.`8888.,8'            │
│{RED}    `8.`8888.    {BLUE}8 8888.   ,88'  {RED}8 8888 8 {BLUE}8888          88 {RED}8 888888888888 {BLUE}  `8.`88888'             │
│{RED}     `8.`8888.   {BLUE}8 888888888P'   {RED}8 8888 8 {BLUE}8888          88 {RED}8 8888         {BLUE}   `8. 8888              │
│{RED}      `8.`8888.  {BLUE}8 8888          {RED}8 8888 8 {BLUE}8888         ,88 {RED}8 8888        {BLUE}     `8 8888              │
│{RED}  8b   `8.`8888. {BLUE}8 8888          {RED}8 8888 8 {BLUE}8888        ,88' {RED}8 8888        {BLUE}      8 8888              │
│{RED}  `8b.  ;8.`8888 {BLUE}8 8888          {RED}8 8888 8 {BLUE}8888    ,o88P'   {RED}8 8888        {BLUE}      8 8888              │
│{RED}   `Y8888P ,88P' {BLUE}8 8888          {RED}8 8888 8 {BLUE}888888888P'      {RED}8 888888888888{BLUE}      8 8888              │
│                                                                                                   │
│           ────────────────────────────────────────────────────────                                │
│   {RED}Rules :                                   {BLUE}                                                      │
│   {RED}   - write => {FAT_TEXT+BLUE}rock{RESET+RED} / {FAT_TEXT+BLUE}paper{RESET+RED} / {FAT_TEXT+BLUE}scissor{RESET}      {BLUE}                                                      │
│   {RED}   - if you want to stop the game => {FAT_TEXT+BLUE}/stop{RESET+BLUE}                                                      │
│                                                                                                   │
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
{RESET}
"""
    )
    write_machine(f"Are You Ready for Game ???? {SPIDER}", 0.1)

def game(score: dict, preview_user: list, preview_ia: list) -> bool:
    """ Launch game between computer and gamer

        Arg:
            score: dict
            preview_user: list
            preview_ia: list
        Return:
            next_moov: str
    """
    print(f"Your turn : ")    
    # user_choose = input()
    user_choose= ""
    while user_choose not in CHOIX_POSSIBLES:
        print(f"\n=== SCORE ACTUEL : Humain({score['humain']}) - Spidey({score['spidey']}) ===")
        user_choose = input().lower()

        if user_choose == "/stop":
            print('ENDGAME')
            return False
    
        if user_choose not in CHOIX_POSSIBLES:
            print(f"{YELLOW}Warning: Wrong value, retry with rock, paper or scissor{RESET}")
            print(f"Your value {user_choose}")
            print(CHOIX_POSSIBLES)
        else: 
            break
    
    computer_choose = computer()   

    preview_user.append(user_choose)
    preview_ia.append(computer_choose)

    if user_choose == computer_choose:
        result = "Draw"
    elif REGLES_GAIN[user_choose] == computer_choose:
        result = f"{BLUE}You WWIIIINNNN !!!!!{RESET}"
        score['humain'] += 1
    else:
        result = f"{RED}You Looose...  Spidey is better{RESET}"
        score['spidey'] += 1
    
    print(f"Résultat : {result}")

    return True
  
