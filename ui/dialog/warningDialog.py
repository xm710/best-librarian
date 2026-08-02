from PySide6.QtWidgets import QMessageBox

def wrong_level_file(error):
    QMessageBox.warning(
        None,
        "錯誤",
        f"打開時發生錯誤\n{error}"
    )