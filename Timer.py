import PySimpleGUI as pg
from playsound import playsound
from time import sleep

class Clock:
    def __init__(self) -> None:
        tema = pg.theme("DarkRed")
        self.Janela = [
            [pg.Text("Work Time",key="t1"),pg.Input(default_text=1,size=(10,15),key="workt")],
            [pg.Text("Rest Time",key="t2"),pg.Input(default_text=1,size=(10,15),key="restt")],
            [pg.Text("Loops",key="t3"),pg.Input(default_text=2,size=(10,15),key="loop")],
            [pg.Button("START",key="start")]
        ]
        self.pomot = [
            [pg.Text(f"",size=(30,30),justification="center",key="crono")],
        ]

    def verifyINT(self,value1:int,value2:int,value3:int):
        try :
            if value1 != None and value2 != None and value3 != None:
                valores = [int(value1),int(value2),int(value3)]
                return True
            else:
                return False
        except:
            return False 


    def run(self):
        #1
        janela = pg.Window("PomoTimer",layout=self.Janela,size=(200,150),grab_anywhere=True)
        #2
        promow = pg.Window("PomoTimer",layout=self.pomot,size=(110,75),grab_anywhere=True)
        
        wcache = 0
        rcache = 0
        lcache = 0

        while True:
            event , value = janela.read(1)
            verify1 = self.verifyINT(value["workt"],value["restt"],value["loop"])

            if value["workt"] != "" and value["restt"] != "" and value["loop"] != "":
                wcache = int(value["workt"])
                rcache = int(value["restt"])
                lcache = int(value["loop"])

            if event in ("Exit",pg.WINDOW_CLOSED):
                janela.close()
                break
            
            if verify1 == True:
                if event == "start":
                    janela.close()
                    break
###########################################################
        #janela do timer
        wsec = 0
        rsec = 0
        rest= rcache
        work = wcache
        while lcache > 0 :
            event ,value = promow.read(1)
            if event in ("Exit",pg.WINDOW_CLOSED):
                janela.close()
                break
            if work >= 0:
                if wsec == 0 :
                    wsec = 59
                    work -= 1
                if work >= 0:
                    sleep(1)
                    promow["crono"].update(f"Work Time!\n{work}:{wsec}\nRepetitions:{lcache-1}")
                    wsec -= 1
                    continue

            if work < 0 and rest >= 0:
                if rsec == 0:
                    rsec = 59
                    rest -= 1
                if rest >= 0:
                    sleep(1)
                    promow["crono"].update(f"Rest Time!\n{rest}:{rsec}\nRepetitions:{lcache-1}")
                    rsec -= 1

            elif rest < 0 :
                lcache -= 1
                work = wcache
                rest = rcache
                wsec = 0
                rsec = 0
                if lcache >=0:
                    playsound("lets_goMa.mp3")
                continue

a = Clock()
a.run()