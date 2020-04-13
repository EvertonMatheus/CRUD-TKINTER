from tkinter import *
import sqlite3
from tkinter import messagebox

lista_a_ = []
lista_p_ = []

#criando a tabela ALUNO no banco de dados

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (nome TEXT NOT NULL, cpf TEXT NOT NULL)''')
conn.close()

#criando a tabela PROFESSORES no banco de dados

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS professores (nome TEXT NOT NULL, cpf TEXT NOT NULL, departamento TEXT NOT NULL)''')
conn.close()

#criando a tabela DISCIPLINA no banco de dados

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS disciplinas (nome TEXT NOT NULL, código TEXT NOT NULL)''')
conn.close()

#criando a tabela de TURMAS no banco de dados

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS turmas (codt TEXT NOT NULL, per TEXT NOT NULL, 
codd TEXT NOT NULL, cpfa TEXT NOT NULL, cpfp TEXT NOT NULL)''')
conn.close()

#criando a tabela relatorio aluno no banco de dados

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS relatorioal (cpf TEXT NOT NULL, turma TEXT NOT NULL, disciplina TEXT NOT NULL,
 periodo TEXT NOT NULL)''')
conn.close()

#criando a tabela relatorio professor no banco de dados

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS relatorioprof (cpf TEXT NOT NULL, turma TEXT NOT NULL, disciplina TEXT NOT NULL, per TEXT NOT NULL)''')
conn.close()

def aluno():
    Frame_principal.place(x=9000,y=0)
    frame_al.place(x=0,y=0)

def professor():
    Frame_principal.place(x=9000,y=0)
    frame_prof.place(x=0,y=0)

def turma():
    Frame_principal.place(x=9000,y=0)
    frame_turma.place(x=0,y=0)

def disciplina():
    Frame_principal.place(x=9000, y=0)
    frame_disc.place(x=0,y=0)

def voltar_principal_a():
    Frame_principal.place(x=0, y=0)
    frame_al.place(x=9000, y=0)

def voltar_principal_p():
    Frame_principal.place(x=0, y=0)
    frame_prof.place(x=9000, y=0)

def voltar_principal_t():
    Frame_principal.place(x=0, y=0)
    frame_turma.place(x=9000, y=0)

def voltar_principal_d():
    Frame_principal.place(x=0, y=0)
    frame_disc.place(x=9000, y=0)

def voltar_aluno():
    Frame_principal.place(x=9000, y=0)
    frame_al.place(x=0, y=0)
    frame_cadalu.place(x=9000, y=0)

def voltar_prof():
    Frame_principal.place(x=9000, y=0)
    frame_prof.place(x=0, y=0)
    frame_cadprof.place(x=9000, y=0)

def voltar_turma():
    Frame_principal.place(x=9000, y=0)
    frame_turma.place(x=0, y=0)
    frame_cadturma.place(x=9000, y=0)
    print(lista_a_)
    print(lista_p_)

def voltar_disc():
    Frame_principal.place(x=9000, y=0)
    frame_disc.place(x=0, y=0)
    frame_cad_disc.place(x=9000, y=0)

def cad_aluno():

    Frame_principal.place(x=9000, y=0)
    frame_al.place(x=9000, y=0)
    frame_cadalu.place(x=0,y=0)


def cad_prof():
    Frame_principal.place(x=9000, y=0)
    frame_prof.place(x=9000, y=0)
    frame_cadprof.place(x=0,y=0)


def cad_disc():
    Frame_principal.place(x=9000, y=0)
    frame_disc.place(x=9000, y=0)
    frame_cad_disc.place(x=0, y=0)

def cad_turma():
    Frame_principal.place(x=9000, y=0)
    frame_turma.place(x=9000, y=0)
    frame_cadturma.place(x=0, y=0)

def consulta_al():
    Frame_principal.place(x=9000, y=0)
    frame_al.place(x=9000, y=0)
    frame_conalu.place(x=0, y=0)
    listaa.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM alunos ''')
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listaa.insert(0, ' | '.join(i))

    conn.close()


def consulta_prof():
    Frame_principal.place(x=9000, y=0)
    frame_prof.place(x=9000, y=0)
    frame_conprof.place(x=0, y=0)
    listap.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM professores ''')
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listap.insert(0, ' | '.join(i))

def consulta_disciplina():
    Frame_principal.place(x=9000, y=0)
    frame_disc.place(x=9000, y=0)
    frame_condisc.place(x=0, y=0)
    listad.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM disciplinas ''')
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listad.insert(0, ' | '.join(i))

def consulta_turma():
    Frame_principal.place(x=9000, y=0)
    frame_turma.place(x=9000, y=0)
    frame_conturma.place(x=0, y=0)

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM turmas ''')
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listat.insert(0, ' | '.join(i))


def voltar_principal_a1():
    Frame_principal.place(x=9000, y=0)
    frame_conalu.place(x=9000, y=0)
    frame_al.place(x=0, y=0)

def voltar_principal_p1():
    Frame_principal.place(x=9000, y=0)
    frame_conprof.place(x=9000, y=0)
    frame_prof.place(x=0,y=0)

def voltar_principal_d1():
    Frame_principal.place(x=9000, y=0)
    frame_condisc.place(x=9000, y=0)
    frame_disc.place(x=0,y=0)

def voltar_principal_t1():
    Frame_principal.place(x=9000, y=0)
    frame_conturma.place(x=9000, y=0)
    frame_turma.place(x=0,y=0)

def atualizar_al():
    Frame_principal.place(x=9000, y=0)
    frame_al.place(x=9000, y=0)
    frame_att_al.place(x=0, y=0)

def atualizar_prof():
    Frame_principal.place(x=9000, y=0)
    frame_prof.place(x=9000, y=0)
    frame_att_prof.place(x=0, y=0)

def atualizar_turma():
    Frame_principal.place(x=9000, y=0)
    frame_turma.place(x=9000, y=0)
    frame_att_turma.place(x=0, y=0)

def atualizar_disc():
    Frame_principal.place(x=9000, y=0)
    frame_disc.place(x=9000, y=0)
    frame_att_disc.place(x=0, y=0)

def voltar_all():
    Frame_principal.place(x=9000, y=0)
    frame_conalu.place(x=9000, y=0)
    frame_att_al.place(x=9000,y=0)
    frame_al.place(x=0, y=0)

def voltar_pro():
    Frame_principal.place(x=9000, y=0)
    frame_conprof.place(x=9000, y=0)
    frame_att_prof.place(x=9000,y=0)
    frame_prof.place(x=0, y=0)

def voltar_dis():
    Frame_principal.place(x=9000, y=0)
    frame_condisc.place(x=9000, y=0)
    frame_att_disc.place(x=9000,y=0)
    frame_disc.place(x=0, y=0)

def voltar_turm():
    Frame_principal.place(x=9000, y=0)
    frame_conturma.place(x=9000, y=0)
    frame_att_turma.place(x=9000,y=0)
    frame_turma.place(x=0, y=0)

def deletar_al():
    Frame_principal.place(x=9000, y=0)
    frame_al.place(x=9000, y=0)
    frame_del_al.place(x=0, y=0)

def deletar_prof():
    Frame_principal.place(x=9000, y=0)
    frame_prof.place(x=9000, y=0)
    frame_del_prof.place(x=0, y=0)

def deletar_disc():
    Frame_principal.place(x=9000, y=0)
    frame_disc.place(x=9000, y=0)
    frame_del_disc.place(x=0, y=0)

def deletar_turma():
    Frame_principal.place(x=9000, y=0)
    frame_turma.place(x=9000, y=0)
    frame_del_turma.place(x=0, y=0)

def voltar_allu():
    Frame_principal.place(x=9000, y=0)
    frame_conalu.place(x=9000, y=0)
    frame_del_al.place(x=9000, y=0)
    frame_al.place(x=0, y=0)

def voltar_proff():
    Frame_principal.place(x=9000, y=0)
    frame_conprof.place(x=9000, y=0)
    frame_del_prof.place(x=9000, y=0)
    frame_prof.place(x=0, y=0)

def voltar_discc():
    Frame_principal.place(x=9000, y=0)
    frame_condisc.place(x=9000, y=0)
    frame_del_disc.place(x=9000, y=0)
    frame_disc.place(x=0, y=0)


def voltar_turmm():
    Frame_principal.place(x=9000, y=0)
    frame_conturma.place(x=9000, y=0)
    frame_del_turma.place(x=9000, y=0)
    frame_turma.place(x=0, y=0)

def relatórioal():
    Frame_principal.place(x=9000, y=0)
    frame_al.place(x=9000, y=0)
    frame_relatorioal.place(x=0, y=0)

def voltar_relal():
    Frame_principal.place(x=9000, y=0)
    frame_al.place(x=0, y=0)
    frame_relatorioal.place(x=9000, y=0)

def relatórioprof():
    Frame_principal.place(x=9000, y=0)
    frame_prof.place(x=9000, y=0)
    frame_relatorioprof.place(x=0, y=0)

def voltar_relprof():
    Frame_principal.place(x=9000, y=0)
    frame_prof.place(x=0, y=0)
    frame_relatorioprof.place(x=9000, y=0)

def ata():
    Frame_principal.place(x=9000, y=0)
    frame_turma.place(x=9000, y=0)
    frame_ata.place(x=0, y=0)

def voltar_ata():
    Frame_principal.place(x=9000, y=0)
    frame_turma.place(x=0, y=0)
    frame_ata.place(x=9000, y=0)

#---------------------------------- DEF'S BANCO DE DADOS --------------------------------------------------#

def bd_cadalu():
    if valida_nome_aluno() is False:
        messagebox.showwarning('Cadastro', 'Nome Inválido')
    elif valida_cpf_aluno() is False:
        messagebox.showwarning('Cadastro', 'CPF Inválido')

    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO alunos (nome,cpf)
                        VALUES(?,?)''', (ent_nome.get(), ent_cpf.get(),))
        conn.commit()
        conn.close()
        ent_nome.delete(0, END)
        ent_cpf.delete(0, END)
        messagebox.showinfo('Cadastro', 'Aluno Cadastrado com Sucesso!')

def bd_cadprof():
    if valida_nome_professor() is False:
        messagebox.showwarning('Cadastro', 'Nome Inválido')
    elif valida_cpf_professor() is False:
        messagebox.showwarning('Cadastro', 'CPF Inválido')

    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO professores (nome,cpf,departamento)
                        VALUES(?,?,?)''', (ent_nome_p.get(),ent_cpf_p.get(),ent_dep_p.get(),))
        conn.commit()
        conn.close()
        ent_nome_p.delete(0, END)
        ent_cpf_p.delete(0, END)
        ent_dep_p.delete(0, END)
        messagebox.showinfo('Cadastro', 'Professor Cadastrado com Sucesso!')


def bd_caddisc():
    if valida_nome_disc() is False:
        messagebox.showwarning('Cadastro', 'Nome Inválido')
    elif valida_cod_disc() is False:
        messagebox.showwarning('Cadastro', 'Código Inválido')

    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO disciplinas (nome,código)
                        VALUES(?,?)''', (ent_nome_d.get(), ent_código_d.get(),))
        conn.commit()
        conn.close()
        ent_nome_d.delete(0, END)
        ent_código_d.delete(0, END)
        messagebox.showinfo('Cadastro', 'Disciplina Cadastrada com Sucesso!')

def bd_cadturma():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO turmas (codt,per,codd,cpfa,cpfp)
                      VALUES(?,?,?,?,?)''', (ent_cod_t.get(), ent_per.get(),ent_cod_disc.get(),('-'.join(lista_a_)),('-'.join(lista_p_)),))
    conn.commit()
    conn.close()
    ent_cod_t.delete(0, END)
    ent_per.delete(0, END)
    ent_cod_disc.delete(0, END)
    ent_cpfal.delete(0, END)
    ent_cpfprof.delete(0, END)
    messagebox.showinfo('Cadastro', 'Turma Cadastrado com Sucesso!')
    for i in lista_a_:
        lista_a_.pop(lista_a_.index(i))
    for i in lista_p_:
        lista_p_.pop(lista_p_.index(i))

def valida_cpf_aluno():
    x = 0
    if len(ent_cpf.get()) == 11:
        for i in ent_cpf.get():
            if i.isalpha():
                x += 1
            else:
                continue
        if x > 0:
            return False
        else:
            return True
    else:
        return False

def valida_nome_aluno():
    x =0
    for i in ent_nome.get():
        if i.isnumeric():
            x = x + 1
        else:
            continue
    if x >0:
        return False
    else:
        return True

def valida_cpf_professor():
    x = 0
    if len(ent_cpf_p.get()) == 11:
        for i in ent_cpf_p.get():
            if i.isalpha():
                x += 1
            else:
                continue
        if x > 0:
            return False
        else:
            return True
    else:
        return False

def valida_nome_professor():
    x =0
    for i in ent_nome_p.get():
        if i.isnumeric():
            x = x + 1
        else:
            continue
    if x >0:
        return False
    else:
        return True

def valida_nome_disc():
    x =0
    for i in ent_nome_d.get():
        if i.isnumeric():
            x = x + 1
        else:
            continue
    if x >0:
        return False
    else:
        return True

def valida_cod_disc():
    x = 0
    for i in ent_código_d.get():
        if i.isnumeric():
            continue
        else:
            x = x + 1
    if x > 0:
        return False
    else:
        return True

def consulta_al_ex():
    listaa.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM alunos WHERE cpf = ? ''',(ent_cpf_c.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listaa.insert(0, ' | '.join(i))

    conn.close()

def consulta_prof_ex():
    listap.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM professores WHERE cpf = ? ''',(ent_cpf_p2.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listap.insert(0, ' | '.join(i))

    conn.close()


def consulta_d_ex():
    listad.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM disciplinas WHERE código = ? ''',(ent_cod_di.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listad.insert(0, ' | '.join(i))

    conn.close()

def consulta_t_ex():
    listat.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM turmas WHERE codt = ? ''',(ent_codt_tu.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listat.insert(0, ' | '.join(i))

    conn.close()

def verifica_al():
    listaa.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM alunos WHERE cpf = ? ''',(ent_cpf_a.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')

    else:
        for i in var:
            listaa.insert(0, ' | '.join(i))

    conn.close()

def consulta_al_att():
    listaal.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM alunos''',)
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listaal.insert(0, ' | '.join(i))

    conn.close()

def att_al():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM alunos WHERE cpf = ? ''',(ent_cpf_a.get(),))
    var = cursor.fetchone()
    if var is None:
        print('oi')
    else:
        new_nome_a.insert(0, var[0])
        new_cpf_a.insert(0,var[1])
        print(var)

    conn.close()

# ATUALIZANDO DADOS DOS ALUNOS

def atuala():
    conn=sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE alunos SET nome = ?,cpf = ? WHERE cpf = ?''',(new_nome_a.get(),new_cpf_a.get(), ent_cpf_a.get(),))
    messagebox.showinfo(title='sucesso!',message='Atualizado com sucesso!')
    conn.commit()
    conn.close()

def consulta_a_del():
    malu.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM alunos ''')
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            malu.insert(0, ' | '.join(i))

    conn.close()

def remover_al():
    conn= sqlite3.connect('database.db')
    cursor=  conn.cursor()
    cursor.execute('''DELETE FROM alunos WHERE cpf = ?''',(ent_del_cpf.get(),))
    conn.commit()
    messagebox.showinfo(title='sucesso!', message='Removido com sucesso!')
    conn.close()

def consulta_t_del():
    mt1.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM turmas ''')
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            mt1.insert(0, ' | '.join(i))

    conn.close()

def remover_t():
    conn= sqlite3.connect('database.db')
    cursor=  conn.cursor()
    cursor.execute('''DELETE FROM turmas WHERE codt = ?''',(ent_del_cod.get(),))
    conn.commit()
    messagebox.showinfo(title='sucesso!', message='Removido com sucesso!')
    conn.close()


def consulta_att_p():
    listaprof1.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM professores ''')
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listaprof1.insert(0, ' | '.join(i))

    conn.close()

def att_prof():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM professores WHERE cpf = ? ''',(ent_cpf_p1.get(),))
    var = cursor.fetchone()
    if var is None:
        print('oi')
    else:
        new_nome_p.insert(0, var[0])
        new_cpf_p.insert(0,var[1])
        ent_dep_prof.insert(0,var[2])
        print(var)

    conn.close()

# ATUALIZANDO DADOS DOS PROFESORES

def atualp():
    conn=sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE professores SET nome = ?,cpf = ? ,departamento = ?WHERE cpf = ?''',(new_nome_p.get(),new_cpf_p.get(),ent_dep_prof.get(), ent_cpf_p1.get(),))
    messagebox.showinfo(title='sucesso!',message='Atualizado com sucesso!')
    conn.commit()
    conn.close()

#REMOVER PROFESSOR

def consulta_p_del():
    mprof.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM professores ''')
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            mprof.insert(0, ' | '.join(i))

    conn.close()

def remover_prof():
    conn= sqlite3.connect('database.db')
    cursor=  conn.cursor()
    cursor.execute('''DELETE FROM professores WHERE cpf = ?''',(ent_del_cpfp.get(),))
    conn.commit()
    messagebox.showinfo(title='sucesso!', message='Removido com sucesso!')
    conn.close()

#ATUALIZAR DISC

def verifica_disc():
    listad1.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM alunos WHERE código = ? ''',(ent_cod_d.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')

    else:
        for i in var:
            listad1.insert(0, ' | '.join(i))

    conn.close()

def consulta_disc_att():
    listad1.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM disciplinas''',)
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listad1.insert(0, ' | '.join(i))

    conn.close()

def att_disc():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM disciplinas WHERE código = ? ''',(ent_cod_d.get(),))
    var = cursor.fetchone()
    if var is None:
        print('oi')
    else:
        new_nome_d.insert(0, var[0])
        new_cod.insert(0,var[1])
        print(var)

    conn.close()

# ATUALIZANDO DADOS DA DISCIPLINA

def atuald():

    conn=sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE disciplinas SET nome = ?,código = ? WHERE código = ?''',(new_nome_d.get(),new_cod.get(), ent_cod_d.get(),))
    messagebox.showinfo(title='sucesso!',message='Atualizado com sucesso!')
    conn.commit()
    conn.close()

# REMOVER DISCILINA

def consulta_d_del():
    mdisc.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM disciplinas ''')
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            mdisc.insert(0, ' | '.join(i))

    conn.close()

def remover_disc():
    conn= sqlite3.connect('database.db')
    cursor=  conn.cursor()
    cursor.execute('''DELETE FROM disciplinas WHERE código = ?''',(ent_del_cod1.get(),))
    conn.commit()
    messagebox.showinfo(title='sucesso!', message='Removido com sucesso!')
    conn.close()

def consulta_al_geral():
    listaral.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf,turma,disciplina,periodo FROM relatorioal WHERE cpf = ? ''',(ent_cpf_ar.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listaral.insert(0, ' | '.join(i))

    conn.close()

def consulta_al_per():
    listaral.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT turma,disciplina,periodo FROM relatorioal WHERE cpf = ? ''',(ent_cpf_ar.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            if ent_per_ar.get() in i:
                listaral.insert(0,' | '.join(i))
            else:
                print('tuamae')

    conn.close()

def consulta_prof_geral():
    listarp.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpf,turma,disciplina,per FROM relatorioprof WHERE cpf = ? ''',(ent_cpf_pr.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            listarp.insert(0, ' | '.join(i))

    conn.close()

def consulta_prof_per():
    listarp.delete(0,END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT per,turma,disciplina FROM relatorioprof WHERE cpf = ? ''',(ent_cpf_pr.get(),))
    var = cursor.fetchall()
    if var is None:
        print('oi')
    else:
        for i in var:
            if ent_per_pr.get() in i:
                listarp.insert(0,' | '.join(i))

    conn.close()



def inserir_al():
    lista_a_.append(ent_cpfal.get())
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO relatorioal (cpf,turma,disciplina,periodo)
                           VALUES(?,?,?,?)''', (ent_cpfal.get(), ent_cod_t.get(),ent_cod_disc.get(),ent_per.get()))
    conn.commit()
    conn.close()
    ent_cpfal.delete(0, END)

def inserir_prof():
    lista_p_.append(ent_cpfprof.get())
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO relatorioprof (cpf,turma,disciplina,per)
                               VALUES(?,?,?,?)''',
                   (ent_cpfprof.get(), ent_cod_t.get(), ent_cod_disc.get(), ent_per.get()))
    conn.commit()
    conn.close()
    ent_cpfprof.delete(0,END)

def remover_al_att():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpfa FROM turmas WHERE codt = ? ''',(ent_cod_att.get(),))
    var = cursor.fetchone()
    lista_a_ = var[0].split('-')
    lista_a_.pop(lista_a_.index(ent_cpfalatt.get()))
    print(lista_a_)
    conn.close()


def remover_prof_att():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpfp FROM turmas WHERE codt = ? ''', (ent_cod_att.get(),))
    var = cursor.fetchone()
    lista_p_ = var[0].split('-')
    lista_p_.pop(lista_p_.index(ent_cpfprofatt.get()))
    print(lista_p_)
    conn.close()

def att_cpf_al():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpfa FROM turmas WHERE codt = ? ''', (ent_cod_att.get(),))
    var = cursor.fetchone()
    lista_a_ = var[0].split('-')
    x= lista_a_.index(ent_cpfalatt.get())
    lista_a_.pop(x)
    lista_a_.insert(x,ent_newcpfal.get())
    print(lista_a_)
    conn.close()

def att_cpf_prof():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT cpfp FROM turmas WHERE codt = ? ''', (ent_cod_att.get(),))
    var = cursor.fetchone()
    lista_p_ = var[0].split('-')
    x= lista_p_.index(ent_cpfprofatt.get())
    lista_p_.pop(x)
    lista_p_.insert(x,ent_newcpfprof.get())
    print(lista_p_)
    conn.close()




# ATUALIZANDO DADOS DA TURMA

def atualt():
    print(lista_a_)
    print(lista_p_)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE turmas SET codt = ?,per = ? ,codd = ?,cpfa = ?,cpfp = ? WHERE codt = ?''',
                   (ent_codt_at.get(), ent_per_at.get(), ent_codd_at.get(),'-'.join(lista_a_),'-'.join(lista_p_),ent_cod_att.get(),))

    messagebox.showinfo(title='sucesso!', message='Atualizado com sucesso!')
    conn.commit()
    conn.close()




def mostrar_t():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM turmas WHERE codt= ?''',(ent_cod_att.get(),))
    var = cursor.fetchone()
    if var is None:
        print('oi')
    else:
        ent_codt_at.insert(0,var[0]), ent_per_at.insert(0,var[1]), ent_codd_at.insert(0,var[2])


def ata1():
    listaata.delete(0, END)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM turmas WHERE codt = ? ''', (ent_codt.get(),))
    var = cursor.fetchone()
    cursor = conn.cursor()
    listaata.insert(0, '-' * 40 + ' Ata de exercício ' + '-' * 50)
    listaata.insert(1,' '*20 + 'Código da turma: ' + var[0] + '    |    Código da disciplina:' + var[2] + '    |    Período:' + var[1])
    conn1 = sqlite3.connect('database.db')
    cursor1 = conn1.cursor()
    conn2 = sqlite3.connect('database.db')
    cursor2 = conn2.cursor()
    listaata.insert(2, '-'*40 + ' Professores '  + '-'*50)
    for c in var[4].split('-'):
        cursor2.execute('''SELECT nome,cpf FROM professores WHERE cpf = ?''',(c,))
        listaata.insert(3, 'Nome: ' + '       |       CPF: '.join(cursor2.fetchone()))
    listaata.insert(4, '-'*42 + ' Alunos ' + '-'*53)
    for i in var[3].split('-'):
        cursor1.execute('''SELECT nome,cpf FROM alunos WHERE cpf = ?''',(i,))
        listaata.insert(5, 'Nome: ' + '       |       CPF: '.join(cursor1.fetchone()))


#---------------------------------------------------------FIM BANCO DE DADOS -------------------------------------------#

janela = Tk()
janela.title('Projeto ip')
janela.geometry('800x550+300+100')
janela['bg']='orangered4'
Frame_principal = Frame(janela,width=800,height=550,bg='orangered4')
Frame_principal.place(x=0,y=0)
Frame_principal.propagate(0)

mensagem = Label(Frame_principal, text='sistema de cadastramento', font='System 25 bold',bg='orangered4',fg='yellow2')
mensagem.place(x=220,y=5)

btcad_aluno = Button(Frame_principal,width=20,height=2,text='Aluno',bg='grey',fg='yellow3',font='System 10',command=aluno)
btcad_aluno.place(x=70,y=70)

btcad_prof = Button(Frame_principal,width=20,height=2,text='Professor',bg='grey',fg='yellow3',font='System 10',command=professor)
btcad_prof.place(x=500,y=70)

btcad_disc = Button(Frame_principal,width=20,height=2,text='Disciplina',bg='grey',fg='yellow3',font='System 10',command=disciplina)
btcad_disc.place(x=70,y=170)

btcad_turma = Button(Frame_principal,width=20,height=2,text='Turma',bg='grey',fg='yellow3',font='System 10',command=turma)
btcad_turma.place(x=500,y=170)

btsair = Button(Frame_principal,width=20,height=2,text='sair',bg='grey',fg='yellow2',font='System 10',command=janela.quit)
btsair.place(x=280,y=120)

img = PhotoImage(file='si.png')
label_imagem = Label(Frame_principal, image=img)
Left_Frame = Frame(Frame_principal,width=390,height=500,bg='orangered4',highlightbackground="orangered4", highlightthickness=3)
label_imagem.place(x=250,y=270)

#criando um novo frame para o botão inicial aluno
frame_al = Frame(janela,width=800,height=550,bg='orangered4')
frame_al.place(x=9000,y=0)
frame_al.propagate(0)

bt_cad_al= Button(frame_al,width=15,height=3,text='Cadastrar Aluno',bg='grey',fg='yellow2',font='System 10',command=cad_aluno)
bt_cad_al.place(x=150,y=70)

bt_con_al= Button(frame_al,width=15,height=3,text='Consultar Aluno',bg='grey',fg='yellow2',font='System 10',command=consulta_al)
bt_con_al.place(x=500,y=70)

bt_att_al= Button(frame_al,width=15,height=3,text='Atualizar Aluno',bg='grey',fg='yellow2',font='System 10',command=atualizar_al)
bt_att_al.place(x=150,y=200)

bt_del_al= Button(frame_al,width=15,height=3,text='Deletar Aluno',bg='grey',fg='yellow2',font='System 10',command=deletar_al)
bt_del_al.place(x=500,y=200)

voltar_p= Button(frame_al,width=15,height=3,text='Voltar',bg='grey',fg='yellow2',font='System 10',command=voltar_principal_a)
voltar_p.place(x=325,y=400)

bt_rel_a= Button(frame_al,width=15,height=3,text='Relatório Aluno',bg='grey',fg='yellow2',font='System 10',command=relatórioal)
bt_rel_a.place(x=325,y=300)

#criando um novo frame para o botão principal professor
frame_prof = Frame(janela,width=800,height=550,bg='orangered4')
frame_prof.place(x=9000,y=0)
frame_prof.propagate(0)

bt_cad_prof= Button(frame_prof,width=18,height=3,text='Cadastrar Professor',bg='grey',fg='yellow2',font='System 10',command=cad_prof)
bt_cad_prof.place(x=150,y=70)

bt_con_prof= Button(frame_prof,width=18,height=3,text='Consultar Professor',bg='grey',fg='yellow2',font='System 10',command=consulta_prof)
bt_con_prof.place(x=500,y=70)

bt_att_prof= Button(frame_prof,width=18,height=3,text='Atualizar Professor',bg='grey',fg='yellow2',font='System 10',command=atualizar_prof)
bt_att_prof.place(x=150,y=200)

bt_del_prof= Button(frame_prof,width=18,height=3,text='Deletar Professor',bg='grey',fg='yellow2',font='System 10',command=deletar_prof)
bt_del_prof.place(x=500,y=200)

voltar_pr= Button(frame_prof,width=18,height=3,text='Voltar',bg='grey',fg='yellow2',font='System 10',command=voltar_principal_p)
voltar_pr.place(x=325,y=400)

rel_prof= Button(frame_prof,width=18,height=3,text='Relatório Professor',bg='grey',fg='yellow2',font='System 10',command=relatórioprof)
rel_prof.place(x=325,y=300)

#criando um novo frame para o botão de turma

frame_turma = Frame(janela,width=800,height=550,bg='orangered4')
frame_turma.place(x=9000,y=0)
frame_turma.propagate(0)

bt_cad_turma= Button(frame_turma,width=18,height=3,text='Cadastrar Turma',bg='grey',fg='yellow2',font='System 10',command=cad_turma)
bt_cad_turma.place(x=150,y=70)

bt_con_turma= Button(frame_turma,width=18,height=3,text='Consultar Turma',bg='grey',fg='yellow2',font='System 10',command=consulta_turma)
bt_con_turma.place(x=500,y=70)

bt_att_turma= Button(frame_turma,width=18,height=3,text='Atualizar Turma',bg='grey',fg='yellow2',font='System 10',command=atualizar_turma)
bt_att_turma.place(x=150,y=200)

bt_del_turma= Button(frame_turma,width=18,height=3,text='Deletar Turma',bg='grey',fg='yellow2',font='System 10',command=deletar_turma)
bt_del_turma.place(x=500,y=200)

voltar_pri= Button(frame_turma,width=18,height=3,text='Voltar',bg='grey',fg='yellow2',font='System 10',command=voltar_principal_t)
voltar_pri.place(x=325,y=400)

ata_turma= Button(frame_turma,width=18,height=3,text='Ata',bg='grey',fg='yellow2',font='System 10',command=ata)
ata_turma.place(x=325,y=300)

#criando um novo frame para o botão disciplina

frame_disc = Frame(janela,width=800,height=550,bg='orangered4')
frame_disc.place(x=9000,y=0)
frame_disc.propagate(0)

bt_cad_disc= Button(frame_disc,width=18,height=3,text='Cadastrar Disciplina',bg='grey',fg='yellow2',font='System 10',command=cad_disc)
bt_cad_disc.place(x=150,y=70)

bt_con_disc= Button(frame_disc,width=18,height=3,text='Consultar Disciplina',bg='grey',fg='yellow2',font='System 10',command=consulta_disciplina)
bt_con_disc.place(x=500,y=70)

bt_att_disc= Button(frame_disc,width=18,height=3,text='Atualizar Disciplina',bg='grey',fg='yellow2',font='System 10',command=atualizar_disc)
bt_att_disc.place(x=150,y=200)

bt_del_disc= Button(frame_disc,width=18,height=3,text='Deletar Disciplina',bg='grey',fg='yellow2',font='System 10',command=deletar_disc)
bt_del_disc.place(x=500,y=200)

voltar_prin= Button(frame_disc,width=18,height=3,text='Voltar',bg='grey',fg='yellow2',font='System 10',command=voltar_principal_d)
voltar_prin.place(x=325,y=300)

#frame cadastro aluno
frame_cadalu = Frame(janela,width=800,height=550,bg='orangered4')
frame_cadalu.place(x=9000,y=0)
frame_cadalu.propagate(0)

ent_nome = Entry(frame_cadalu, font="arial 15")
ent_nome.place(x=90,y=55)
mensnome = Label(frame_cadalu, text='nome:', font='System 16 bold', bg='orangered4',
                     fg='black')
mensnome.place(x=40, y=60)
ent_cpf = Entry(frame_cadalu, font="arial 15")
ent_cpf.place(x=90, y=95)
menscpf = Label(frame_cadalu, text='cpf:', font='System 16 bold', bg='orangered4',
                     fg='black')
menscpf.place(x=50, y=100)
mensagemcadal = Label(frame_cadalu, text='Cadastro de Aluno', font='System 25 bold', bg='orangered4',
                     fg='yellow2')
mensagemcadal.place(x=80, y=5)
voltar_alu = Button(frame_cadalu, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                        command=voltar_aluno)
voltar_alu.place(x=130, y=150)
bcadastrar = Button(frame_cadalu, width=15, height=2, text='Cadastrar', bg='grey', fg='yellow2', font='System 10',
                        command=bd_cadalu)
bcadastrar.place(x=330, y=70)


#frame cadastro professor

frame_cadprof = Frame(janela,width=800,height=550,bg='orangered4')
frame_cadprof.place(x=9000,y=0)
frame_cadprof.propagate(0)
ent_nome_p = Entry(frame_cadprof, font="arial 15")
ent_nome_p.place(x=110,y=55)
mensnome = Label(frame_cadprof, text='nome:', font='System 16 bold', bg='orangered4',
                     fg='black')
mensnome.place(x=60, y=60)
ent_cpf_p = Entry(frame_cadprof, font="arial 15")
ent_cpf_p.place(x=110, y=95)
menscpf = Label(frame_cadprof, text='cpf:', font='System 16 bold', bg='orangered4',
                     fg='black')
menscpf.place(x=70, y=100)
ent_dep_p = Entry(frame_cadprof, font="arial 15")
ent_dep_p.place(x=110,y=135)
mensdep = Label(frame_cadprof, text='Departamento:', font='System 16 bold', bg='orangered4',
                    fg='black')
mensdep.place(x=0, y=140)
mensagemcadprof = Label(frame_cadprof, text='Cadastro de Professor', font='System 25 bold', bg='orangered4',
                          fg='yellow2')
mensagemcadprof.place(x=80, y=5)
bvoltar_prof = Button(frame_cadprof, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                        command=voltar_prof)
bvoltar_prof.place(x=140, y=190)
bcadastrarP = Button(frame_cadprof, width=15, height=2, text='Cadastrar', bg='grey', fg='yellow2', font='System 10',command=bd_cadprof)
bcadastrarP.place(x=350, y=90)

#frame cadastro disc

frame_cad_disc = Frame(janela,width=800,height=550,bg='orangered4')
frame_cad_disc.place(x=9000,y=0)
frame_cad_disc.propagate(0)

ent_nome_d = Entry(frame_cad_disc, font="arial 15")
ent_nome_d.place(x=90, y=55)
mensnome = Label(frame_cad_disc, text='nome:', font='System 16 bold', bg='orangered4',
                     fg='black')
mensnome.place(x=40, y=60)
ent_código_d = Entry(frame_cad_disc, font="arial 15")
ent_código_d.place(x=90, y=95)
menscod = Label(frame_cad_disc, text='Código:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscod.place(x=35, y=100)
mensagemcaddisc = Label(frame_cad_disc, text='Cadastro de Disciplina', font='System 25 bold', bg='orangered4',
                          fg='yellow2')
mensagemcaddisc.place(x=80, y=5)
bvoltar_disc = Button(frame_cad_disc, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_disc)
bvoltar_disc.place(x=130, y=140)
bcadastrard = Button(frame_cad_disc, width=15, height=2, text='Cadastrar', bg='grey', fg='yellow2', font='System 10',command=bd_caddisc)
bcadastrard.place(x=330, y=70)

#frame cadastro turma

frame_cadturma = Frame(janela,width=800,height=550,bg='orangered4')
frame_cadturma.place(x=9000,y=0)
frame_cadturma.propagate(0)
ent_cod_t = Entry(frame_cadturma, font="arial 15")
ent_cod_t.place(x=180, y=55)
menscodigo = Label(frame_cadturma, text='Código da turma:', font='System 16 bold', bg='orangered4',
                     fg='black')
menscodigo.place(x=60, y=60)
ent_per = Entry(frame_cadturma, font="arial 15")
ent_per.place(x=180, y=95)
mensper = Label(frame_cadturma, text='Período:', font='System 16 bold', bg='orangered4',
                    fg='black')
mensper.place(x=110, y=100)
ent_cod_disc = Entry(frame_cadturma, font="arial 15")
ent_cod_disc.place(x=180, y=135)
menscodd = Label(frame_cadturma, text='Código da Disciplina:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscodd.place(x=30, y=140)
ent_cpfal = Entry(frame_cadturma, font="arial 15")
ent_cpfal.place(x=180, y=175)
menscpfal = Label(frame_cadturma, text='Cpf do Aluno:', font='System 16 bold', bg='orangered4',
                     fg='black')
menscpfal.place(x=80, y=180)
ent_cpfprof = Entry(frame_cadturma, font="arial 15")
ent_cpfprof.place(x=180, y=215)
menscpfprof = Label(frame_cadturma, text='Cpf do Professsor:', font='System 16 bold', bg='orangered4',
                      fg='black')
menscpfprof.place(x=50, y=220)
mensagemcadturma = Label(frame_cadturma, text='Cadastro de Turma', font='System 25 bold', bg='orangered4',
                          fg='yellow2')
mensagemcadturma.place(x=170, y=5)
bvoltar_turma = Button(frame_cadturma, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_turma)
bvoltar_turma.place(x=220, y=260)
bcadastrart = Button(frame_cadturma, width=15, height=2, text='Cadastrar', bg='grey', fg='yellow2', font='System 10',command=bd_cadturma)
bcadastrart.place(x=430, y=110)

binserir_a = Button(frame_cadturma, width=17, height=1, text='inserir aluno', bg='grey', fg='yellow2', font='System 10',command=inserir_al
                          )
binserir_a.place(x=430,y=185)

binserir_p = Button(frame_cadturma, width=17, height=1, text='inserir professor', bg='grey', fg='yellow2', font='System 10',command=inserir_prof
                          )
binserir_p.place(x=430,y=220)
#frame consulta aluno

frame_conalu = Frame(janela,width=800,height=550,bg='orangered4')
frame_conalu.place(x=9000,y=0)
frame_conalu.propagate(0)

listaa= Listbox(frame_conalu,width=40,height=15,bg='grey')
listaa.place(x=200,y=100)
mensagemc = Label(frame_conalu, text='Consulta\nde\nAluno: ', font='System 25 bold', bg='orangered4',
                     fg='yellow2')
mensagemc.place(x=50, y=150)
bvoltar_al1 = Button(frame_conalu, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                         command=voltar_principal_a1)
bvoltar_al1.place(x=520, y=200)

ent_cpf_c = Entry(frame_conalu, font="arial 15")
ent_cpf_c.place(x=205, y=50)
menscpf_c = Label(frame_conalu, text='cpf:', font='System 18 bold', bg='orangered4',
                    fg='black')
menscpf_c.place(x=140, y=45)
consultac = Button(frame_conalu, width=15, height=2, text='Consultar', bg='grey', fg='yellow2', font='System 10',
                         command=consulta_al_ex)
consultac.place(x=450, y=45)


#frame consulta professor

frame_conprof = Frame(janela,width=800,height=550,bg='orangered4')
frame_conprof.place(x=9000,y=0)
frame_conprof.propagate(0)

listap= Listbox(frame_conprof,width=40,height=15,bg='grey')
listap.place(x=200,y=100)
mensagemcp = Label(frame_conprof, text='Consulta\nde\nProfessor: ', font='System 25 bold', bg='orangered4',
                     fg='yellow2')
mensagemcp.place(x=50, y=150)
bvoltar_p1 = Button(frame_conprof, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                         command=voltar_principal_p1)
bvoltar_p1.place(x=520, y=200)

ent_cpf_p2 = Entry(frame_conprof, font="arial 15")
ent_cpf_p2.place(x=205, y=50)
menscpf_p = Label(frame_conprof, text='cpf:', font='System 18 bold', bg='orangered4',
                    fg='black')
menscpf_p.place(x=140, y=45)
consultap1 = Button(frame_conprof, width=15, height=2, text='Consultar', bg='grey', fg='yellow2', font='System 10',
                         command=consulta_prof_ex)
consultap1.place(x=450, y=45)


#frame consulta disciplina

frame_condisc = Frame(janela,width=800,height=550,bg='orangered4')
frame_condisc.place(x=9000,y=0)
frame_condisc.propagate(0)
listad= Listbox(frame_condisc,width=40,height=15,bg='grey')
listad.place(x=200,y=100)
mensagemcd = Label(frame_condisc, text='Consulta\nde\nDisciplina: ', font='System 25 bold', bg='orangered4',
                     fg='yellow2')
mensagemcd.place(x=50, y=150)
bvoltar_d1 = Button(frame_condisc, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_principal_d1)
bvoltar_d1.place(x=520, y=200)

ent_cod_di = Entry(frame_condisc, font="arial 15")
ent_cod_di.place(x=205, y=50)
menscod_d = Label(frame_condisc, text='Código:', font='System 18 bold', bg='orangered4',
                    fg='black')
menscod_d.place(x=100, y=45)
consultac = Button(frame_condisc, width=15, height=2, text='Consultar', bg='grey', fg='yellow2', font='System 10',
                         command=consulta_d_ex)
consultac.place(x=450, y=45)

#frame consulta turma

frame_conturma = Frame(janela,width=800,height=550,bg='orangered4')
frame_conturma.place(x=9000,y=0)
frame_conturma.propagate(0)

listat= Listbox(frame_conturma,width=60,height=15,bg='grey')
listat.place(x=200,y=100)
mensagemcd = Label(frame_conturma, text='Consulta\nde\nturma: ', font='System 25 bold', bg='orangered4',
                     fg='yellow2')
mensagemcd.place(x=50, y=150)
bvoltar_t1 = Button(frame_conturma, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                        command=voltar_principal_t1)
bvoltar_t1.place(x=620, y=200)

ent_codt_tu = Entry(frame_conturma, font="arial 15")
ent_codt_tu.place(x=205, y=50)
menscodt_t = Label(frame_conturma, text='Código:', font='System 18 bold', bg='orangered4',
                    fg='black')
menscodt_t.place(x=100, y=45)
consultat1 = Button(frame_conturma, width=15, height=2, text='Consultar', bg='grey', fg='yellow2', font='System 10',
                         command=consulta_t_ex)
consultat1.place(x=450, y=45)


#frane atualizar aluno
frame_att_al= Frame(janela,width=800,height=550,bg='orangered4')
frame_att_al.place(x=9000,y=0)
frame_att_al.propagate(0)

bvoltar_alu = Button(frame_att_al, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_all)
bvoltar_alu.place(x=310, y=280)

bverificar = Button(frame_att_al, width=15, height=2, text='Verificar', bg='grey', fg='yellow2', font='System 10',command=att_al,
                          )
bverificar.place(x=420, y=60)

mensagem_cpf = Label(frame_att_al, text='Digite o cpf do aluno para atualizar:', font='System 17 bold',bg='orangered4',fg='yellow2')
mensagem_cpf.place(x=150,y=5)

ent_cpf_a = Entry(frame_att_al, font="arial 15")
ent_cpf_a.place(x=180, y=70)

menscpf_att = Label(frame_att_al, text='CPF:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscpf_att.place(x=130, y=75)

mensagem_newd = Label(frame_att_al, text='Digite os novos dados:', font='System 18 bold',bg='orangered4',fg='yellow2')
mensagem_newd.place(x=150,y=130)


new_nome_a = Entry(frame_att_al, font="arial 15")
new_nome_a.place(x=180, y=180)

mens_newnome = Label(frame_att_al, text='Nome:', font='System 16 bold', bg='orangered4',
                    fg='black')
mens_newnome.place(x=130, y=180)

new_cpf_a = Entry(frame_att_al, font="arial 15")
new_cpf_a.place(x=180, y=220)

mens_newcpf = Label(frame_att_al, text='CPF:', font='System 16 bold', bg='orangered4',
                    fg='black')
mens_newcpf.place(x=130, y=220)

batualizara = Button(frame_att_al, width=15, height=2, text='Atualizar', bg='grey', fg='yellow2', font='System 10',command=atuala)
batualizara.place(x=160, y=280)

listaal= Listbox(frame_att_al,width=40,height=15,bg='grey')
listaal.place(x=500,y=170)

bmostrar = Button(frame_att_al, width=15, height=2, text='Mostrar alunos', bg='grey', fg='yellow2', font='System 10',command=consulta_al_att)
bmostrar.place(x=560, y=440)


#frame atualizar professor

frame_att_prof = Frame(janela,width=800,height=550,bg='orangered4')
frame_att_prof.place(x=9000,y=0)
frame_att_prof.propagate(0)

bvoltar_pro = Button(frame_att_prof, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_pro)
bvoltar_pro.place(x=320, y=320)

bverificarp = Button(frame_att_prof, width=15, height=2, text='Verificar', bg='grey', fg='yellow2', font='System 10',command=att_prof
                          )
bverificarp.place(x=420, y=60)

mensagem_cpfp = Label(frame_att_prof, text='Digite o cpf do Professor para atualizar:', font='System 17 bold',bg='orangered4',fg='yellow2')
mensagem_cpfp.place(x=150,y=5)

ent_cpf_p1 = Entry(frame_att_prof, font="arial 15")
ent_cpf_p1.place(x=180, y=70)

menscpf_attp = Label(frame_att_prof, text='CPF:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscpf_attp.place(x=130, y=75)

ent_dep_prof = Entry(frame_att_prof, font="arial 15")
ent_dep_prof.place(x=180, y=260)

mensdep_attp = Label(frame_att_prof, text='departamento:', font='System 16 bold', bg='orangered4',
                    fg='black')
mensdep_attp.place(x=70, y=260)


mensagem_newdp = Label(frame_att_prof, text='Digite os novos dados:', font='System 18 bold',bg='orangered4',fg='yellow2')
mensagem_newdp.place(x=150,y=130)


new_nome_p = Entry(frame_att_prof, font="arial 15")
new_nome_p.place(x=180, y=180)

mens_newnomep = Label(frame_att_prof, text='Nome:', font='System 16 bold', bg='orangered4',
                    fg='black')
mens_newnomep.place(x=130, y=180)

new_cpf_p = Entry(frame_att_prof, font="arial 15")
new_cpf_p.place(x=180, y=220)

mens_newcpfp = Label(frame_att_prof, text='CPF:', font='System 16 bold', bg='orangered4',
                    fg='black')
mens_newcpfp.place(x=130, y=220)

batualizarp = Button(frame_att_prof, width=15, height=2, text='Atualizar', bg='grey', fg='yellow2', font='System 10',command=atualp)
batualizarp.place(x=160, y=320)

listaprof1= Listbox(frame_att_prof,width=40,height=15,bg='grey')
listaprof1.place(x=500,y=170)

bmostrarp = Button(frame_att_prof, width=17, height=2, text='Mostrar Professores', bg='grey', fg='yellow2', font='System 10',command=consulta_att_p)
bmostrarp.place(x=560, y=440)

#frame atualizar turma

frame_att_turma = Frame(janela,width=800,height=550,bg='orangered4')
frame_att_turma.place(x=9000,y=0)
frame_att_turma.propagate(0)

bvoltar_turm = Button(frame_att_turma, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_turm)
bvoltar_turm.place(x=220, y=440)

menscodigo = Label(frame_att_turma, text='Código da turma:', font='System 16 bold', bg='orangered4',
                     fg='black')
menscodigo.place(x=60, y=60)
ent_codt_at = Entry(frame_att_turma, font="arial 15")
ent_codt_at.place(x=180, y=60)
ent_per_at = Entry(frame_att_turma, font="arial 15")
ent_per_at.place(x=180, y=95)
mensper = Label(frame_att_turma, text='Período:', font='System 16 bold', bg='orangered4',
                    fg='black')
mensper.place(x=110, y=100)
ent_codd_at = Entry(frame_att_turma, font="arial 15")
ent_codd_at.place(x=180, y=135)
menscodd = Label(frame_att_turma, text='Código da Disciplina:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscodd.place(x=30, y=140)
ent_cpfalatt = Entry(frame_att_turma, font="arial 15")
ent_cpfalatt.place(x=180, y=175)
menscpfal = Label(frame_att_turma, text='Cpf do Aluno:', font='System 16 bold', bg='orangered4',
                     fg='black')
menscpfal.place(x=80, y=180)
ent_cpfprofatt = Entry(frame_att_turma, font="arial 15")
ent_cpfprofatt.place(x=180, y=215)
menscpfprof = Label(frame_att_turma, text='Cpf do Professsor:', font='System 16 bold', bg='orangered4',
                      fg='black')
menscpfprof.place(x=50, y=220)

ent_newcpfal = Entry(frame_att_turma, font="arial 15")
ent_newcpfal.place(x=180, y=260)
mensnewcpfal = Label(frame_att_turma, text='novo cpf do aluno:', font='System 16 bold', bg='orangered4',
                      fg='black')
mensnewcpfal.place(x=30, y=260)

ent_newcpfprof = Entry(frame_att_turma, font="arial 15")
ent_newcpfprof.place(x=180, y=300)
mensnewcpfprof = Label(frame_att_turma, text='novo cpf do professor:', font='System 16 bold', bg='orangered4',
                      fg='black')
mensnewcpfprof.place(x=20, y=300)

mensagemcadturma = Label(frame_att_turma, text='Cadastro de Turma', font='System 25 bold', bg='orangered4',
                          fg='yellow2')
mensagemcadturma.place(x=170, y=5)
bcadastrart = Button(frame_att_turma, width=15, height=2, text='ATUALIZAR', bg='grey', fg='yellow2', font='System 10',command=atualt)
bcadastrart.place(x=430, y=110)

binserir_a = Button(frame_att_turma, width=17, height=1, text='Atualizar aluno', bg='grey', fg='yellow2', font='System 10',command=att_cpf_al
                          )
binserir_a.place(x=430,y=185)

binserir_p = Button(frame_att_turma, width=17, height=1, text='Atualizar professor', bg='grey', fg='yellow2', font='System 10',command=att_cpf_prof
                          )
binserir_p.place(x=430,y=220)

ent_cod_att = Entry(frame_att_turma, font="arial 15")
ent_cod_att.place(x=180, y=390)

menscodatt = Label(frame_att_turma, text='Código da Disciplina:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscodatt.place(x=30, y=395)
menscodatt1 = Label(frame_att_turma, text='Insira o código da disciplina que você quer atualizar:', font='System 17 bold', bg='orangered4',
                    fg='yellow2')
menscodatt1.place(x=40, y=350)

bremover_p = Button(frame_att_turma, width=17, height=1, text='Remover professor', bg='grey', fg='yellow2', font='System 10',command=remover_prof_att
                          )
bremover_p.place(x=600,y=220)

bremover_a = Button(frame_att_turma, width=17, height=1, text='Remover aluno', bg='grey', fg='yellow2', font='System 10',command=remover_al_att
                          )
bremover_a.place(x=600,y=185)

bmostrar_t = Button(frame_att_turma, width=17, height=1, text='Mostrar turma', bg='grey', fg='yellow2', font='System 10',command=mostrar_t
                          )
bmostrar_t.place(x=430,y=390)


#frame atualizar disciplina

frame_att_disc = Frame(janela,width=800,height=550,bg='orangered4')
frame_att_disc.place(x=9000,y=0)
frame_att_disc.propagate(0)

bvoltar_dis = Button(frame_att_disc, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_dis)
bvoltar_dis.place(x=320, y=260)

bverificard = Button(frame_att_disc, width=15, height=2, text='Verificar', bg='grey', fg='yellow2', font='System 10',command=att_disc
                          )
bverificard.place(x=420, y=60)

mensagem_codd = Label(frame_att_disc, text='Digite o Código da Disciplina para atualizar:', font='System 17 bold',bg='orangered4',fg='yellow2')
mensagem_codd.place(x=150,y=5)

ent_cod_d = Entry(frame_att_disc, font="arial 15")
ent_cod_d.place(x=180, y=70)

menscod_att = Label(frame_att_disc, text='Código:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscod_att.place(x=118, y=75)

mensagem_newdd = Label(frame_att_disc, text='Digite os novos dados:', font='System 18 bold',bg='orangered4',fg='yellow2')
mensagem_newdd.place(x=150,y=130)


new_nome_d = Entry(frame_att_disc, font="arial 15")
new_nome_d.place(x=180, y=180)

mens_newdi = Label(frame_att_disc, text='Nome:', font='System 16 bold', bg='orangered4',
                    fg='black')
mens_newdi.place(x=130, y=180)

new_cod = Entry(frame_att_disc, font="arial 15")
new_cod.place(x=180, y=220)

mens_newcod = Label(frame_att_disc, text='Código:', font='System 16 bold', bg='orangered4',
                    fg='black')
mens_newcod.place(x=120, y=220)

batualizard = Button(frame_att_disc, width=15, height=2, text='Atualizar', bg='grey', fg='yellow2', font='System 10',command=atuald)
batualizard.place(x=160, y=260)

listad1= Listbox(frame_att_disc,width=40,height=15,bg='grey')
listad1.place(x=500,y=170)

bmostrard = Button(frame_att_disc, width=18, height=2, text='Mostrar disciplinas', bg='grey', fg='yellow2', font='System 10',command=consulta_disc_att)
bmostrard.place(x=560, y=440)

#frame deletar aluno

frame_del_al=Frame(janela,width=800,height=550,bg='orangered4')
frame_del_al.place(x=9000,y=0)
frame_del_al.propagate(0)

bvoltar_allu = Button(frame_del_al, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_allu)
bvoltar_allu.place(x=300, y=240)

ent_del_cpf = Entry(frame_del_al, font="arial 15")
ent_del_cpf.place(x=180, y=180)

malu= Listbox(frame_del_al,width=40,height=15,bg='grey')
malu.place(x=500,y=170)

mensagem_del = Label(frame_del_al, text='Remover Alunos:', font='System 17 bold',bg='orangered4',fg='yellow2')
mensagem_del.place(x=180,y=10)

mensagem_delcpf = Label(frame_del_al, text='Digite o cpf do aluno que você deseja remover:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagem_delcpf.place(x=150,y=140)

mensagem_delcpf1 = Label(frame_del_al, text='CPF:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagem_delcpf1.place(x=130,y=180)

bmostra_a = Button(frame_del_al, width=15, height=2, text='Mostrar Aluno', bg='grey', fg='yellow2', font='System 10',
                          command=consulta_a_del)
bmostra_a.place(x=550, y=440)

bremovera = Button(frame_del_al, width=15, height=2, text='Remover', bg='grey', fg='yellow2', font='System 10',command=remover_al)
bremovera.place(x=150, y=240)


#frame deletar professor

frame_del_prof=Frame(janela,width=800,height=550,bg='orangered4')
frame_del_prof.place(x=9000,y=0)
frame_del_prof.propagate(0)

bvoltar_proff = Button(frame_del_prof, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_proff)
bvoltar_proff.place(x=320, y=240)

ent_del_cpfp = Entry(frame_del_prof, font="arial 15")
ent_del_cpfp.place(x=180, y=180)

mprof= Listbox(frame_del_prof,width=40,height=15,bg='grey')
mprof.place(x=500,y=170)

mensagem_delp = Label(frame_del_prof, text='Remover Professores:', font='System 17 bold',bg='orangered4',fg='yellow2')
mensagem_delp.place(x=180,y=10)

mensagem_delcpfp = Label(frame_del_prof, text='Digite o cpf do professor que você deseja remover:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagem_delcpfp.place(x=150,y=140)

mensagem_delcpf2 = Label(frame_del_prof, text='CPF:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagem_delcpf2.place(x=130,y=180)

bmostra_p = Button(frame_del_prof, width=18, height=2, text='Mostrar Professor', bg='grey', fg='yellow2', font='System 10',
                          command=consulta_p_del)
bmostra_p.place(x=550, y=440)

bremoverp = Button(frame_del_prof, width=15, height=2, text='Remover', bg='grey', fg='yellow2', font='System 10',command=remover_prof)
bremoverp.place(x=150, y=240)

#frame deletar disciplina

frame_del_disc=Frame(janela,width=800,height=550,bg='orangered4')
frame_del_disc.place(x=9000,y=0)
frame_del_disc.propagate(0)

bvoltar_discc = Button(frame_del_disc, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_discc)
bvoltar_discc.place(x=320, y=220)

ent_del_cod1 = Entry(frame_del_disc, font="arial 15")
ent_del_cod1.place(x=180, y=180)

mdisc= Listbox(frame_del_disc,width=40,height=15,bg='grey')
mdisc.place(x=500,y=170)

mensagem_deld = Label(frame_del_disc, text='Remover Disciplinas:', font='System 17 bold',bg='orangered4',fg='yellow2')
mensagem_deld.place(x=180,y=10)

mensagem_delcod = Label(frame_del_disc, text='Digite o código da disciplina que você deseja remover:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagem_delcod.place(x=150,y=140)

mensagem_delcod1 = Label(frame_del_disc, text='Código:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagem_delcod1.place(x=118,y=180)

bmostra_d = Button(frame_del_disc, width=18, height=2, text='Mostrar Disciplinas', bg='grey', fg='yellow2', font='System 10',
                          command=consulta_d_del)
bmostra_d.place(x=550, y=440)

bremoverd = Button(frame_del_disc, width=15, height=2, text='Remover', bg='grey', fg='yellow2', font='System 10',command=remover_disc)
bremoverd.place(x=150, y=220)

#frame deletar turma

frame_del_turma=Frame(janela,width=800,height=550,bg='orangered4')
frame_del_turma.place(x=9000,y=0)
frame_del_turma.propagate(0)

bvoltar_turmm = Button(frame_del_turma, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_turmm)
bvoltar_turmm.place(x=300, y=240)

ent_del_cod = Entry(frame_del_turma, font="arial 15")
ent_del_cod.place(x=180, y=180)

mt1= Listbox(frame_del_turma,width=40,height=15,bg='grey')
mt1.place(x=500,y=170)

mensagem_delt = Label(frame_del_turma, text='Remover Turmas:', font='System 17 bold',bg='orangered4',fg='yellow2')
mensagem_delt.place(x=180,y=10)

mensagem_delcodt = Label(frame_del_turma, text='Digite o código da turma que você deseja remover:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagem_delcodt.place(x=150,y=140)

mensagem_delcodt1 = Label(frame_del_turma, text='Código:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagem_delcodt1.place(x=120,y=180)

bmostra_t1 = Button(frame_del_turma, width=15, height=2, text='Mostrar Turma', bg='grey', fg='yellow2', font='System 10',
                          command=consulta_t_del)
bmostra_t1.place(x=550, y=440)

bremovert = Button(frame_del_turma, width=15, height=2, text='Remover', bg='grey', fg='yellow2', font='System 10',command=remover_t)
bremovert.place(x=150, y=240)

#frame relatório aluno

frame_relatorioal= Frame(janela,width=800,height=550,bg='orangered4')
frame_relatorioal.place(x=9000,y=0)
frame_relatorioal.propagate(0)

bvoltar_relal = Button(frame_relatorioal, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_relal)
bvoltar_relal.place(x=600, y=110)

ent_cpf_ar = Entry(frame_relatorioal, font="arial 15")
ent_cpf_ar.place(x=180, y=80)

menscpfr = Label(frame_relatorioal, text='CPF:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscpfr.place(x=130, y=80)

mensagemracpf = Label(frame_relatorioal, text='Relatório Geral:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagemracpf.place(x=210,y=40)

ent_per_ar = Entry(frame_relatorioal, font="arial 15")
ent_per_ar.place(x=180, y=160)

mensper = Label(frame_relatorioal, text='CPF:', font='System 16 bold', bg='orangered4',
                    fg='black')
mensper.place(x=130, y=160)


mensagemraper = Label(frame_relatorioal, text='Relatório Por período:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagemraper.place(x=210,y=120)

listaral= Listbox(frame_relatorioal,width=40,height=15,bg='grey')
listaral.place(x=250,y=250)

bmostra_rga = Button(frame_relatorioal, width=16, height=2, text='Pesquisar', bg='grey', fg='yellow2', font='System 10',command=consulta_al_geral
                          )
bmostra_rga.place(x=430, y=70)

bmostra_rpa = Button(frame_relatorioal, width=16, height=2, text='Pesquisar', bg='grey', fg='yellow2', font='System 10',command=consulta_al_per
                          )
bmostra_rpa.place(x=430, y=160)

#frame relatório professor

frame_relatorioprof= Frame(janela,width=800,height=550,bg='orangered4')
frame_relatorioprof.place(x=9000,y=0)
frame_relatorioprof.propagate(0)

bvoltar_relprof = Button(frame_relatorioprof, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_relprof)
bvoltar_relprof.place(x=600, y=110)

ent_cpf_pr = Entry(frame_relatorioprof, font="arial 15")
ent_cpf_pr.place(x=180, y=80)

menscpfrp = Label(frame_relatorioprof, text='CPF:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscpfrp.place(x=130, y=80)

mensagemrpcpf = Label(frame_relatorioprof, text='Relatório Geral:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagemrpcpf.place(x=210,y=40)

ent_per_pr = Entry(frame_relatorioprof, font="arial 15")
ent_per_pr.place(x=180, y=160)

mensperp = Label(frame_relatorioprof, text='CPF:', font='System 16 bold', bg='orangered4',
                    fg='black')
mensperp.place(x=130, y=160)


mensagemrpper = Label(frame_relatorioprof, text='Relatório Por período:', font='System 16 bold',bg='orangered4',fg='yellow2')
mensagemrpper.place(x=210,y=120)

listarp= Listbox(frame_relatorioprof,width=40,height=15,bg='grey')
listarp.place(x=250,y=250)

bmostra_rgp = Button(frame_relatorioprof, width=16, height=2, text='Pesquisar', bg='grey', fg='yellow2', font='System 10',command=consulta_prof_geral
                          )
bmostra_rgp.place(x=430, y=70)

bmostra_rpp = Button(frame_relatorioprof, width=16, height=2, text='Pesquisar', bg='grey', fg='yellow2', font='System 10',command=consulta_prof_per
                          )
bmostra_rpp.place(x=430, y=160)


#frame ata

frame_ata= Frame(janela,width=800,height=550,bg='orangered4')
frame_ata.place(x=9000,y=0)
frame_ata.propagate(0)

bvoltar_ata = Button(frame_ata, width=15, height=2, text='Voltar', bg='grey', fg='yellow2', font='System 10',
                          command=voltar_ata)
bvoltar_ata.place(x=630, y=400)

ent_codt = Entry(frame_ata, font="arial 15")
ent_codt.place(x=180, y=100)

menscodt = Label(frame_ata, text='Código da Turma:', font='System 16 bold', bg='orangered4',
                    fg='black')
menscodt.place(x=20, y=100)

listaata= Listbox(frame_ata,width=85,height=20,bg='grey')
listaata.place(x=80,y=200)

bmostra_ata = Button(frame_ata, width=16, height=2, text='Pesquisar', bg='grey', fg='yellow2', font='System 10',command=ata1
                          )
bmostra_ata.place(x=460, y=100)

janela.mainloop()
