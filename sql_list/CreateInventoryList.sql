CREATE TABLE [Etax].[InventoryList](
	[barcode] [varchar](50) NULL,
	[barcodeName] [nvarchar](255) NULL,
	[classificationCode] [varchar](50) NULL,
	[productTypeCode] [varchar](50) NULL,
	[productTypeName] [nvarchar](255) NULL,
	[productCategory] [nvarchar](255) NULL,
	[productPercent] [decimal](10, 2) NULL,
	[productSize] [int] NULL,
	[unitCode] [nvarchar](50) NULL,
	[LOAD_DATETIME] [datetime] NOT NULL
) ON [PRIMARY]
GO

ALTER TABLE [Etax].[InventoryList] ADD  DEFAULT (getdate()) FOR [LOAD_DATETIME]