# Lemari Lama 

Rahma Dwi Maghfira  
2306245794  
PBP F

Link Menuju Project : http://rahma-dwi31-lemarilama.pbp.cs.ui.ac.id  
Link Menuju Repository : https://github.com/rahmafira01/lemarilama.git  


# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
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
![bagan.png](images/bagan.png)

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi sebagai sistem pengendalian versi yang digunakan dalam pengembangan perangkat lunak untuk melacak perubahan kode, menyimpan versi proyek, dan memfasilitasi kolaborasi antar anggota tim. Dengan Git, perubahan yang dilakukan dapat dicatat secara rinci, memungkinkan rollback ke versi sebelumnya jika diperlukan, serta meminimalkan risiko konflik kode saat bekerja dalam tim. Git juga memastikan pengelolaan proyek yang efisien. 

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django dijadikan sebagai permulaan dalam pembelajaran perangkat lunak karena framework ini menggunakan bahasa Python, yang dikenal sederhana dan mudah dipahami. Django menerapkan pola arsitektur Model-View-Template (MVT), yang memudahkan pemisahan logika antara Model, View, dan Template. Selain itu, platform Django ini mempunyai banyak fitur bawaan yang siap untuk digunakan sehingga cocok untuk para pemula.

## Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena memungkinkan pengembang berinteraksi dengan basis data relasional menggunakan objek Python. ORM berfungsi menghubungkan antara model Python dan tabel di database, sehingga pengembang dapat mengelola data tanpa menulis SQL secara langsung. Hal ini mempermudah pengelolaan dan manipulasi data dalam database secara lebih efisien dan terstruktur.  


# Tugas 3: Implementasi Form dan Data Delivery pada Django
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### 1. Membuat forms untuk input
Hal pertama yang saya lakukan adalah membuat ```forms.py``` untuk mendefinisikan form berbasis model ```Product```. Setelah itu, saya menambahkan fungsi ```create_product``` di ```views.py``` untuk memproses dan menyimpan data form. Kemudian, saya mengedit ```urls.py``` untuk menambahkan *URL path* ke form tersebut. Selanjutnya, saya membuat ```create_product.html``` untuk menampilkan form input, dan memperbarui ```main.html``` agar menampilkan data product dalam tabel serta menambahkan tombol untuk membuka form. Terakhir, saya menjalankan server dan menguji fungsionalitasnya.
### 2. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
* Format XML  
Langkah awal yang saya lakukan adalah menambahkan impor ```HttpResponse``` dan ```serializers``` di ```views.py```, lalu membuat fungsi ```show_xml``` untuk mengambil data Product dan menyerialisasinya menjadi XML. Hasilnya dikembalikan sebagai ```HttpResponse``` dengan ```content_type="application/xml"```.  
* Format JSON  
Langkah-langkah untuk implementasi JSON tidak jauh berbeda dari XML. Perbedaannya hanya terletak pada penggunaan ```content_type="application/json"``` dan ```serializers.serialize("json", data)```  
* Format XML by ID dan JSON by ID  
Sebenarnya, langkah-langkahnya mirip dengan yang dilakukan untuk menampilkan data XML dan JSON secara umum, hanya saja kali ini fokus pada data berdasarkan ID. Pertama, saya membuat dua fungsi baru di ```views.py```: ```show_xml_by_id``` dan ```show_json_by_id```. Fungsi-fungsi ini mengambil data dari Product berdasarkan ID yang diberikan menggunakan ```Product.objects.filter(pk=id)```. Data tersebut kemudian diserialisasi menjadi format XML atau JSON, sesuai dengan fungsi yang dipanggil, dan dikembalikan sebagai ```HttpResponse``` dengan ```content_type``` yang sesuai. Setelah itu, saya mengimpor kedua fungsi tersebut di ```urls.py``` dan menambahkan path URL yang sesuai untuk masing-masing fungsi.   
### 3. Membuat routing URL 
```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam pengimplementasian sebuah platform untuk memastikan bahwa data dapat dikirimkan dengan efisien dan aman antara berbagai komponen sistem atau ke pengguna akhir. Ini mendukung integritas data, meningkatkan performa aplikasi, dan memungkinkan interaksi yang lancar antara sistem yang berbeda. Tanpa mekanisme data delivery yang baik, platform akan mengalami masalah dalam konsistensi data, performa, dan keamanan.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih disukai dibandingkan XML karena formatnya lebih ringan, lebih mudah dibaca, dan lebih efisien dalam pemrosesan serta ukuran data. JSON juga lebih populer karena dukungan luas di berbagai bahasa pemrograman dan API.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memvalidasi input pengguna sesuai dengan aturan yang telah ditetapkan di form. Ini memastikan data yang diterima sudah benar dan aman sebelum diproses atau disimpan.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
{% csrf_token %} adalah token keamanan yang dihasilkan secara otomatis oleh Django untuk mencegah serangan Cross-Site Request Forgery (CSRF). Token ini memastikan bahwa permintaan yang dikirimkan ke server berasal dari sumber yang sah dan bukan dari penyerang yang mencoba mengelabui pengguna. 

## Screenshot Postman
### 1. HTML Source  
![HTML.png](images/HTML.png)
### 2. XML  
![XML.png](images/XML.png)
### 3. JSON  
![JSON.png](images/JSON.png)
### 4. XML by ID  
![XMLBYID.png](images/XMLBYID.png)
### 5. JSON by ID  
![JSONBYID.png](images/JSONBYID.png)  
  

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  
### 1. Mengimplementasikan fungsi registrasi, login, dan logout
Hal pertama yang saya lakukan adalah membuat halaman registrasi dengan mengimpor ```UserCreationForm``` dan ```messages``` di ```views.py```, kemudian membuat fungsi ```register``` untuk menangani pemuatan akun baru dan menampilkan formulir registrasi pada ```register.html```. Setelah itu, saya menambahkan fungsi ```login_user``` yang menggunakan ```AuthenticationForm``` untuk autentikasi pengguna, dan menampilkan formulir login pada ```login.html```. Setelah login berhasil, pengguna diarahkan ke halaman utama. Selanjutnya, saya membuat fungsi ```logout_user``` untuk menghapus sesi pengguna yang sedang login, dan menambahkan tombol logout di halaman utama (```main.html```). Semua fungsi ini dihubungkan melalui path yang ditambahkan pada ```urls.py```.   
### 2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Pertama, daftar akun pengguna melalui halaman registrasi dengan mengisi *username* dan *password*. Setelah berhasil, login dan tambahkan tiga produk melalui form yang berisi nama produk, harga, dan deskripsi. Setelah selesai, logout dan ulangi proses dengan mendaftarkan akun kedua.  
### 3. Menghubungkan model ```Product``` dengan ```User```.
Saya menguhubungkan LemariLama dengan User menggunakan ```ForeignKey``` di ```models.py```. Di ```views.py```, saya memodifikasi fungsi ```create_product``` agar setiap entri product terkait dengan pengguna yang sedang login, dan hanya menampilkan entri pengguna tersebut di ```show_main``` menggunakan ```filter(user=request.user)```. Setelah itu, saya melakukan migrasi dengan ```python3 manage.py makemigrations```. Terakhir, atur ```DEBUG``` untuk ```production``` di ```settings.py``` dan menjalankan server.  
### 4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan ```cookies``` seperti ```last login``` pada halaman utama aplikasi.  
Menambahkan ```cookie``` untuk menyimpan data ```last login``` dan menampilkannya di halaman utama. Di ```login_user```, setelah login berhasil, tambahkan ```cookie``` ```last_login``` menggunakan ```response.set_cookie()```. Pada ```show_main```, tampilkan ```last_login``` dari ```cookie``` di ```context```. Di ```logout_user```, hapus *cookie* ```last_login``` saat logout menggunakan ```response.delete_cookie()```. Terakhir, di ```main.html```, tambahkan kode untuk menampilkan ```last login``` di halaman utama. Jalankan proyek dan cek ```cookies``` di *browser* untuk melihat hasilnya.  

## Apa perbedaan antara ```HttpResponseRedirect()``` dan ```redirect()```
Perbedaan utama antara *HttpResponseRedirect()* dan *redirect()* di Django adalah bahwa *HttpResponseRedirect()* adalah kelas bawaan Django yang secara manual mengarahkan pengguna ke URL tertentu, sedangkan *redirect()* adalah fungsi yang mempermudah penggunaan *HttpResponseRedirect()*. Dengan *redirect()*, kita bisa langsung memasukkan nama URL atau view name tanpa harus membangun URL secara manual, sehingga lebih efisien dan mudah digunakan.

##  Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model *Product* dengan *User* di Django biasanya dilakukan menggunakan *ForeignKey*. Pada model *Product*, tambahkan field *user* dengan tipe *ForeignKey* yang mengacu pada model *User*. Ini memungkinkan setiap produk dikaitkan dengan pengguna yang membuatnya. Setiap *ForeignKey* juga dapat diatur dengan opsi *on_delete* (misalnya *CASCADE*), yang menentukan apa yang terjadi pada produk ketika pengguna dihapus. Dengan penghubungan ini, kita bisa mengakses data pengguna dari produk atau sebaliknya.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses verifikasi identitas pengguna (apakah pengguna adalah siapa yang mereka klaim), sedangkan authorization adalah proses menentukan hak akses pengguna ke sumber daya setelah mereka terautentikasi. Saat pengguna login, Django melakukan authentication dengan memverifikasi kredensial (seperti username dan password). Setelah berhasil login, Django menggunakan izin atau *permissions* untuk menentukan hak akses (authorization) pengguna ke berbagai fitur atau halaman. Django mengimplementasikan authentication melalui *User* model dan *auth* system, sedangkan authorization dikelola dengan *permissions* dan *decorators* seperti `@login_required` untuk membatasi akses.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan *session cookies*. Ketika pengguna login, Django menyimpan informasi pengguna dalam cookie yang terkait dengan sesi, memungkinkan pengguna tetap terautentikasi selama sesi berlangsung tanpa perlu login ulang setiap kali berpindah halaman. Selain autentikasi, cookies juga digunakan untuk menyimpan preferensi pengguna atau data sementara lainnya. Namun, tidak semua cookies aman—cookies yang tidak dienkripsi atau dilindungi dengan baik rentan terhadap serangan seperti *cookie hijacking*. Untuk keamanan, Django menggunakan *session* cookies yang aman (misalnya dengan *HttpOnly* dan *Secure* flags).

# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  
###  1. Implementasikan fungsi untuk menghapus dan mengedit product
Yang pertama saya lakukan adalah dengan membuat fungsi baru bernama ```delete_product``` dan ```edit_product``` yang menerima parameter ```request``` dan ```id``` pada ```views.py```. Lalu mengimport fungsi delete dan edit pada forlder ```urls.py``` dan menambahkan *path url* kedalam ```urlpatters```. Setelah itu ubah kode di <td> terakhir pada ```main.html```. 
### 2. Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
Pada kustomisasi halaman login, register, dan tambah produk saya menggunakan warna palatte #322D29, #72383D, #AC9C8D, #D1C7BD, #D9D9D9, #EFE9E1
### 3. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive.
Pada tahap ini yang saya lakukan adalah menambah 3 fitur pada navbar, yaitu home, product, dan profile. 

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!   
### 1. Inline Sytles 
CSS yang ditulis langsung di dalam atribut style pada elemen HTML memiliki prioritas tertinggi. Contoh: ```<div style="color: red;">```.
### 2. ID Selectors 
Selector yang menggunakan ID (dikenali dengan simbol #) memiliki prioritas tinggi kedua. Contoh: ```#header```.
### 3. Class, Attribute, dan Pseudo-classes Selectors 
Selector yang menggunakan class (dikenali dengan simbol .), attribute selector, dan pseudo-classes (seperti :*hover*) memiliki prioritas menengah. Contoh: ```.menu, [type="text"], :first-child```.
### 4. Element (Type) Selectors
Selector yang menggunakan nama elemen HTML, seperti div, p, atau h1, memiliki prioritas lebih rendah. Contoh: ```div, p```.

##  Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!  
Responsive design menjadi konsep penting dalam pengembangan aplikasi web karena tampilan dan fungsionalitas aplikasi dapat disesuaikan dengan ukuran layar dan resolusi perangkat yang berbeda, sehingga meningkatkan pengalaman pengguna. Contoh aplikasi yang sudah menerapkan responsive design adalah situs web e-commerce seperti Amazon dan eBay, yang menyesuaikan layout dan konten mereka agar mudah diakses di berbagai perangkat. Sementara itu, contoh aplikasi yang belum menerapkan responsive design adalah beberapa situs berita lama atau blog yang masih memiliki layout tetap, sehingga tampilan mereka menjadi tidak optimal saat diakses melalui perangkat mobile, mengurangi kenyamanan pengguna.

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Padding adalah ruang untuk mengosongkan area di sekitar konten (transparan), Border adalah garis tepian yang membungkus konten dan padding-nya, dan Margin adalah ruang untun mengosongkan area di sekitar border (transparan).  
``` 
div {
  width: 300px;
  border: 15px solid green;
  padding: 50px;
  margin: 20px;
}
```  

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!  
Flexbox adalah model layout CSS yang memungkinkan pengembang untuk menyusun elemen dalam satu baris atau kolom secara fleksibel dan responsif. Dengan Flexbox, elemen dapat dengan mudah diselaraskan, dibagi ruang, dan diatur ukurannya tanpa perlu menggunakan float atau positioning. Flexbox digunakan untuk tata letak satu dimensi (baris atau kolom), cocok untuk elemen-elemen yang perlu diatur dalam satu arah.
Grid Layout adalah model layout CSS yang memungkinkan pengembang untuk membagi halaman menjadi grid dua dimensi, terdiri dari baris dan kolom. Dengan Grid Layout, elemen dapat ditempatkan secara tepat di dalam grid, memberikan kontrol yang lebih besar atas tata letak dibandingkan dengan model layout lainnya. Grid Layout lebih cocok untuk tata letak dua dimensi (baris dan kolom), memberikan fleksibilitas lebih besar untuk desain halaman yang lebih kompleks.    

# Tugas 6: JavaScript dan AJAX
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
### AJAX GET
* *Ubahlah kode cards data mood agar dapat mendukung AJAX GET.*  
Pada file  `main/template/main.html`, tambahkan elemen `<div>` yang akan digunakan untuk menampilkan daftar product. Kemudian, tambahkan kode JavaScript untuk mengambil data product menggunakan `fetch()` dan menampilkannya secara dinamis.  
* *Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.*    
Membuat fungsi `getProductEntries()` yang mengambil data product dari server menggunakan AJAX dan memastikan URL mengarah ke *endpoint*. 
### AJAX POST  
* Menambahkan tombol di halaman utama untuk membuka modal  
* Modal di-trigger dengan menekan suatu tumbol pada halaman utama  
`<button onclick="showModal()">Add Product</button>`
* Saat penambahan product berhasil maka modal harus ditutu dengan memanggil fungsi `hideModal()` dan reset form
* Jika penambahan gagal, maka menampilkan pesan error menggunakan `alert()` atau elemen didalam modal.
* Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.  
```
@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) 
    price = request.POST.get("price")
    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```
* Buatlah path /create-ajax/:
``` path('create-product-ajax', add_product_ajax, name='add_product_ajax'),```  
* Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
``` 
 <form id="ProductForm">
          <div class="mb-4">
            <label for="name" class="block text-sm font-medium text-[#322D29]">Product Name</label>
            <input type="text" id="name" name="name" class="mt-1 block w-full border border-[#AC9C8D] rounded-md p-2 hover:border-[#72383D]" placeholder="Enter your product name" required>
          </div>
  <form>
``` 
* Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
Setelah menambahkan product, panggil ``` refreshProductEntries()```  untuk memperbarui tampilan product tanpa memuat ulang halaman utama.  

## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!  
JavaScript sangat bermanfaat dalam pengembangan aplikasi web karena memungkinkan interaksi yang dinamis dan responsif antara halaman web dan pengguna. Dengan eksekusi di sisi client, JavaScript mengurangi beban server dan mempercepat pemuatan halaman melalui caching file eksternal. Selain itu, JavaScript mendukung event-driven programming, memungkinkan kode hanya dijalankan ketika terjadi peristiwa tertentu. Kemampuannya untuk memanipulasi DOM secara langsung juga mempermudah pembaruan konten tanpa memuat ulang halaman, sehingga meningkatkan pengalaman pengguna secara keseluruhan.  

## Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi `await` dalam penggunaan `fetch()` adalah untuk menunggu hingga permintaan HTTP selesai sebelum melanjutkan eksekusi kode berikutnya. Jika `await` tidak digunakan, `fetch()` hanya mengembalikan *Promise* yang belum selesai, sehingga kode di bawahnya mungkin dieksekusi sebelum respons diterima, yang bisa menyebabkan error atau data yang belum siap. Dengan `await`, kita dapat memastikan proses asynchronous berjalan lebih teratur dan hasil dari fetch diproses setelah datanya tersedia.  

## Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Decorator `@csrf_exempt` digunakan pada view untuk AJAX POST agar Django tidak memeriksa token CSRF, sehingga request POST dapat diterima tanpa error. Ini diperlukan jika token CSRF tidak dikirim dengan request, tetapi harus digunakan dengan hati-hati karena dapat membuka celah keamanan.

## Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data input pengguna dilakukan di belakang karena validasi di frontend saja tidak cukup untuk mencegah ancaman keamanan seperti Cross-Site Scripting (XSS). Meskipun pembersihan di frontend menggunakan DOMPurify dapat melindungi saat data ditampilkan di browser, data yang dikirim ke server tetap berpotensi berbahaya jika tidak dibersihkan di backend. Dalam tutorial ini, fungsi `strip_tags` di backend digunakan untuk menghilangkan semua tag HTML dari input pengguna sebelum data tersebut disimpan di basis data. Ini melindungi aplikasi dari serangan Stored XSS, di mana data berbahaya dapat tersimpan di server dan dieksekusi saat ditampilkan kepada pengguna lain. Pembersihan di backend memastikan data yang disimpan aman, terlepas dari apakah pengguna memanipulasi kode frontend.