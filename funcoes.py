import os

from PySide6.QtWidgets import QMessageBox


def gravar_loteria(lottery_name: str, file_path, file_content):
    if not os.path.exists(file_path):
        arquivo = open(file_path, 'w', encoding='UTF-8')
        arquivo.close()

    arquivo = open(file_path, 'a', encoding='UTF-8')
    arquivo.write(f'\nNúmeros para {lottery_name}:\n\n')
    arquivo.write(str(file_content) + '\n')
    arquivo.write('------------------------------------------------------------')
    arquivo.close()

    dialogo = QMessageBox()
    dialogo.setWindowTitle(f'Loteria: {lottery_name}')
    dialogo.setText('Números adicionados ao arquivo "Loterias.txt"\nna sua Área de Trabalho')
    dialogo.setStandardButtons(QMessageBox.Ok)
    dialogo.setIcon(QMessageBox.Information)
    dialogo.exec()
