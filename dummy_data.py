import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


import django
django.setup()



# import ----> functions
from faker import Faker
import random
from products.models import product, Brand, Category



def seed_brand(n):
    faker = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.png', '6.jpeg', '7.png']

    for _ in range(n):
        name = faker.name()
        image = f"brands/{images[random.randint(0, 6)]}"
        Brand.objects.create(
            name = name,
            image = image
        )
    print(f"Successfully seeded {n} brand")

def seed_category(n):
    faker = Faker()
    images = ['1.png', '2.jpg', '3.jpg', '4.jpg', '5.png', '6.jpeg']

    for _ in range(n):
        name = faker.name()
        image = f"category/{images[random.randint(0, 5)]}"
        Category.objects.create(
            name = name,
            image = image
        )
    print(f"Successfully seeded {n} category")

def seed_product(n):
    faker = Faker()
    images = ['1.png', '2.jpg', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.png']
    flagtype = ['New', 'Feature', 'Sale']

    for _ in range(n):
        name = faker.name()
        image = f"products/{images[random.randint(0, 15)]}"
        flag = flagtype[random.randint(0,2)]
        sku = random.randint(2457, 5245365)
        price = round(random.uniform(66.85, 700.85),2)
        subtitle = faker.text(max_nb_chars=500)
        desc = faker.text(max_nb_chars=10000)
        category = Category.objects.get(id=random.randint(32, 141))
        brand = Brand.objects.get(id=random.randint(31,143))

        product.objects.create(
            name = name,
            image = image,
            flag=flag,
            sku = sku ,
            price = price,
            subtitle=subtitle,
            desc = desc,
            category = category,
            brand = brand,
            video_url="https://www.youtube.com/watch?v=NRUGWNK_G28"
        )
    print(f"Successfully seeded {n} Products")



# seed_brand(100)
# seed_category(100)
seed_product(3000)


