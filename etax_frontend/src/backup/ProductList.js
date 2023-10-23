import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';

function ProductList() {
  const [products, setProducts] = useState([]);
  const [selectionModel, setSelectionModel] = useState([]);

  useEffect(() => {
    fetch('/api/products')
      .then(response => response.json())
      .then(data => setProducts(data));
  }, []);

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'barcode', headerName: 'BarCode', width: 130 },
    { field: 'sku', headerName: 'SKU', width: 90 },
    { field: 'name', headerName: 'Name', width: 130 },
  ];

  const rows = products.map(product => ({ id: product.id, barcode: product.barcode, sku: product.sku, name: product.name }));

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

export default ProductList;