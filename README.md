# Twitter Scraper dengan Tweepy

Script ini digunakan untuk melakukan scraping data dari Twitter menggunakan Twitter API v2 dan Tweepy. Hasil scraping akan diekspor ke dalam file CSV untuk analisis lebih lanjut.

## Persyaratan
Sebelum menjalankan script, pastikan Anda telah menginstal dependensi yang diperlukan pada environment:

```bash
pip install -r requirements.txt
```

Selain itu, Anda memerlukan akun Twitter Developer dan mendapatkan Bearer Token dari [Twitter Developer Portal Projects & Apps page](https://developer.x.com/en/portal/projects-and-apps) untuk dapat mengakses Twitter API v2.

## Konfigurasi

Buat file .env di direktori proyek dan tambahkan Bearer Token yang diperoleh dari akun Twitter Developer Anda:

BEARER_TOKEN=your_twitter_bearer_token_here

Cara Menggunakan

Siapkan env: Pastikan dependensi telah diinstal dan file .env sudah dibuat.

Jalankan script:
python scrape.py

Hasil scraping: Data akan tersimpan dalam file tweets.csv di direktori yang sama dengan script.
