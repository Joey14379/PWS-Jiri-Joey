
###IMPORTS###
import customtkinter as ctk
import random

###VARIABELEN###
global standaardlijst
standaardlijst = {
    'Een':'One',
    'Twee':'Two',
    'Drie':'Three',
    'Vier':'Four',
    'Vijf':'Five',
    'Zes':'Six',
    'Zeven':'Seven',
    'Acht':'Eight',
    'Negen':'Nine',
    'Tien':'Ten',
    'Elf':'Eleven',
    'Twaalf':'Twelve',
    'Dertien':'Thirteen',
    'Veertien':'Fourteen',
    'Vijftien':'Fifteen',
    'Zestien':'Sixteen',
    'Zeventien':'Seventeen',
    'Achttien':'Eighteen',
    'Negentien':'Nineteen',
    'Twintig':'Twenty',
}

###FUNCTIES###

# Deze functie draagt de gebruiker het prompt voor, en controleert of het inguvelde antwoord overeenkomt
# met de betekenis die als value is ingevuld bij de bijbehorende key in de achtieve termenlijst.
def promptvoordracht_en_controle():
    # Deze line geeft een prompt door een random key te kiezen uit een lijst met keys van de termenlijst
    prompt = random.choice(list(termenlijst.keys()))
    print("Wat is de vertaling van: ",prompt)
    antwoord = input()
    # Deze line checkt of het opgegeven antwoord overeenkomt met het antwoord (value) 
    # die gekoppeld staat aan het prompt in de termenlijst 
    if antwoord == termenlijst[prompt]:
        print('Correct')
    else:
        print('Incorrect')


def main():
    global termenlijst
    termenlijst = standaardlijst
    promptvoordracht_en_controle()

main()