
from django.core.management.base import BaseCommand
from PySide6.QtWidgets import QApplication
from desktop.main import MainWindow
import sys

from typing import Any

class Command(BaseCommand):
    help = "Запуск desktop Приложения"
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exit(app.exec())