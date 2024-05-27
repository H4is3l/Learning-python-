from PyQt6 import uic, QtWidgets

def executar():

    peso = formulario.txtPeso.text()
    peso =float(peso)
    altura = formulario.txtAltura.text()
    altura = float(altura)
    IMC= peso/altura

    formulario.lblImc.setText(str(f'O seu IMC é: {IMC:.1f}'))

app=QtWidgets.QApplication([])
formulario=uic.loadUi('tela.ui')
formulario.btnCalculo.clicked.connect(executar)

formulario.show()
app.exec()