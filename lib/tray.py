
from PyQt6.QtGui import * 
from PyQt6.QtWidgets import * 

def setuptray(animations, set_animation, quit_func): 
    print("Creating app")
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    def quitApp():
        app.quit()
        quit_func()

    # Create the icon
    icon = QIcon("icon.png")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the menu
    menu = QMenu()

    animationMenu = QMenu("Animations")

    for animation in animations:
        if not animation.endswith(".py"): 
            continue
        animationAction = animationMenu.addAction(animation)

        receiver = lambda bVal, anim=animation: set_animation(bVal, anim)

        animationAction.triggered.connect(receiver)

    menu.addMenu(animationMenu)

    # Add a Quit option to the menu.
    quit = QAction("Quit")
    quit.triggered.connect(quitApp)
    menu.addAction(quit)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    app.exec()
    