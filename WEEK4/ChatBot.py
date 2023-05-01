#------------------------------------------------------------------Library-----------------------------------------------------------------
import tkinter as tk
import nltk
from nltk.chat.util import Chat, reflections


#--------------------------------------------------------------------Chat_Var----------------------------------------------------------------

chat_Q_A = [
            ['      What is computer science?', ['     Computer science is the study of computers and computational systems.']],
            
            ['        What is programming?', ['     Programming is the process of designing, writing, testing, and maintaining computer programs.']],
            
            ['     What is a computer program?', ['     A computer program is a set of instructions that tells a computer what to do.']],
            
            ['        What is an algorithm?', ['     An algorithm is a set of instructions for solving a problem or performing a task.']],
            
            ['    What is artificial intelligence?', ['     Artificial intelligence is the simulation of human intelligence in machines that are programmed to think and act like humans.']],
            
            ['       What is machine learning?', ['     Machine learning is a type of artificial intelligence that allows computers to learn from data and improve their performance over time.']],
            
            ['        What is a database?', ['     A database is a collection of data that is organized and stored in a way that allows for efficient retrieval and manipulation.']],
            
            ['(.*)', ['     Sorry, I did not understand what you said.']]
        ]
        
#------------------------------------------------------------------Functions---------------------------------------------------------------


def Question_Send():
        selected_question = Q_list.get(tk.ACTIVE)
        response = chatbot.respond(selected_question)
        chat_history.insert(tk.END, "You: " + selected_question + "\n\n")
        chat_history.insert(tk.END, "Chatbot: \n" + response + "\n\n")
        


#--------------------------------------------------------------------GUI-------------------------------------------------------------------
root = tk.Tk()
root.geometry("700x450")
root.configure(bg="white")
root.title("Computer Science Chatbot")
       
chatbot = Chat(chat_Q_A, reflections)


chat_history = tk.Text(root, height=20, width=90 ,highlightthickness=0)
chat_history.pack( padx=10, pady=10)


Q_list = tk.Listbox(root, height=10, width=39 ,highlightthickness=0)
Q_list.pack(pady=10,padx=10)

items = [" ","      What is computer science?",
         " ","        What is programming?",
         " ","     What is a computer program?",
         " ","        What is an algorithm?"  ,
         " ","    What is artificial intelligence?" ,
         " ","       What is machine learning?",
         " ","        What is a database?"]

for item in items:
    Q_list.insert(tk.END, item)


tk.Button(root, text="Send", command=Question_Send ,width=10 , bg = "plum" ,highlightthickness=0 ).pack( padx=10, pady=10)

root.mainloop()


