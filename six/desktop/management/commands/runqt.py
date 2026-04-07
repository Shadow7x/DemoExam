from typing import Any

from PySide6.QtWidgets import QApplication
from django.core.management.base import BaseCommand
from desktop.main import MainWindow
import sys

class Command(BaseCommand):
    help = "Запуск desktop приложения"
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exit(app.exec())