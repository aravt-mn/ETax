CREATE TABLE etax.ProductType (
    id INT PRIMARY KEY,
    category_code VARCHAR(2),
    category_name nVARCHAR(255)
);

--truncate table etax.ProductType;

INSERT INTO etax.ProductType  (id, category_code, category_name)
VALUES (1, '01', N'Спирт'),
       (2, '02', N'Цагаан архи, ликёр, кордиал ба спиртлэг бусад ундаа'),
       (3, '03', N'Коньяк, виски, ром, джин'),
       (4, '04', N'Шимийн архи'),
       (5, '05', N'Дарс'),
       (6, '06', N'Пиво'),
       (7, '07', N'Янжуур тамхи'),
       (8, '08', N'Дүнсэн тамхи'),
       (9, '09', N'Автобензин'),
       (10, '10', N'Дизелийн түлш'),
       (11, '11', N'Газрын тосны үйлдвэрлэлийн дайвар бүтээгдэхүүн, керосин');