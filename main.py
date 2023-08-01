from tkinter import * 

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()
    def tela(self):
        self.root.title("Sistema SLX")
        self.root.configure(background= "#D3D3D3")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd= 4, bg= "white", 
                             highlightbackground="#D3D3D3", highlightthickness= 2 )
        self.frame_1.place(relx= 0.02,  rely= 0.02, relwidth= 0.97, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd= 4, bg= "white", 
                             highlightbackground="#D3D3D3", highlightthickness= 2 )
        self.frame_2.place(relx= 0.02,  rely= 0.5, relwidth= 0.97, relheight= 0.46)

          




Application()