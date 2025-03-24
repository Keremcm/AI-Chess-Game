# Satranç AI

Bu proje, yapay zeka destekli bir satranç motoru içerir. Python, PyQt5 ve Stockfish motoru kullanılarak geliştirilmiştir. Ayrıca, Ollama tabanlı bir AI modeline entegre edilmiştir. Kullanıcı, AI'ya karşı oynayabilir ve her hamlesinin açıklamasını alabilir.

## Özellikler
- PyQt5 ile görselleştirilmiş satranç tahtası
- Stockfish motoru ile AI hamlesi
- Ollama modelinden AI hamle açıklamaları
- Kullanıcı vs. AI oyun modu
- Geçerli hamle kontrolü ve hamle geçmişi

## Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki kütüphanelerin kurulu olması gerekmektedir:

```sh
pip install pyqt5 chess ollama
```

Ayrıca, Stockfish motorunun sisteminizde yüklü olması gerekmektedir. Stockfish'i [bu bağlantıdan](https://stockfishchess.org/download/) indirebilirsiniz.

## Kullanım
Projeyi çalıştırmak için terminalde aşağıdaki komutu kullanın:

```sh
python chess_game.py
```

### Kullanıcı Hamlesi
Oyuncu beyaz taşlarla başlar. Kullanıcı hamlesini "e2e4" gibi bir formatta girerek oyuna katılabilir. Hamle geçerliyse, AI bir hamle yapacak ve hamlesini açıklayacaktır.

## AI Açıklamaları
Her hamle sonrası AI, Ollama tabanlı modelden bir açıklama alarak yapılan hamleyi neden yaptığını kullanıcıya iletecektir.

## Stockfish Motoru
Stockfish, satrançta en güçlü motorlardan birisidir ve burada AI'nın hamlelerini değerlendirmek için kullanılır.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
