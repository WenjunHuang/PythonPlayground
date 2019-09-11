from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtSql import *
from PySide2.QtGui import *
from createdb import *
from initDb import *
from bookdelegate import BookDelegate


class BookWindow(QMainWindow):
    bookTable: QTableView

    def __init__(self):
        super().__init__()
        self.setupUi()

        init_db()
        # err = init_db()
        # if not err.type() == QSqlError.NoError:
        #     self.showError(err)
        #     return

        model = QSqlRelationalTableModel(self.bookTable)
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.setTable("books")

        author_idx = model.fieldIndex("author")
        genre_idx = model.fieldIndex("genre")
        model.setRelation(author_idx, QSqlRelation("authors", "id", "name"))
        model.setRelation(genre_idx, QSqlRelation("genres", "id", "name"))

        # set the localized header captions:
        model.setHeaderData(author_idx, Qt.Horizontal, self.tr("Author Name"))
        model.setHeaderData(genre_idx, Qt.Horizontal, self.tr("Genre"))
        model.setHeaderData(model.fieldIndex("title"), Qt.Horizontal, self.tr("Title"))
        model.setHeaderData(model.fieldIndex("year"), Qt.Horizontal, self.tr("Year"))
        model.setHeaderData(model.fieldIndex("rating"), Qt.Horizontal, self.tr("Rating"))

        if not model.select():
            print(model.lastError())

        self.bookTable.setModel(model)
        self.bookTable.setItemDelegate(BookDelegate(self.bookTable))
        self.bookTable.setColumnHidden(model.fieldIndex("id"), True)
        self.bookTable.setSelectionMode(QAbstractItemView.SingleSelection)

        # Initialize the Author combo box:
        self.authorEdit.setModel(model.relationModel(author_idx))
        self.authorEdit.setModelColumn(model.relationModel(author_idx).fieldIndex("name"))

        self.genreEdit.setModel(model.relationModel(genre_idx))
        self.genreEdit.setModelColumn(model.relationModel(genre_idx).fieldIndex("name"))

        # Lock and prohibit resizing of the width of the rating column:
        self.bookTable.horizontalHeader().setSectionResizeMode(model.fieldIndex("rating"),
                                                               QHeaderView.ResizeToContents)

        mapper = QDataWidgetMapper(self)
        mapper.setModel(model)
        mapper.setItemDelegate(BookDelegate(self))
        mapper.addMapping(self.titleEdit, model.fieldIndex("title"))
        mapper.addMapping(self.yearEdit, model.fieldIndex("year"))
        mapper.addMapping(self.authorEdit, author_idx)
        mapper.addMapping(self.genreEdit, genre_idx)
        mapper.addMapping(self.ratingEdit, model.fieldIndex("rating"))

        selection_model = self.bookTable.selectionModel()
        selection_model.currentRowChanged.connect(mapper.setCurrentModelIndex)

        self.bookTable.setCurrentIndex(model.index(0, 0))
        self.create_menubar()

    def showError(self, err):
        QMessageBox.critical(self, "Unable to initialize Database",
                             "Error initializing database:" + err.text())

    def create_menubar(self):
        file_menu = self.menuBar().addMenu(self.tr("&File"))
        quit_action = file_menu.addAction(self.tr("&Quit"))
        quit_action.triggered.connect(qApp.quit)

        help_menu = self.menuBar().addMenu(self.tr("&Help"))
        about_action = help_menu.addAction(self.tr("&About"))
        about_action.setShortcut(QKeySequence.HelpContents)
        about_action.triggered.connect(self.about)
        aboutQt_action = help_menu.addAction("&About Qt")
        aboutQt_action.triggered.connect(qApp.aboutQt)

    def about(self):
        QMessageBox.about(self,
                          self.tr("About Books"),
                          self.tr(
                              "<p>The <b>Books</b> example shows how to use QT SQL classes with a model/view framework."))

    def setupUi(self):
        self.setWindowTitle('Books')

        vbox = QVBoxLayout()
        vbox.setSpacing(6)
        vbox.setContentsMargins(9,
                                9,
                                9,
                                9)

        groupBox = QGroupBox()
        groupBoxLayout = QVBoxLayout()
        groupBox.setLayout(groupBoxLayout)
        groupBoxLayout.setSpacing(6)
        groupBoxLayout.setContentsMargins(9,
                                          9,
                                          9,
                                          9)

        self.bookTable = QTableView()
        self.bookTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        groupBoxLayout.addWidget(self.bookTable)
        groupBox.setLayout(groupBoxLayout)

        groupBox2 = QGroupBox()
        groupBox2.setTitle('Details')
        groupBox2Layout = QFormLayout()
        self.titleEdit = QLineEdit()
        groupBox2Layout.addRow(QLabel(text="<b>Title</b>"),
                               self.titleEdit)

        self.authorEdit = QComboBox()
        self.authorEdit.setEnabled(True)
        groupBox2Layout.addRow(QLabel(text="<b>Author</b>"),
                               self.authorEdit)

        self.genreEdit = QComboBox()
        self.genreEdit.setEnabled(True)
        groupBox2Layout.addRow(QLabel(text="<b>Genre</b>"),
                               self.genreEdit)

        self.yearEdit = QSpinBox()
        self.yearEdit.setMinimum(-1000)
        self.yearEdit.setMaximum(2100)
        self.yearEdit.setEnabled(True)
        groupBox2Layout.addRow(QLabel(text="<b>Year</b>"),
                               self.yearEdit)

        self.ratingEdit = QSpinBox()
        self.ratingEdit.setMaximum(5)
        groupBox2Layout.addRow(QLabel(text="<b>Rating</b>"),
                               self.ratingEdit)

        groupBox2.setLayout(groupBox2Layout)

        groupBoxLayout.addWidget(groupBox2)

        vbox.addWidget(groupBox)

        center = QWidget()
        center.setLayout(vbox)
        self.setCentralWidget(center)
