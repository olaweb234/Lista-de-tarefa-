import customtkinter

def nova():
    # Cria um novo frame para a tarefa
    frame = customtkinter.CTkFrame(janela, bg_color='white')
    frame.pack(padx=20, pady=10, fill='x')

    # Cria uma entrada de texto para a tarefa
    nova_tarefa = customtkinter.CTkEntry(frame, placeholder_text='SUA TAREFA' )
    nova_tarefa.pack(side='left', padx=5, pady=5)

    check = customtkinter.CTkCheckBox(frame, text='Concluída', text_color='green')
    check.pack(side='left', pady=20, padx=20)


    # Cria um botão para remover a tarefa
    remover_botao = customtkinter.CTkButton(frame, text='Remover', command=lambda: remover(frame))
    remover_botao.pack(side='right', padx=5, pady=5)

def remover(frame):
    # Destroi o frame da tarefa
    frame.destroy()

def resetar():
    print('ola')

janela = customtkinter.CTk()
janela.geometry('500x300')

texto1 = customtkinter.CTkLabel(janela, text='GERADOR DE TAREFA')
texto1.pack(pady=20)

nova_tarefa = customtkinter.CTkButton(janela, text='NOVA TAREFA', command=nova)
nova_tarefa.pack(pady=10)

rest = customtkinter.CTkButton(janela, text='RESETAR AS TAREFAS', command=resetar)
rest.pack(pady=10)

janela.mainloop()


