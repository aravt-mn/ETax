import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';

function ItemsTable() {
  const [items, setItems] = useState([]);
  const [selectionModel, setSelectionModel] = useState([]);

  useEffect(() => {
    fetch('/api/items')
      .then(response => response.json())
      .then(data => setItems(data));
  }, []);

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'SKU', headerName: 'SKU', width: 130 },
    { field: 'barcode', headerName: 'Barcode', width: 130 },
    { field: 'itemName', headerName: 'Item Name', width: 200 },
    { field: 'itemNameEn', headerName: 'Item Name (EN)', width: 200 },
    { field: 'classificationCode', headerName: 'Classification Code', width: 200 },
    { field: 'productTypeCode', headerName: 'Product Type Code', width: 200 },
    { field: 'productTypeName', headerName: 'Product Type Name', width: 200 },
    { field: 'productCategory', headerName: 'Product Category', width: 200 },
    { field: 'productPercent', headerName: 'Product Percent', width: 200 },
    { field: 'productSize', headerName: 'Product Size', width: 200 },
    { field: 'unitCode', headerName: 'Unit Code', width: 200 },
  ];

  const rows = items.map(item => ({
    id: item.id,
    SKU: item.SKU,
    barcode: item.barcode,
    itemName: item.itemName,
    itemNameEn: item.itemNameEn,
    classificationCode: item.classificationCode,
    productTypeCode: item.productTypeCode,
    productTypeName: item.productTypeName,
    productCategory: item.productCategory,
    productPercent: item.productPercent,
    productSize: item.productSize,
    unitCode: item.unitCode,
  }));

  const handleSelectionModelChange = (newSelection) => {
    setSelectionModel(newSelection.selectionModel);
  };

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        checkboxSelection
        selectionModel={selectionModel}
        onSelectionModelChange={handleSelectionModelChange}
      />
    </div>
  );
}

function DashboardAppPages() {
  return (
    <div>
      <h1>Бүтээгдэхүүний жагсаалт</h1>
      <ItemsTable />
    </div>
  );
}

export default DashboardAppPages;