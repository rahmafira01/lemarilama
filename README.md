Rahma Dwi Maghfira  
2306245794  
PBP F

Link Menuju Project : http://rahma-dwi31-lemarilama.pbp.cs.ui.ac.id

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekedar mengukuti tutorial). 
### 1. Membuat Proyek Django 
Untuk membuat project Django, hal pertama yang saya lakukan adalah menginisiasi git pada direktori utama "lemarilama" dan juga menghubungkan repository github dengan direktori tersebut. Selanjutnya, saya membuat dan mengaktifkan virtual envoirment dengan perintah ```python3 -m venv env``` dan ```source env/bin/activate```, kemudian menginstal dependencies yang tercantum dalam ```requirements.txt```. Setelah itu, saya membuat proyek Django baru dengan perintah ```django-admin startproject lemarilama``` dan mengonfigurasi ```ALLOWED_HOST``` di ```settings.py``` menjadi ```["localhost", "127.0.0.1"]```. Saya menjalankan server Django menggunakan ```python3 manage.py runserver```, dan memeriksa apakah proyek berhasil dengan membuka (http://localhost:8000), lalu menghentikan server dan menonaktifkan virtual environment. Terakhir, saya membuat file ```.gitignore``` untuk menentukan file yang harus diabaikan oleh Git, dan melakukan commit serta push ke repository Github.

### 2. Membuat aplikasi dengan nama *main*
Setelah berhasil membuat proyek Django dan memastikan virtual environment tetap aktif, langkah selanjutnya yang saya lakukan adalah menjalankan perintah ```python3 manage.py startapp main``` untuk membuat aplikasi baru dengan nama "main". Perintah ini akan menghasilkan direktori baru dengan nama "main" yang berisi struktur awal aplikasi Django. Kemudian, saya membuka berkas ```settings.py``` di dalam direktori "lemarilama" dan menambahkan *'main'* ke dalam daftar aplikasi di ```INSTALLED_APPS```. 

### 3. Melakukan *routing* pada proyek
Untuk mendaftarkan aplikasi *main* ke dalam proyek, saya membuka berkas ```settings.py``` di direktori lemarilama dan menambahkan *'main'* ke dalam daftar aplikasi di variabel ```INSTALLED_APPS``` sebagai elemen terakhir.  

### 4. Membuat model pada aplikasi dengan atribut *name*, *price*, dan *description*
Setelah melakukan *routing* pada proyek *main*, saya mengubah berkas ```models.py``` dalam aplikasi *main* untuk mendefinisikan model baru bernama ```Product``` dengan atribut *name*, *price*, dan *description*, serta metode ```is_pricey_price``` untuk menentukan apakah harga produk melebihi 10000.

### 5. Membuat fungsi pada *views.py* untuk dikembalikan ke *template*
Karena pada berkas ```views.py``` sudah memiliki import yang diperlukan, maka saya langsung mengubah data yang ada di dalam dictionary ```context``` pada fungsi ```show_main``` dengan data baru seperti *aplikasi*, *nama*, dan *kelas*. Fungsi ini kemudian menggunakan render untuk menampilkan tampilan dengan berkas template ```main.html``` yang sesuai. 

### 6. Membuat *routing* di *urls.py* untuk memetakan fungsi dari *views.py*
Setelah membuat aplikasi *main*, langkah selanjutnya yang saya lakukan adalah mengatur *routing* URL dengan membuat berkas ```urls.py``` di direktori *main* dan menambahkan rute untuk tampilan ```show_main```. Selanjutnya, saya mengimpor fungsi ```include``` di berkas ```urls.py``` proyek *lemarilama* dan menambahkan rute untuk aplikasi *main* dalam ```urlspatterns```. 

### 7. *deployment* ke PWS
Agar dapat dilihat oleh orang lain, hal pertama yang saya lakukan adalah menekan tombol *Create New Project* lalu mengisi *Project Name* dengan lemarilama, kemudian menekan tombol *Create New Project*. Selanjutnya, saya memasukkan URL *deployments* PWS saya ke variabel ```ALLOWED_HOSTS``` di berkas ```settings.py```. Setelah melakukan semua perubahan, saya melakukan git add, commit, dan push ke Github dan PWS untuk memastikan proyek dapat diakses publik. 

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara *urls.py*, *views.py*, *models.py*, dan berkas *html*.

## Jelaskan fungsi git dalam pengembangan perangkat lunak!

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

## Mengapa model pada Django disebut sebagai ORM?