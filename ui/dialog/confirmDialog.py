from PySide6.QtWidgets import QFileDialog

def select_world():
    """
    選擇世界資料夾
    """
    world_path = QFileDialog.getExistingDirectory(
        None,
        "選擇 Minecraft 世界"
    )

    return world_path