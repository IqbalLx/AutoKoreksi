from tkinter import *
from tkinter import messagebox
import sys
import webbrowser
from os.path import join
from os import chdir

filename = 'otak.png'
if hasattr(sys, '_MEIPASS'):
    chdir(sys._MEIPASS)
    filename = join(sys._MEIPASS, filename)
else:
    chdir(dirname(sys.argv[0]))
    filename = join(dirname(sys.argv[0]), filename)

filename1 = 'app.ico'
if hasattr(sys, '_MEIPASS'):
    chdir(sys._MEIPASS)
    filename1 = join(sys._MEIPASS, filename1)
else:
    chdir(dirname(sys.argv[0]))
    filename1 = join(dirname(sys.argv[0]), filename1)

def metu():
    if messagebox.askokcancel('Keluar', 'Yakin ingin keluar ?', icon='warning'):
        top.destroy()
    else:
        pass
        return

def main():
    kuy.destroy()
    foto.destroy()
    def mulai():
        try:
            e = list(kunci.get())
            f = float(kkm.get())
            g = float(skor.get())
            h = list(jawaban.get())

            benar = 0
            for i in range(len(e)):
                if e[i] == h[i]:
                    benar += 1

            skor_akhir = float(benar * g)
            if skor_akhir >= float(f):
                i = 'Lulus'
            elif skor_akhir < f:
                i = 'Remedial'

            box.delete(1.0, END)
            print('Benar   = {}\nSalah   = {}\nNilai     = {}\nStatus  = {}\n\nSelesai !'.format(benar, len(e) - benar, skor_akhir, i))
            jawaban.delete(0, END)
        except:
            messagebox.showinfo('Perhatian !', 'Isi setiap kolom dengan benar !\nCek Bantuan untuk Cara Penggunaan')

    def reset():
        if messagebox.askyesno('Reset', 'Reset Semua Kolom ?', icon='warning'):
            kunci.delete(0, END)
            kkm.delete(0, END)
            skor.delete(0, END)
            jawaban.delete(0, END)
            box.delete(1.0, END)
        else:
            pass
            return

    def redirestor(x):
        box.insert(INSERT, x)
        return

    sys.stdout.write = redirestor

    root = Frame(top)
    root.pack()

    def help():
        new = Toplevel(top)
        new.resizable(width=False, height=False)
        new.geometry('560x176')
        help = Label(new, text='Cara Penggunaan Aplikasi Auto Korektor').grid(row=0, column=0)
        satu = Label(new,text='1. Masukan Kunci Jawaban').grid(row=1, stick=W)
        dua = Label(new, text='2. Masukkan Nilai Minimum atau KKM').grid(row=2, stick=W)
        tiga = Label(new, text='3. Masukkan Nilai atau Skor untuk setiap jawaban benar. Gunakan titik untuk skor dengan angka desimal').grid(row=3, stick=W)
        empat = Label(new, text='4. Masukkan Jawaban Murid, jika murid tidak menjawab pada nomor tertentu isikan dengan "x"').grid(row=4, stick=W)
        lima = Label(new, text='5. Klik Mulai untuk memulai koreksi otomatis').grid(row=5, stick=W)
        enam = Label(new, text='6. Jika telah selesai satu paket soal, klik Reset untuk memulai kembali dari awal').grid(row=6, stick=W)
        back = Button(new, text='Tutup',width=20, command=lambda: new.destroy())
        back.grid(row=8,sticky=S)

    def link(event):
        webbrowser.open_new(event.widget.cget("text"))

    def about():
        new = Toplevel(top)
        new.resizable(width=False, height=False)
        new.geometry('300x157')
        help = Label(new, text='Credit\n\nM Iqbal Maulana').pack(side='top')
        sign = Label(new, text=r'www.otak-keren.com', fg='blue', cursor='hand2')
        sign.pack(side='top')
        sign.bind("<Button-1>", link)
        fol1 = Label(new, text='Like Fanspage Otak Keren Saya', fg ='red').pack(side='top')
        fol = Label(new, text=r'www.facebook.com/otakkereniqbal', fg = 'blue', cursor='hand2')
        fol.pack(side='top')
        fol.bind('<Button-1>', link)
        back = Button(new, text='Tutup',width=20, command=lambda: new.destroy()).pack(side='bottom')


    menu = Menu(top)
    top.config(menu=menu)

    bantuan = Menu(menu)
    menu.add_cascade(label='Bantuan', menu=bantuan)
    bantuan.add_command(label='Cara Penggunaan', command=help)

    tentang = Menu(menu)
    menu.add_cascade(label='Tentang', menu=tentang)
    tentang.add_command(label='Pembuat', command=about)

    a = Label(root, text='Kunci Jawaban : ').grid(row=0, column=0, sticky=E)
    b = Label(root, text='Nilai Minimum : ').grid(row=1, column=0, sticky=E)
    c = Label(root, text='Skor per Jawaban Benar : ').grid(row=2, column=0, sticky=E)
    d = Label(root, text='Jawaban Murid : ').grid(row=3, column=0, sticky=E)

    kunci = Entry(root, width=60)
    kunci.grid(row=0, column=1, columnspan=3)
    kkm = Entry(root, width=60)
    kkm.grid(row=1, column=1, columnspan=3)
    skor = Entry(root, width=60)
    skor.grid(row=2, column=1, columnspan=3)
    jawaban = Entry(root, width=60)
    jawaban.grid(row=3, column=1, columnspan=3)

    hasil = Label(root, text='Hasil :', fg='red').grid(row=7, columnspan=4)
    box = Text(root, width=35, height=6, fg='red', font=('Times New Roman', 14))
    box.grid(row=8, columnspan=4)
    space = Label(root, text='\n')
    space1 = Label(root, text='\n')
    space2 = Label(root, text='\n')
    space1.grid(row=4)
    yok = Button(root, text='Mulai !',activebackground='blue',fg='red', width=40,height=2,cursor='hand2', command = mulai).grid(row=5, columnspan=4)
    space.grid(row=6)
    space2.grid(row=9)
    keuar = Button(root, text='Keluar', fg='red', width=10, command=metu).grid(row=10, column=3, sticky=W)
    res = Button(root, text='Reset', fg='green', width=10, command=reset).grid(row=10, column=2, )

    credit = Label(root, text='Created by : M Iqbal Maulana', fg='red')
    credit.grid(row=10, column=0)
    sign = Label(root, text=r'www.otak-keren.com', fg='blue', cursor='hand2')
    sign.grid(row=10, column=1, sticky=W)
    sign.bind("<Button-1>", link)
    return

top = Tk()
top.title('AutoKorektor BETA')
top.resizable(width=False, height=False)
top.geometry('535x413')
top.iconbitmap(default='app.ico')

kuy = Frame(top)
kuy.pack(fill='both')
cuy = Label(kuy, text='\n\n\n\nSelamat datang di Aplikasi\nAuto Korektor BETA\nCopyright 2017 ( M Iqbal Maulana )\n\n\n', fg='green')
cuy.config(width=200)
cuy.config(font=('Algerian', 15))
cuy.pack(side=TOP)
start = Button(kuy, text='Mulai',cursor='hand2',width=20, bg='white', activebackground='green', fg='red', command=main).pack(side=TOP)
exit = Button(kuy, text='Keluar',width=20, command=metu).pack(side=BOTTOM)

fot = PhotoImage(file='otak.png')
foto =Label(top, image=fot, width=60, height=60)
foto.pack(side=BOTTOM, anchor=SW)

top.mainloop()
