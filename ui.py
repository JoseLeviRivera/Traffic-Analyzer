import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QTabWidget, QVBoxLayout, QWidget, QTextEdit, QTableWidget, QTableWidgetItem


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Configurar la barra de menú
        menubar = self.menuBar()

        # Menú de Servicios
        services_menu = menubar.addMenu('Servicios')

        # Submenús de Servicios
        save_action = QAction('Guardar Registro', self)
        update_action = QAction('Actualizar Registro', self)
        delete_action = QAction('Eliminar Registro', self)

        services_menu.addAction(save_action)
        services_menu.addAction(update_action)
        services_menu.addAction(delete_action)

        # Submenú de Ayuda
        help_menu = menubar.addMenu('Ayuda')

        # Submenú de Salir
        exit_action = QAction('Salir', self)
        exit_action.triggered.connect(self.close)

        help_menu.addAction(exit_action)

        # Configurar pestañas
        tab_widget = QTabWidget(self)

        # Pestaña 1: Servicios
        services_tab = QWidget()
        services_tab.layout = QVBoxLayout(services_tab)

        # Crear una tabla para mostrar datos de la base de datos
        services_table = QTableWidget()
        services_table.setColumnCount(3)  # Columnas: puerto, nombre_servicio, ip
        services_table.setHorizontalHeaderLabels(["Puerto", "Nombre del Servicio", "IP"])

        # Llenar la tabla con datos de ejemplo (puedes reemplazar esto con datos reales de tu base de datos)
        self.populate_table(services_table)

        services_tab.layout.addWidget(services_table)
        services_tab.setLayout(services_tab.layout)

        # Pestaña 2: Analizar servicios nmap
        analyze_tab = QWidget()
        analyze_tab.layout = QVBoxLayout(analyze_tab)
        analyze_tab.text_edit = QTextEdit()
        analyze_tab.layout.addWidget(analyze_tab.text_edit)
        analyze_tab.setLayout(analyze_tab.layout)

        # Pestaña 3: Generar Alerta
        reports_tab = QWidget()
        reports_tab.layout = QVBoxLayout(reports_tab)
        reports_tab.text_edit = QTextEdit()
        reports_tab.layout.addWidget(reports_tab.text_edit)
        reports_tab.setLayout(reports_tab.layout)

        # Pestaña 4: Ver Hosts Conectados Localmente
        local_hosts_tab = QWidget()
        local_hosts_tab.layout = QVBoxLayout(local_hosts_tab)
        local_hosts_tab.text_edit = QTextEdit()
        local_hosts_tab.layout.addWidget(local_hosts_tab.text_edit)
        local_hosts_tab.setLayout(local_hosts_tab.layout)

        # Pestaña 5: Licencia
        license_tab = QWidget()
        license_tab.layout = QVBoxLayout(license_tab)
        license_tab.text_edit = QTextEdit()
        license_tab.layout.addWidget(license_tab.text_edit)
        license_tab.setLayout(license_tab.layout)

        # Agregar pestañas al widget principal
        tab_widget.addTab(services_tab, "Servicios Registrados")
        tab_widget.addTab(analyze_tab, "Analizar servicios nmap")
        tab_widget.addTab(analyze_tab, "Generar Reportes")
        tab_widget.addTab(reports_tab, "Generar Alerta")
        tab_widget.addTab(local_hosts_tab, "Ver Hosts Conectados Localmente")

        # Configurar el widget central
        self.setCentralWidget(tab_widget)

        # Configurar la ventana principal
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Interfaz con Menús')
        self.show()

    def populate_table(self, table):
        # Puedes reemplazar estos datos de ejemplo con datos reales de tu base de datos
        data = [
            {"puerto": 80, "nombre_servicio": "HTTP", "ip": "192.168.1.1"},
            {"puerto": 22, "nombre_servicio": "SSH", "ip": "192.168.1.2"},
            {"puerto": 443, "nombre_servicio": "HTTPS", "ip": "192.168.1.3"}
        ]

        for row, record in enumerate(data):
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(str(record["puerto"])))
            table.setItem(row, 1, QTableWidgetItem(record["nombre_servicio"]))
            table.setItem(row, 2, QTableWidgetItem(record["ip"]))


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
