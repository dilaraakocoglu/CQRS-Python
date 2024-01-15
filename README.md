# CQRS Project

Bu proje, Command Query Responsibility Segregation (CQRS) mimarisini kullanarak bir örnek uygulamayı içermektedir.

## Proje Açıklaması

Projenin temel amacı, yazma (write) ve okuma (read) işlemlerini ayrı veritabanları üzerinde gerçekleştirmek ve bu işlemleri CQRS prensiplerine uygun şekilde yönetmektir.

### Teknolojiler

- Python
- FastAPI
- SQLAlchemy
- Diator

### Yapı

Projede aşağıdaki ana bileşenler bulunmaktadır:

- **Write Database (write_db):** Yazma işlemlerini gerçekleştiren PostgreSQL veritabanı.
- **Read Database (read_db):** Okuma işlemlerini gerçekleştiren PostgreSQL veritabanı.
- **FastAPI:** Web API'yi oluşturan Python web framework'ü.
- **Diator:** Mediator (aracı) deseni üzerine inşa edilen ve CQRS işlemlerini yöneten kütüphane.

## Kurulum

Projenin çalışması için Docker ve Docker Compose gereklidir. Aşağıdaki adımları izleyerek projeyi başlatabilirsiniz:

1. Repoyu klonlayın:

    ```bash
    git clone
    cd cqrs-proje
    ```

2. Docker Compose kullanarak servisleri başlatın:

    ```bash
    docker-compose up -d
    ```

3. Web API'yi çalıştırın:

    ```bash
    uvicorn main:app --reload
    ```

Proje başarıyla çalıştığında [http://localhost:8000/docs](http://localhost:8000/docs) adresine giderek Swagger belgelerine erişebilirsiniz.

## API Endpoints

- **POST /products/:** Yeni bir öğe ekler.
- **GET /products/:** Tüm öğeleri listeler.


## Lisans

Bu proje [MIT lisansı](LICENSE) altında lisanslanmıştır.
