class Pybank:
    def __init__(self):
        self.dados_usuario = []
        self.logado = False
        self.saldo = 0
        self.boolean_saq = False

    def cadastro(self, nome , usuario, senha, saldo):

        self.dados_usuario = [nome, usuario, senha, saldo]
        with open(f'{nome}','w') as f:
            for dados in self.dados_usuario:
                f.write(str(dados)+'\n')

    def login(self,nome, usuario, senha):
        with open(f'{nome}','r') as f:
            dados = f.read()
            self.dados_usuario = dados.split('\n')
            if str(usuario) in str(self.dados_usuario):
                if str(senha) in str(self.dados_usuario):
                    self.logado = True
                else:
                    self.logado = False
            else:
                self.logado = False



            if self.logado == True:
                self.saldo = int(self.dados_usuario[3]) 
                self.nome = nome
                print('Usuario logado')
                
            
    
    def depositar(self,valor_deposito,nome):
        
        
            self.saldo = self.saldo + valor_deposito
            with open(f'{nome}','r') as f:
                dados = f.read()
                self.dados_usuario = dados.split('\n')
            with open(f"{nome}","w") as f:
                f.write(dados.replace(str(self.dados_usuario[3]),str(self.saldo)))
            print('Saldo adicionado com sucesso')

    def transferir(self,valor_transferencia, nome_destino):
        with open(f"{nome_destino}","r") as f:
            dados = f.read()
            self.dados_usuario = dados.split("\n")
        saldo_total = int(self.dados_usuario[3]) + valor_transferencia
        saldo_sobra = self.saldo - valor_transferencia
        with open(f"{nome_destino}","w") as f:
                f.write(dados.replace(str(self.dados_usuario[3]),str(saldo_total)))
        with open(f"{self.nome}","r") as f:
                dados_2 = f.read()
                self.dados_usuario = dados.split("\n")
        with open(f"{self.nome}","w") as f:
                f.write(dados_2.replace(str(self.dados_usuario[3]),str(saldo_sobra)))

    def sacar(self,valor_saque,nome):
        self.nome = nome
        with open(f'{self.nome}',"r") as f:
                dados = f.read()
                self.dados_usuario = dados.split('\n')
        self.saldo = int(self.dados_usuario[3])
        if valor_saque > self.saldo:
            self.boolean_saq = False
            
        else:
            self.boolean_saq = True
            balanco = self.saldo - valor_saque
            with open(f"{self.nome}","w") as f:
                f.write(dados.replace(str(self.dados_usuario[3]),str(balanco)))
            print('Saque efetivado!')
       
    def atualizar_saldo(self):
        with open(f'{self.nome}',"r") as f:
                dados = f.read()
                self.dados_usuario = dados.split('\n')        
        self.saldo = self.dados_usuario[3]





        
        
    








    


        

    
    

    




        







