from tkinter import *

top= Tk()

top.title('Auto Koreksi v1.0')

root= Frame(top, width=400, height=400)
root.pack()

kunci  = Label(root, text='Kunci Jawaban   :', fg = 'green')
kuncibox = Entry(root, width=50)
kunci.grid(row=2, column=0)
kuncibox.grid(row=2, column=1)
warn = Label(root, text='Perhatikan Input Kunci Jawaban\nPastikan Input Kunci Benar', bg='yellow', fg = 'red')
warn.grid(row=3, column=1)

skor   = Label(root, text='Skor per Jawaban:', fg = 'green')
skorbox = Entry(root, width=50)
skor.grid(row=4, column=0)
skorbox.grid(row=4, column = 1)

kkm    = Label(root, text='Nilai KKM       :', fg='green')
kkmbox = Entry(root, width=50)
kkm.grid(row=5, column=0)
kkmbox.grid(row=5, column=1)

jawab  = Label(root, text='Jawaban Murid   :', fg = 'green')
jawabbox = Entry(root, width=50)
jawab.grid(row=6, column=0)
jawabbox.grid(row=6, column=1)

def com():
    try:
        kunci_data = kuncibox.get()
        skor_data = int(skorbox.get())
        kkm_data = int(kkmbox.get())
        jawab_data = jawabbox.get()

        hasil = Label(root, text='HASIL :', fg='red')
        hasilbox= Entry(root, width=40)
    
        a = list(kunci_data)
        b = list(jawab_data)
        benar = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                benar += 1

        skor_akhir = float(int(benar)*skor_data)
        status = ''
        if skor_akhir >= kkm_data:
            status ='Lulus'
        else:
           status='Remedial'

        hasil.grid(row=9, column=0)
        hasilbox.grid(row=10, column=0)
    
        hasilbox.insert(0, "Skor = {0}, ({1})".format(skor_akhir, status))
        jawabbox.delete(0, END)
        return
    except:
        per = Label(root, text='Isi semua kolom dengan benar !', bg='yellow', fg='red')
        per.grid(row=7, column=1)

proses = Button(root, text='Mulai !', bg='white', fg='red',width=15, command=com)
proses.grid(row=8, column=1)

exit = Button(root, text='EXIT', fg='red', command=top.quit())
exit.grid(row=11, column=3)

def rest():
    kuncibox.delete(0,END)
    skorbox.delete(0,END)
    kkmbox.delete(0, END)
    jawabbox.delete(0, END)
    return

res= Button(root, text='Reset', fg='green',command=rest)
res.grid(row=11,column=2)

cop = Label(root, text='Copyright 2017 M Iqbal Maulana', fg='red')
cop.grid(row=11, column=0)

root.mainloop()
