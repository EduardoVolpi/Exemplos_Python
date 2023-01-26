import os
import platform
import random
import sys
from datetime import datetime  # Para datas e horas

from PySide6.QtCore import QLibraryInfo, QSize, Qt, QTranslator
from PySide6.QtWidgets import (QApplication, QColorDialog, QFileDialog,
                               QFontDialog, QInputDialog, QMainWindow,
                               QMessageBox, QWidget)

import funcoes
from interfaces.ui_mainwindow import Ui_MainWindow
from interfaces.ui_segundoform import Ui_frmSegundoForm

"""
Begin Class SegundoForm
"""


class SegundoForm(QWidget, Ui_frmSegundoForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setMaximumSize(390, 244)
        # self.setMinimumSize(390, 244)
        self.setFixedSize(QSize(390, 244))

        # tem que importar Qt from PySide6.QtCore
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Teste Segundo Form")
        """
        Widgets
        """

        """
        Signals/Slots
        """
        self.btnSegFormClose.clicked.connect(self.btn_segform_close_clicked)

        """
        Functions/Actions
        """

    def btn_segform_close_clicked(self):
        self.close()


"""
End Class SegundoForm
"""

"""
Begin Class MainWindows
"""


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Para Fixar Tamanho da Janela'''
        self.setMaximumSize(QSize(952, 555))
        self.setMinimumSize(QSize(952, 555))
        """
        Widgets
        """
        # Desabilitado pois só o exemplo no código basta
        self.btnCriarPastas.setEnabled(False)
        """
        Signals/Slots
        """
        # Menu Sair
        self.action_Sair.triggered.connect(self.close)
        # Botões Caixas de Diálogo
        self.btnDialogCustom.clicked.connect(self.btn_dialog_custom_clicked)
        self.btnDialogSobre.clicked.connect(self.btn_dialog_sobre_clicked)
        self.btnDialogSobreQt.clicked.connect(self.btn_dialog_sobre_qt_clicked)
        self.btnDialogInfo.clicked.connect(self.btn_dialog_info_clicked)
        self.btnDialogErro.clicked.connect(self.btn_dialog_erro_clicked)
        self.btnDialogAlerta.clicked.connect(self.btn_dialog_alerta_clicked)
        self.btnDialogQuestao.clicked.connect(self.btn_dialog_questao_clicked)
        self.btnInputText.clicked.connect(self.btn_input_text_clicked)
        self.btnInputInt.clicked.connect(self.btn_input_int_clicked)
        self.btnInputDouble.clicked.connect(self.btn_input_double_clicked)
        self.btnInputItem.clicked.connect(self.btn_input_item_clicked)
        self.btnAbrirArquivo.clicked.connect(self.btn_abrir_arquivo_clicked)
        self.btnSalvarArquivo.clicked.connect(self.btn_salvar_arquivo_clicked)
        self.btnEscolherPasta.clicked.connect(self.btn_escolher_pasta_clicked)
        self.btnDialogFonts.clicked.connect(self.btn_dialog_fonts_clicked)
        self.btnDialogColors.clicked.connect(self.btn_dialog_colors_clicked)
        # Botões Pastas e Arquivos
        self.btnGravarArquivo.clicked.connect(self.btn_gravar_arquivo_clicked)
        self.btnLerArquivo.clicked.connect(self.btn_ler_arquivo_clicked)
        self.btnExcluirArquivo.clicked.connect(self.btn_excluir_arquivo_clicked)
        self.btnRenomearAP.clicked.connect(self.btn_renomear_ap_clicked)
        self.btnPastaHome.clicked.connect(self.btn_pasta_home_clicked)
        self.btnPastaDocuments.clicked.connect(self.btn_pasta_documents_cliked)
        self.btnPastaAtual.clicked.connect(self.btn_pasta_atual_clicked)
        self.btnCriarPasta.clicked.connect(self.btn_criar_pasta_clicked)
        self.btnCriarPastas.clicked.connect(self.btn_criar_pastas_clicked)
        self.btnExcluirPasta.clicked.connect(self.btn_excluir_pastas_clicked)
        self.btnListDir.clicked.connect(self.btn_list_dir_clicked)
        # Botões Para Random
        self.btnRandUniform.clicked.connect(self.btn_rand_uniform_clicked)
        self.btnRandInt.clicked.connect(self.btn_rand_int_clicked)
        self.btnRandChoices.clicked.connect(self.btn_rand_choices_clicked)
        self.btnRandChoices2.clicked.connect(self.btn_rand_choices2_clicked)
        self.btnRandShuffle.clicked.connect(self.btn_rand_shuffle_clicked)
        self.btnRandSample.clicked.connect(self.btn_rand_sample_clicked)
        # Botões Para Outros
        self.btnLoterias.clicked.connect(self.btn_loterias_clicked)
        self.btnSistemaOperacional.clicked.connect(self.btn_sistema_operacional_clicked)
        self.btnDataHoraSistema.clicked.connect(self.btn_data_hora_sistema_clicked)
        self.btnAbrirSegundoForm.clicked.connect(self.btn_abrir_segundo_form_clicked)
        # Botões Para Testes
        self.btnParaTestes.clicked.connect(self.btn_para_testes_clicked)

        # Inicia Outros Forms Aqui - Depois é só utilizar o metodo .show() para abrir
        self.segundo_form = SegundoForm()  # Ui importada acima e classe definida acima

    """
    Functions/Actions
    """

    def btn_dialog_custom_clicked(self):
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle("Título de Exemplo")
        dialogo.setText("Este é o texto da caixa de diálogo\nDeseja Sair?")
        dialogo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dialogo.button(QMessageBox.Ok).setText("Botão 1: OK")
        dialogo.button(QMessageBox.Cancel).setText("Botão 2: Cancelar")
        dialogo.setIcon(QMessageBox.Question)
        # dialogo.exec()
        # Caso queira capturar o botão clicado
        resposta = dialogo.exec()
        if resposta == QMessageBox.Ok:
            self.close()  # Sai do programa

    def btn_dialog_sobre_clicked(self):
        # Utiliza o icone definido para o programa
        QMessageBox.about(
            self, "Titulo Exemplo", 'Mensagem de texto "Sobre" o programa'
        )

    def btn_dialog_sobre_qt_clicked(self):
        QMessageBox.aboutQt(self, "Titulo do Programa")

    def btn_dialog_info_clicked(self):
        QMessageBox.information(
            self, "Titulo Exemplo", "Esta é uma mensagem informativa"
        )

    def btn_dialog_erro_clicked(self):
        QMessageBox.critical(
            self, "Titulo Exemplo", "Esta é uma mensagem de erro crítico"
        )

    def btn_dialog_alerta_clicked(self):
        QMessageBox.warning(
            self,
            "Titulo aqui",
            "Tem certeza que deseja aplicar estas mudanças?",
            buttons=QMessageBox.Apply | QMessageBox.Cancel,
        )

    def btn_dialog_questao_clicked(self):
        dialogo = QMessageBox.question(
            self, "Titulo", "Tem certeza que deseja encerrar o programa?"
        )
        if dialogo == QMessageBox.Yes:
            self.close()

    def btn_input_text_clicked(self):
        digitado, confirma = QInputDialog.getText(
            self, "Titulo Exemplo", "Por favor informe seu nome completo:"
        )
        if confirma:
            temp = digitado.replace(" ", "")
            if temp > "":
                QMessageBox.information(self, "Titulo Exemplo", f"Digitado: {digitado}")

    def btn_input_int_clicked(self):
        digitado, confirma = QInputDialog.getInt(
            self, "Titulo Exemplo", "Informe um número qualquer abaixo:"
        )
        if confirma:
            QMessageBox.information(
                self, "Titulo Aqui", f"Voce escolheu o número {digitado}"
            )

    def btn_input_double_clicked(self):
        digitado, confirma = QInputDialog.getDouble(
            self, "Titulo Exemplo", "Informe um número qualquer abaixo:"
        )
        if confirma:
            QMessageBox.information(
                self, "Titulo Aqui", f"Voce escolheu o número {digitado}"
            )

    def btn_input_item_clicked(self):
        digitado, confirma = QInputDialog.getItem(
            self,
            "Titulo Exemplo",
            "Escolha uma côr:",
            ["Azul", "Vermelho", "Verde", "Amarelo"],
            editable=False,
        )
        if confirma:
            QMessageBox.information(
                self, "Titulo Aqui", f"Voce escolheu a côr {digitado}"
            )

    def btn_abrir_arquivo_clicked(self):
        arquivo, _ = QFileDialog.getOpenFileName(self, "Titulo Aqui(abre)", ".")
        temp = arquivo.replace(" ", "")
        if temp > "":
            QMessageBox.about(self, "Titulo Aqui", f"Arquivo aberto:\n {arquivo}")

    def btn_salvar_arquivo_clicked(self):
        arquivo, _ = QFileDialog.getSaveFileName(self, "Titulo Aqui(salva)", ".")
        temp = arquivo.replace(" ", "")
        if temp > "":
            QMessageBox.about(self, "Titulo Aqui", f"Arquivo salvo:\n {arquivo}")

    def btn_escolher_pasta_clicked(self):
        arquivo = QFileDialog.getExistingDirectory(self, "Escolha a pasta", ".")
        temp = arquivo
        if temp.replace(" ", "") > "":
            QMessageBox.about(self, "Titulo Aqui", f"Diretorio escolhido:\n {arquivo}")

    def btn_dialog_fonts_clicked(self):
        confirmado, fonte = QFontDialog.getFont(self)
        if confirmado:
            self.lblFontesCores.setFont(fonte)

    def btn_dialog_colors_clicked(self):
        color = QColorDialog.getColor()
        # print(color)
        # print(color.name())
        if color.isValid():
            self.lblFontesCores.setStyleSheet(f"color:{color.name()}")

    # Definição Funções de Pastas e Arquivos

    def btn_gravar_arquivo_clicked(self):
        # Primeiro obtenho e formato a data e hora
        tempo = datetime.now()
        data = tempo.strftime("%d/%m/%Y")  # Y = aaaa / y = aa
        hora = tempo.strftime("%H:%Mhs")  # '%H:%M:S'

        arquivo = open("arquivo.txt", "w", encoding="UTF-8")
        arquivo.write("Eduardo Volpi de Almeida\n")
        arquivo.write("Rua Willis Roberto Banks, 549 apto.92B\n")
        arquivo.write("05128-000 São Paulo - SP\n")
        arquivo.write("\n")
        arquivo.write(f"Gravado em {data} às {hora}")
        arquivo.close()
        QMessageBox.information(self, "Titulo", "Arquivo Gravado com Sucesso!.")

    def btn_ler_arquivo_clicked(self):
        if os.path.exists("arquivo.txt"):  # tem que usar 'import os' acima
            arquivo = open("arquivo.txt", "r", encoding="UTF-8")
            QMessageBox.about(self, "Titulo", arquivo.read())
            arquivo.close()
        else:
            QMessageBox.information(self, "Titulo", "Arquivo Inexistente.")

    def btn_excluir_arquivo_clicked(self):
        if os.path.exists("arquivo.txt"):  # tem que usar 'import os' acima
            os.remove("arquivo.txt")
            QMessageBox.information(self, "Titulo", "Arquivo Removido com Sucesso!.")
        else:
            QMessageBox.information(self, "Titulo", "Arquivo Inexistente.")

    def btn_renomear_ap_clicked(self):
        # Pode-se renomear Arquivos e Pastas desta mesma forma
        # A função rename() tamebm pode ser usada para mover um arquivo, caso você informe um diretório diferente. Veja
        # como mover um arquivo:
        # os.rename("nome_novo.txt", "Curso Linux/nome_novo.txt")
        # Antes vou ver se existe um arquivo renomeado anterior e exclui-lo
        if os.path.exists("arquivo_renomeado.txt"):
            os.remove("arquivo_renomeado.txt")
        if os.path.exists("arquivo.txt"):  # tem que usar 'import os' acima
            os.rename("arquivo.txt", "arquivo_renomeado.txt")
            QMessageBox.information(
                self,
                "Titulo",
                'Arquivo "arquivo.txt" renomeado para "arquivo_renomeado.txt".',
            )
        else:
            QMessageBox.information(self, "Titulo", "Arquivo Inexistente.")

    def btn_pasta_home_clicked(self):
        user_dir = os.path.expanduser("~")
        QMessageBox.about(self, "Titulo", f'Diretório "home" do sistema:\n{user_dir}')

    def btn_pasta_documents_cliked(self):
        sep = os.path.sep
        user_dir = os.path.expanduser("~")
        documents = "Documents"
        desktop = "Desktop"
        documents_dir = user_dir + sep + documents
        desktop_dir = user_dir + sep + desktop
        QMessageBox.about(
            self,
            "Titulo",
            f'Diretório "Documentos":\n{documents_dir}\nArea de Trabalho (Desktop):\n{desktop_dir}',
        )

    def btn_pasta_atual_clicked(self):
        # diretorio corrente/atual de onde se encontra executando o programa
        pasta_atual = os.getcwd()
        QMessageBox.about(self, "Titulo", f"Diretório do programa:\n{pasta_atual}")

    def btn_criar_pasta_clicked(self):
        pasta_path = os.path.expanduser("~") + os.path.sep + "Pasta Criada"
        if not os.path.exists(pasta_path):
            os.mkdir(pasta_path)
            QMessageBox.about(self, "Titulo", f"Pasta criada:\n{pasta_path}")
        else:
            QMessageBox.warning(self, "Titulo", f'A pasta "{pasta_path}" já existe.')

    def btn_criar_pastas_clicked(self):
        pasta_path = (
            os.path.expanduser("~")
            + os.path.sep
            + "Pasta Criada2"
            + os.path.sep
            + "Outra Pasta"
        )
        if not os.path.exists(pasta_path):
            os.makedirs(pasta_path)
            QMessageBox.about(self, "Titulo", f"Pastas criadas:\n{pasta_path}")
        else:
            QMessageBox.warning(self, "Titulo", f'As pastas "{pasta_path}" já existem.')

    def btn_excluir_pastas_clicked(self):
        # Esta função: os.rmdir remove somente pastas vazias.
        # Para remover pastas com qualquer conteúdo (arquivos ou outras pastas)
        # é preciso usar 'import shutil' e utilizar shutil.rmtree(nomeDir)
        pasta_path = os.path.expanduser("~") + os.path.sep + "Pasta Criada"
        pastas_path = (
            os.path.expanduser("~")
            + os.path.sep
            + "Pasta Criada2"
            + os.path.sep
            + "Outra Pasta"
        )

        if os.path.exists(pasta_path):
            os.rmdir(pasta_path)
            QMessageBox.information(
                self, "T", f"Pasta removida com sucesso.\n{pasta_path}"
            )
        elif os.path.exists(pastas_path):
            os.rmdir(pastas_path)
            QMessageBox.information(
                self, "T", f"Pasta removida com sucesso.\n{pastas_path}"
            )
        else:
            QMessageBox.information(self, "T", "Pasta Inexistente")

    def btn_list_dir_clicked(self):
        # Comando os.listdir() # Lista diretorios e arquivos

        # primeiro vou deixar o usuario escolher o diretorio que deseja lista:
        arquivo = QFileDialog.getExistingDirectory(self, "Escolha a pasta", ".")
        temp = arquivo
        if temp.replace(" ", "") > "":
            # Lista diretorios e arquivos da pasta
            dirs_and_files = os.listdir(arquivo)
            QMessageBox.information(
                self,
                f'Listando: "{arquivo}"',
                f"Lista de arquivos e diretórios:\n\n{str(dirs_and_files)}",
            )

    # Definição Funções Random - usa "import random"

    def btn_rand_uniform_clicked(self):
        # Gera um valor decimal
        val = random.uniform(4, 10)
        QMessageBox.about(
            self, "Title", f"Valor decimal entre 4 e 10 gerado aleatoriamente:\n\n{val}"
        )

    def btn_rand_int_clicked(self):
        # Gera um valor inteiro
        val = random.randint(4, 10)
        QMessageBox.about(
            self, "Title", f"Valor inteiro entre 4 e 10 gerado aleatoriamente:\n\n{val}"
        )

    def btn_rand_choices_clicked(self):
        # Escolhe uma opção aleatória
        nomes = ["Eduardo", "Cleusa", "Nádia", "Karina", "Pedro"]
        nome = random.choice(nomes)
        QMessageBox.about(
            self,
            "Title",
            f"Nome escolhido aleatoriamente:\nNomes: {nomes}\nEscolhido: {nome}",
        )

    def btn_rand_choices2_clicked(self):
        # Escolhe mais de uma opção aleatória
        nomes = ["Eduardo", "Cleusa", "Nádia", "Karina", "Pedro"]
        nome = random.choices(nomes, k=2)
        QMessageBox.about(
            self,
            "Title",
            f"Nome escolhido aleatoriamente:\nNomes: {nomes}\nEscolhidos: {nome}",
        )

    def btn_rand_shuffle_clicked(self):
        # Embaralha items
        cartas = [
            "carta 1",
            "carta 2",
            "carta 3",
            "carta 4",
            "carta 5",
            "carta 6",
            "carta 7",
        ]
        random.shuffle(cartas)
        QMessageBox.about(self, "Title", f"Cartas de 1 a 7 embaralhadas:\n{cartas}")

    def btn_rand_sample_clicked(self):
        # Escolhe alelatoriamente item de uma lista ou range sem repeti-los
        cartas = [
            "carta 1",
            "carta 2",
            "carta 3",
            "carta 4",
            "carta 5",
            "carta 6",
            "carta 7",
        ]
        temp = random.sample(cartas, 3)
        QMessageBox.information(
            self, "Cartas Sorteadas", f"Estas são as cartas:\n{temp}"
        )

    # Definição Funções para Outros

    def btn_loterias_clicked(self):
        jogo, confirma = QInputDialog.getItem(
            self,
            "Loterias",
            "Selecione o jogo para o qual deseja um palpite:",
            ["Megasena", "Lotofacil", "Lotomania", "Supersete"],
            editable=False,
        )
        if confirma:
            if jogo == "Megasena":
                megasena = random.sample(range(1, 61), 6)
                megasena = str(megasena).replace("[", "")
                megasena = megasena.replace("]", "")
                dialogo = QMessageBox.question(
                    self,
                    "Megasena",
                    f"Números sorteados:\n{megasena}\n\nDeseja salvar em um arquivo?",
                )
                if dialogo == QMessageBox.Yes:
                    # Caminho e Arquivo será salvo na area de trabalho
                    arquivo = (
                        os.path.expanduser("~")
                        + os.path.sep
                        + "Desktop"
                        + os.path.sep
                        + "Loterias.txt"
                    )
                    funcoes.gravar_loteria("Megasena", arquivo, megasena)
            elif jogo == "Lotofacil":
                # 15 numeros de 1 a 25
                lotofacil = random.sample(range(1, 26), 15)
                lotofacil = str(lotofacil).replace("[", "")
                lotofacil = lotofacil.replace("]", "")
                dialogo = QMessageBox.question(
                    self,
                    "Lotofacil",
                    f"Números sorteados:\n{lotofacil}\n\nDeseja salvar em um arquivo?",
                )
                if dialogo == QMessageBox.Yes:
                    # Caminho e Arquivo será salvo na area de trabalho
                    arquivo = (
                        os.path.expanduser("~")
                        + os.path.sep
                        + "Desktop"
                        + os.path.sep
                        + "Loterias.txt"
                    )
                    funcoes.gravar_loteria("Lotofácil", arquivo, lotofacil)
            elif jogo == "Lotomania":
                QMessageBox.information(self, "Lotomania", "Estará disponível em breve")
            elif jogo == "Supersete":
                QMessageBox.information(self, "Supersete", "Estará disponível em breve")

    def btn_sistema_operacional_clicked(self):
        plataforma = platform.system()  # utiliza 'import platform' acima
        plataforma2 = sys.platform  # utiliza o "import sys"
        QMessageBox.about(
            self,
            "Titulo",
            f'com "import platform": {plataforma}\ncom "import sys": {plataforma2}',
        )
        """
        com import platform retorna:
        Linux: Linux
        Windows: Windows
        MacOS: Darwin
        com import sys retorna:
        Linux: linux
        Windows: Win32
        MacOS: darwin
        AIX: aix
        """

    def btn_data_hora_sistema_clicked(self):
        # Utiliza: 'from datetime import datetime'
        # Primeiro obtenho data e hora
        tempo = datetime.now()
        # Agora Formato
        data = tempo.strftime("%d/%m/%Y")  # Y = aaaa / y = aa
        hora = tempo.strftime("%H:%Mhs")  # '%H:%M:S'
        # e exibo
        QMessageBox.information(
            self,
            "Data e Hora do Sistema",
            f"Data de Hoje do Sistema: {data}\nHora Atual do Sistema: {hora} ",
        )

    def btn_abrir_segundo_form_clicked(self):
        self.segundo_form.show()

    # Definição Funções para Testes

    # para testes
    def btn_para_testes_clicked(self):
        digitado, confirma = QInputDialog.getText(
            self, "Inverte Nomes", "Por favor informe seu nome:"
        )
        if confirma:
            temp = digitado.replace(" ", "")
            if temp > "":
                nome_invertido = digitado[::-1]
                QMessageBox.information(self, "Nome Invertido", nome_invertido)


"""
Initialization
"""
if __name__ == "__main__":
    app = QApplication()
    # app.setStyle('Fusion')  # Windows - windowsvista - Fusion

    # Habilitar a aplicação com o tradutor
    translator = QTranslator(app)
    # Recuperar o diretório de traduções
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    # Carregar a tradução no tradutor
    translator.load("qtbase_pt_BR", translations)
    # Aplicar
    app.installTranslator(translator)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
