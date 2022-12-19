from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from tempfile import mkdtemp
import math

app = Flask(__name__) 

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/") #函式的裝飾（Decorator) 以函式為基礎，提供附加的功能
def index():
    return render_template("index.html")

 
@app.route("/game")
def game():
    if "board" not in session:
        session["board"] = [[None, None, None],
                             [None, None, None], 
                             [None, None, None]]
        session["turn"] = "X"
    ans = CheckWinner(session["board"])

    if(ans[0] == True):
        return render_template("finish.html",ans="{} Player is Won!".format(ans[1]))
    elif(ans[0] == False and ans[1] == "Draw"):
        return render_template("finish.html",ans="Its a Draw!")
    else:
        return render_template("game.html",game=session["board"],turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "O"
    else:
        session["turn"] = "X"
    return redirect(url_for("game"))

@app.route("/clear") 
def clear():
    session["board"] = [[None,None,None],
                        [None,None, None],
                        [None,None, None]]
    session["turn"] = "X"
    return redirect(url_for("game"))

def CheckWinner(board): # [x,y] for x iff game is finished with winner and y = "Draw" if the game is draw, else, the winner (["Alice","Y"])
    # Checking the rows..
    for i in range(3):
        for j in range(3):
            if(board[i][0] == None):
                break
            if(board[i][0] == board[i][1] and board[i][1] == board[i][2]):
                return [True, board[i][0]]

    # Checking the columns..
    for i in range(3):
        for j in range(3):
            if(board[0][i] == None):
                break
            if(board[0][i] == board[1][i] and board[1][i] == board[2][i]):
                return [True, board[0][i]]

    # Checking the diagonals..
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
         if(board[0][0] != None):
             return [True, board[0][0]]

     # Checking the diagonals..
    if(board[2][0] == board[1][1] and board[1][1] == board[0][2]):
         if(board[1][1] != None):
             return [True, board[1][1]]

    for i in range(3):
        for j in range(3):
            if(board[i][j] == None):
                return [False, board[0][0]]  # Its Return somthing, never mind[1].

    # Its Draw!
    return [False, "Draw"]


# def minimax(board,turn):
#     ans = CheckWinner(board)
#     if(ans[0] == True and ans[1] == "X"):
#         return (1,None)
#     elif(ans[0] == True and ans[1] == "O"):
#         return (-1,None)
#     elif(ans[0] == False and ans[1] == "Draw"):
#         return (0,None)
#     else: # Next Step of Recursion
#         moves = []
#         for i in range(3):
#             for j in range(3):
#                 if(board[i][j] == None):
#                     moves.append((i,j))
#         # All Moves that avaliabe are now at moves
#         if turn == "X":
#             value = -2
#             for i,j in moves:
#                 board[i][j] = "X"
#                 result = minimax(board,"O")[0]
#                 if(value < result):
#                     value = result
#                     step = (i,j)
#                 board[i][j] = None
#         elif turn == "O": # turn is "O"
#             value = 2
#             for i,j in moves:
#                 board[i][j] = "O"
#                 result = minimax(board,"X")[0]
#                 if(value > result):
#                     value = result
#                     step = (i,j)
#                 board[i][j] = None
#         return (value,step)

if __name__=="__main__":
    app.run(debug=True)



    # if request.method == 'POST':
    #     if request.args.get('name') == '':
    #         return render_template('index.html', method=request.method, name=name)
    #     return redirect('/play')
    # else:
    #     return render_template('index.html', method=request.method)