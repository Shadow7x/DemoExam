from django.core.management.base import BaseCommand
from PySide6.QtWidgets import QApplication
from desktop.Forms.main import MainWindow
import sys

class Command(BaseCommand):
    help = "Запуск Desktop приложения"
    
    def handle(self, *args, **options ) -> str | None:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exit(app.exec())