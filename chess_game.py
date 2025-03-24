import sys
import chess
import chess.svg
import chess.engine
import ollama
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit
from PyQt5.QtSvg import QSvgWidget

# Stockfish motorunun yolu
STOCKFISH_PATH = "C:/Users/CASPER/repos/DQN/Chess/stockfish/stockfish-windows-x86-64-avx2.exe"

class ChessGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Satranç tahtası ve mesaj listesi
        self.board = chess.Board()
        self.messages = []
        self.messages.append({"role": "user", "content": f"Merhaba Asistan, ben Keremcem. Bugün santranç oynayacağız. Ben beyazım ve sen siyahsın. Beni yenebilecek misin?"})

        self.initUI()
        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

    def initUI(self):
        self.setWindowTitle("Master Chief vs. Asistan AI")
        self.setGeometry(100, 100, 600, 700)

        self.board_display = QSvgWidget(self)
        self.update_board()

        self.move_input = QTextEdit(self)
        self.move_input.setPlaceholderText("Hamleni gir (örn: e2e4)")

        self.move_button = QPushButton("Hamle Yap", self)
        self.move_button.clicked.connect(self.make_move)

        self.log = QTextEdit(self)
        self.log.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.board_display)
        layout.addWidget(self.move_input)
        layout.addWidget(self.move_button)
        layout.addWidget(self.log)

        self.setLayout(layout)

    def update_board(self):
        """ Tahtayı günceller ve SVG olarak gösterir """
        svg_data = chess.svg.board(self.board).encode("utf-8")
        self.board_display.load(svg_data)

    def make_move(self):
        """ Kullanıcı hamle yapar ve Asistan yanıt verir """
        move = self.move_input.toPlainText().strip()

        if chess.Move.from_uci(move) in self.board.legal_moves:
            self.board.push_uci(move)
            self.log.append(f"Senin hamlen: {move}")
            self.messages.append({"role": "user", "content": f"Keremcem'in hamlesi: {move}"})
            
            # Asistan hamlesi
            result = self.engine.play(self.board, chess.engine.Limit(time=1.0))
            ai_move = result.move
            self.board.push(ai_move)
            self.log.append(f"Asistan'ın hamlesi: {ai_move}")

            # Asistan AI'dan açıklama al
            explanation = self.get_ai_explanation(ai_move)
            self.log.append(f"Asistan: {explanation}")

            self.update_board()
        else:
            self.log.append("Geçersiz hamle!")

        self.move_input.clear()

    def get_ai_explanation(self, move):
        """ Asistan modeline hamlenin açıklamasını sorar """
        board_state = self.board.fen()
        prompt = f"Satranç tahtasında şu pozisyondayken '{move}' hamlesini yaptın:\n\n{board_state}\n\nBu hamleyi neden yaptığını açıklar mısın?"
        
        self.messages.append({"role": "user", "content": prompt})
        
        response = ollama.chat(model="Keremcm_/Asistan_AI:2b", messages=self.messages)
        yanıt = response["message"]["content"]

        self.messages.append({"role": "assistant", "content": yanıt})
        return yanıt

    def closeEvent(self, event):
        """ Pencere kapanırken Stockfish motorunu kapat """
        self.engine.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChessGUI()
    window.show()
    sys.exit(app.exec_())
