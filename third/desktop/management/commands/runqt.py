from django.core.management.base import BaseCommand
from PySide6.QtWidgets import QApplication
from desktop.main import MainWindow
import sys


class Command(BaseCommand):
    help ="Запуск приложения"
    
    def handle(self, *args, **options) -> str | None:
        app = QApplication(sys.argv)
        main = MainWindow()
        main.show()
        app.exit(app.exec())