product:
    - name 
    - image ---> images
    - price
    - sku
    - brand
    - category
    - tage
    - description
    - subtitle
    - reviews
    - flag [new,sale,feature]
    - video 

category:
    - name
    - image

brand:
    - name
    - image

orders:
    - id 
    - addrees
    - totalItemes
    - orderDate
    - DeliveryTime
    - Order Time
    - TotalAmount

user:
    - name
    - email
    - addrees
    - phone
    - image
    - favorate

- extend user:
    - Baise user
    - AbstractBaseUser
    - one-to-one model