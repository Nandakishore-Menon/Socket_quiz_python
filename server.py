import socket
import select
import threading
import _thread
import sys
import time
import random
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = socket.gethostbyname("")
Port = 9999
server.bind((IP, Port))
server.listen(100)
client_addr=[]
clients=[]

Q = [" What is the Iron man's real name?\n a.Tony pork   b.Pony clark   c.Stony lark   d.Tony Stark\n",
     " How did Jake Peralta want his wedding to be like?\n a.fancy   b.expensive   c.cool cool cool   d.Toit nups\n",
     " How many infinity stones were there?\n a.5   b.4   c.6   d.7\n",
     " Who is the Thor's father?\n a.Heimdall   b.Loki   c.Odin   d.Tony Stark\n",
     " How many horcruxes did Lord Voldemort make?\n a.1   b.7   c.3   d.11\n",
     " What is Captain America's shield made of?\n a.Vibranium   b.Adamandium   c.Titanium   d.Ambuja Cement\n",
     " How many cameras does Galaxy S10 plus have in total?\n a.2   b.3   c.4   d.5\n",
     " How many states are there in India?\n a.29   b.28   c.30   d.31\n",
     " Which mythology features Thor?\n a.Greek   b.Indian   c.Eqyptian   d.Norse\n",
     " Who is Loki?\n a.God of Thunder   b.God of Dwarves   c.God of Mischief   d.God of Gods\n",
     " Who is Indian PM?\n a.Marendra Nodi   b.Gajendra Lodi   c.Ramprakash   d.Narendra Modi\n",
     " Who was one of the founders Apple Inc?\n a.Steve Jobs   b.Adam and Eve   c.Stane Jobless   d.KRK\n",
     " Who is Holt's arch nemesis?\n a.Melissa Lunch   b.Madeline Wuntch   c.Jake Peralta   d.Norm Scully\n",
     " Who composed the Avengers theme song?\n a.Alan Silvestri   b.John Powell   c.Utkarsh Heerawala   d.Prabhu Nidhish\n",
     " Who directed Avengers: Endgame?\n a.Russian brothers   b.Houdini brothers   c.Russo brothers   d.Stan Lee\n",
     " Who plays the role of Deadpool?\n a.Nicolas Cage   b.Hugh Jackman   c.Ryan Reynolds   d.Robert Downey\n",
     " What is Wolverine's claws composed of?\n a.Vibranium   b.Adamandium   c.Titanium   d.Ambuja Cement\n",
     " Who is Jake Peralta's criminal friend?\n a.Trudy Judy   b.Frank Judy   c.Doug Judy   d.Charles Boyle\n",
     " What cars does Doug Judy steal?\n a.Pontiacs   b.Maruti   c.Ford   d.Mahindra\n",
     " In which precint does Rosa Diaz work in?\n a.99   b.69   c.86   d.107\n",
     " Which pokemon does Ryan Reynolds voice in a particular Pokemon movie?\n a.Charmander   b.Squirtle   c.Pikachu   d.Bulbazor\n",
     " What is Lord Voldemort's real name?\n a.Tin-Tin   b.Tom Riddle   c.Tom Puzzle   d.Crossword Tom\n",
     " Which movie is Jake Peralta obsessed with?\n a.Pulp fiction   b.Die Hard   c.Inception   d.Ghost Rider\n",
     " Who was Harry Potter's godfather?\n a.Sirius Black   b.Sirius White   c.Silly Black   d.Silly White\n",
     " Who plays Batman in The Dark Knight?\n a.Hindu Whale   b.Muslim Gayle   c.Christian Bale   d.Jewish Pale\n",
     " Which is the longest river on Earth?\n a.Amazon   b.Brahmaputra   c.Mississippi   d.Nile\n",
     " How many bones does an adult human have?\n a.207   b.206   c.208   d.205\n",
     " Which country is called the land of rising sun?\n a.Russia   b.India   c.Japan   d.China\n",
     " Which day is observed as World Environment Day?\n a.June 5   b.March 20   c.June 22   d.May 11\n",
     " How many days are there in a week?\n a.5   b.8   c.7   d.9\n",
     " Who is the author of the Harry Potter series of books?\n a.Agatha Christie   b.Harper Lee   c.Rick Riordan   d.J.K.Rowling\n",
     " Which is the longest bone in the human adult body?\n a.Femur   b.Stapes   c.Ulna   d.Sternum\n",
     " Which invented electricity?\n a.Benjamin Franklin   b.Thomas Edison   c.John Baird   d.James Watt\n",
     " Who is Thor?\n a.God of Nature   b.God of Thunder   c.God of Mischief   d.God of Death\n",
     " Who plays the role of Iron Man in the MCU?\n a.Robert Downey Jr.   b.Chris Evans   c.Tom Cruise   d.George Clooney\n",
     " What is a group of lions called?\n a.A school   b.A brood   c.A pride   d.A flock\n",
     " What is the name of Harry Potter's pet owl?\n a.Fluffy   b.Hedwig   c.Scabbers   d.Crookshanks\n",
     " How many consonants are there in the English alphabet?\n a.26   b.22   c.24   d.21\n",
     " Who painted the Mona Lisa?\n a.Rembrandt   b.Leonardo Da Vinci   c.Pablo Picasso   d.Raphael\n",
     " Which is the highest mountain on Earth?\n a.Kangchenjunga   b.Nanda Devi   c.Mt.Everest   d.K2\n",
     " Which city is the Statue of Liberty in?\n a.New York   b.Washington   c.Chicago   d.San Francisco\n",
     " Who wrote Hamlet and Macbeth?\n a.Mark Twain   b.Jane Austen   c.T.S.Eliot   d.William Shakespeare\n",
     " Which element does Fe represent?\n a.Sodium   b.Aluminium   c.Iron   d.Copper\n",
     " 5 + 6 = \n a.14   b.11   c.13   d.10\n",
     " Which infinity stone was in the Tesseract?\n a.Mind   b.Time   c.Space   d.Power\n",
     " 30 + 11 = \n a.41   b.69   c.59   d.51\n",
     " Which of the following is not a primary colour?\n a.Red   b.Blue   c.Yellow   d.Black\n",
     " Which is the longest grass?\n a.Palak   b.Pudhina   c.Bamboo   d.Dhaniya\n",
     " What is the full-form of SSD?\n a.Solid state drive   b.Solid storage drive   c.Super state drive   d.Super storage drive\n",
     " Who is the author of Marvel comics?\n a.Bruce Lee   b.Stan Lee   c.Harper Lee   d.Cooper Lee\n"]

A = ['d', 'd', 'c', 'c', 'b', 'a', 'd', 'b', 'd', 'c', 'd', 'a', 'b', 'a', 'c', 'c', 'b','c','a','a','c','b','b','a','c','d', 'b', 'c', 'a', 'c', 'd', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'b', 'c', 'a', 'd', 'c', 'b', 'c', 'a', 'd', 'c', 'a', 'b']



score=[0,0,0]
def broadcast(message):
    for client in clients:
        try:
            client.send(str.encode(message))
        except:
            pass



def next_question():
    current_question = random.randint(0,10000)%len(Q)
    if len(Q) != 0:
        broadcast(Q[current_question])
    else:
        broadcast("\n\n\t\t\tGAME OVER! NO WINNERS")
        time.sleep(2)
        broadcast("~exit~")
        time.sleep(1)
        server.close()
        sys.exit()


player=0
current_question=[0]

def parallel():
    dummy=[]
   
    while True:
        next_question()
        read_sockets,write_socket, error_socket = select.select(clients,[],clients,10)
        if not read_sockets:
            broadcast("\n\t\t\tNobody pressed the buzzer.....The Next Question is...\n")
            Q.pop(current_question[0])
            A.pop(current_question[0])
            continue
        else:
            buzzer=str(read_sockets[0].recv(2048),'utf-8')
            dummy=[read_sockets[0]]
            broadcast("\n\t\t\tPlayer"+str(clients.index(read_sockets[0])+1)+" pressed the buzzer first \n")
            read_sockets[0].send(str.encode("\n\t\t\tPlease answer within 10 seconds....\n"))
            read_sockets1,write_socket1, error_socket1 = select.select(dummy,[],dummy,10)
            if not read_sockets1:
                read_sockets2,write_socket2, error_socket2 = select.select(clients,[],clients,0.5)
                if not read_sockets2:
                    broadcast("\n\t\t\tPlayer"+str(clients.index(read_sockets[0])+1)+" didnt answer.\n\t\t\tThe Next Question is.......\n\n")
                    continue
                else:
                    for x in read_sockets2:
                        message2=str(x.recv(2048),'utf-8')
                continue
            message=str(dummy[0].recv(2048),'utf-8')
            if message[0]==A[current_question[0]][0]:
                broadcast("\n\t\t\tPlayer " + str(clients.index(read_sockets[0])+1) + " gets 1 point!" + "\n\t\t\tThe Next question is.....\n\n")
                
                score[clients.index(read_sockets[0])]+=1
                if max(score)>=5:
                    #time.sleep(1)
                    #broadcast(str.encode("Player" + str(score.index(max(score))+1) + " WON!!!!" + "\n"))
                    #time.sleep(1)
                    gameover()
                    #break
            else:
                broadcast("\n\t\t\tPlayer " + str(clients.index(read_sockets[0])+1) + " loses 0.5" + "\n")
                score[clients.index(read_sockets[0])] -= 0.5
            read_sockets2,write_socket2, error_socket2 = select.select(clients,[],clients,0.5)
            Q.pop(current_question[0])
            A.pop(current_question[0])
            if not read_sockets2:
                continue
            else:
                for x in read_sockets2:
                    message2=str(x.recv(2048),'utf-8')


def next_question():
    current_question[0] = random.randint(0,10000)%len(Q)
    if len(Q) != 0:
        broadcast(Q[current_question[0]])
    #parallel()
        
def gameover():
    player_id = score.index(max(score))
    for i in range(0,3):
        clients[i].send(str.encode("\t\t\tGAME OVER!\n\n\t\t\tPlayer "+str(player_id+1)+" wins!!\n\n"+"\t\t\tYour score :" + str(score[i]) + " points.\n\n"))
    time.sleep(2)
    broadcast("~exit~")
    time.sleep(1)
    server.close()
    sys.exit()

def quiz():
    broadcast("\t\t\tHey there QuizMaster!\n\t\t\tWelcome to the Quiz!!!\n\t\t\tFirst person to score 5 points wins\n\t\t\tOne correct answer gets 1 point and a wrong answer gets -0.5 points\n")
    broadcast("\t\t\tWithin ten seconds of getting the question,press the buzzer.USE ENTER AS THE BUZZER\n\t\t\tYou'll have 10 seconds to answer the question.\n\t\t\tANSWER THE QUESTION BY PRESSING THE OPTION CHARACTER IN LOWER CASE AND PRESSING ENTER KEY\n\t\t\tTHERE WILL BE NO PASSED QUESTIONS\n\n\t\t\tTHE QUIZ STARTS IN 10 seconds\n")
    for i in range(10,1,-1):
        broadcast("\t\t"+str(i))
        time.sleep(1)
    parallel()

def main():
    while True:
        try:
            conn, addr = server.accept()
            clients.append(conn)
            client_addr.append(addr)
            print(addr[0] + " connected")
            #_thread.start_new_thread(parallel,(conn,addr))
            if(len(clients)==3):
                quiz()
            if len(clients)!=3:
                conn.send(str.encode("\t\t\tWaiting for players to join.....\n"))
                #next_question()
        except:
            time.sleep(2)
            broadcast("~exit~")
            time.sleep(1)
            server.close()
            sys.exit()
            pass
#server.close()
    
    
    
main()

