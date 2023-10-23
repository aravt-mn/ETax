drop table ultimate_inventory_list;
CREATE TABLE ultimate_inventory_list (
                    isbn VARCHAR(50),
                    invtID VARCHAR(50),
                    descr NVARCHAR(255),
                    tranStatus VARCHAR(50))

drop table inventory_list;
CREATE TABLE inventory_list (
                    barcode VARCHAR(50),
                    barcodeName NVARCHAR(255),
                    classificationCode VARCHAR(50),
                    productTypeCode VARCHAR(50),
                    productTypeName NVARCHAR(255),
                    productCategory NVARCHAR(255),
                    productPercent DECIMAL(10, 2),
                    productSize INT null,
                    unitCode NVARCHAR(50))