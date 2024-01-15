import customtkinter
import tkinter
from pytube import YouTube
def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link,on_progress_callback=prog)
        vid = yt_object.streams.get_highest_resolution()
        link_label.configure(text=yt_object.title)
        finish_label.configure(text="")
        vid.download()
        finish_label.configure(text="Download Complete!!", text_color="white",font=("Hevetica",20))
    except:
        finish_label.configure(text="download error, please enter a valid link",text_color="red")
def prog(stream,chunk,bytes_remaining):
    totalsize=stream.filesize
    bytes_downloaded = totalsize - bytes_remaining
    perc= str(int(bytes_downloaded/totalsize*100))
    percentage.configure(text= perc +'%')
    percentage.update()

    progress.set(float(perc)/100)



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("MoonlitSky.json")

app= customtkinter.CTk()
app.geometry("720x480")
app.title("YTdownloader")

link_label = customtkinter.CTkLabel(app,text="Enter the desired link",font=("Helvetica", 20,"bold"))
link_label.pack(padx=10,pady=40)

url = tkinter.StringVar()

link = customtkinter.CTkEntry(master=app, textvariable=url,corner_radius=15,width=250,border_width=3,fg_color="#1e1e1e",border_color="#1e1e1e")
link.pack()

finish_label = customtkinter.CTkLabel(app,text="")
finish_label.pack()

download_button= customtkinter.CTkButton(master=app,command=start_download,text="Download",corner_radius=32,fg_color="#152238",hover_color="#111111")
download_button.place(relx=0.5,rely=0.37,anchor="center")

percentage = customtkinter.CTkLabel(app,text="0%",text_color="white")
percentage.pack(pady=30)

progress=customtkinter.CTkProgressBar(app,width=400,progress_color="#0096c7",fg_color="white",bg_color="#0096c7",corner_radius=10)
progress.set(0)
progress.pack()



app.mainloop()
