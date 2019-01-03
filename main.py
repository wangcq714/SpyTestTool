import sys
sys.path.append("./dtctest")
sys.path.append("./msgtest")
sys.path.append("./signaltest")
from dtctest import spy_dtc_test
from msgtest import spy_msg_test
from ui.ui import *

app = QApplication(sys.argv)
mainWindow = MyMainWindow()
mainWindow.setupUi(mainWindow)
mainWindow.setup()

mainWindow.show()

sys.exit(app.exec_())
