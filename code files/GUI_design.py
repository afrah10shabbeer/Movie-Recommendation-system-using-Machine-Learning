from tkinter import *
import Movie_recommendation_system as mrs


# ----------------------------Functions----------------

def search_movie():
        
    # Get the movie name from the text label    
    movie_name = movie_textbox.get("1.0","end-1c")

    # Call the backend code to get the recommended movies
    recommended_movies = mrs.get_recommendation(movie_name)

    print(recommended_movies)
    resultant_movies_text_box.delete("1.0",END)
    confidence_text_box.delete("1.0",END)



    resultant_movies_text_box.insert(END,"\n")
    confidence_text_box.insert(END,"\n")

    for tuple_item in recommended_movies:

        movie,confidence = tuple_item

        # resultant_movies_text_box.delete("1.0",END)
        resultant_movies_text_box.insert(END,f"{movie:^1s}")
        resultant_movies_text_box.insert(END,"\n\n")


        confidence_text_box.insert(END,"{:.3f}".format(confidence))
        confidence_text_box.insert(END,"\n\n")



# --------------------Color variables---------------------------
window_bg_color = "#0d0d0d"
# core_color = "#6600cc"
core_color = '#e60000'
text_box_color = "white"
label_bg_color = "white"  


window = Tk()
window.geometry("1200x900+400+100")  # (width,height)
window.config(bg=window_bg_color)
window.title("Movie Recommendation App")

# --------------------- Movie Recommendation Label -------------------------

# Movie label
movie_label = Label(fg="white", text="Movie", font="Helvetica 40 bold", bg=window_bg_color)
movie_label.place(x=227, y=60)

# Recommendation label
recommendation_label = Label(fg=core_color, text="Recommendation", font="Helvetica 41 bold", bg=window_bg_color)
recommendation_label.place(x=400, y=60)

# App label
app_label = Label(fg="white", text="App", font="Helvetica 40 bold", bg=window_bg_color)
app_label.place(x=872, y=60)

# Caption label
caption_label = Label(fg="white", text="Get movie recommendations based on your favorite movie", font="Calibri 18", bg=window_bg_color)
caption_label.place(x=240, y=130)


# ----------------------Text Boxes-----------------------------------

movie_textbox = Text(window,height=1,width=51,bg=text_box_color,fg="#8c8c8c",font = "Helvetica 13",padx = 10,pady = 10)

def on_text_focus_in(event):
    if movie_textbox.get("1.0", "end-1c") == "Enter movie name":
        movie_textbox.delete("1.0", "end-1c")
        movie_textbox.config(fg="black")

def on_text_focus_out(event):
    if movie_textbox.get("1.0", "end-1c") == "Enter movie name":
        movie_textbox.insert("1.0", "Enter movie here")
        movie_textbox.config(fg="red")

movie_textbox.insert("1.0", "Enter movie name")
movie_textbox.bind("<FocusIn>", on_text_focus_in)
movie_textbox.bind("<FocusOut>", on_text_focus_out)

movie_textbox.place(x=250,y=240) 

# ---------------------Search Box-----------------------------------------
search_button = Button(window,width=13,height=2,fg="white",bg=core_color,padx=0,pady=0,command = search_movie,text="Search",font = "Helvetica 14 bold",bd=0,highlightthickness=0)
search_button.place(x=800,y=241)


# ----------------------Header label------------------------------------------

headlines = "\tRecommended Movie\t\t                 Confidence"
header_label = Label(text=headlines,fg="white",font="Helvetica 13 ",bg=core_color,padx=21,pady=11,width=64,highlightthickness=1)
header_label.place(x=248,y=330)

# --------------------Text widget to diplay resulting movies -------------------------------------


resultant_movies_text_box = Text(window,width = 50,height=22,fg="white",bg=window_bg_color,relief=FLAT,font = "Helvetica 14",borderwidth=1,highlightbackground="#d9d9d9",padx=20)
resultant_movies_text_box.place(x=248,y=370)

confidence_text_box = Text(window,width = 7,height=22,fg="white",bg=window_bg_color,relief=FLAT,font = "Helvetica 14",borderwidth=1,highlightbackground="#d9d9d9",padx=56)
confidence_text_box.place(x=748,y=370)




window.mainloop()





