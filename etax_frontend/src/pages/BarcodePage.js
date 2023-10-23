import React, { useState, useEffect } from 'react';
import { Container, Pagination } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import Box from '@mui/material/Box';
import LoadingButton from '@mui/lab/LoadingButton';
import SendIcon from '@mui/icons-material/Send';

export default function BarcodePage() {
  const [inventoryData, setInventoryData] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);

  const fetchInventoryData = async (page) => {
    const response = await fetch(`/api/inventorylist/${page}`);
    const data = await response.json();
    setInventoryData(data);
  };

  useEffect(() => {
    fetchInventoryData(currentPage);
  }, [currentPage]);

  const handlePageChange = (event, page) => {
    setCurrentPage(page);
  };
  const [loading, setLoading] = React.useState(true);
  function handleClick() {
    setLoading(true);
  }

  const handleRefreshClick = () => {
    fetch('/api/inventorylist/refresh')
      .then(response => response.json())
      .then(data => setInventoryData(data));
  };

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'barcode', headerName: 'Barcode', width: 200 },
    { field: 'barcodeName', headerName: 'Barcode Name', width: 200 },
    { field: 'classificationCode', headerName: 'Classification Code', width: 200 },
    { field: 'productTypeCode', headerName: 'Product Type Code', width: 200 },
    { field: 'productTypeName', headerName: 'Product Type Name', width: 200 },
    { field: 'productCategory', headerName: 'Product Category', width: 200 },
    { field: 'productPercent', headerName: 'Product Percent', width: 200 },
    { field: 'productSize', headerName: 'Product Size', width: 200 },
    { field: 'unitCode', headerName: 'Unit Code', width: 200 },
    { field: 'loaddatetime', headerName: 'Load Date', width: 200 },
  ];

  const rows = inventoryData.map((item) => ({
    id: item.id,
    barcode: item.barcode,
    barcodeName: item.barcodeName,
    classificationCode: item.classificationCode,
    productTypeCode: item.productTypeCode,
    productTypeName: item.productTypeName,
    productCategory: item.productCategory,
    productPercent: item.productPercent,
    productSize: item.productSize,
    unitCode: item.unitCode,
    loaddatetime: item.loaddatetime,
  }));

  return (
    <Container>
      <h1>Barcode List</h1>

      <Box sx={{ display: 'flex' }}>
        <LoadingButton
          onClick={handleClick}
          endIcon={<SendIcon />}
          loading={false}
          loadingPosition="start"
          variant="contained"
        >
          <span>Refresh Inventory List</span>
        </LoadingButton>
        {console.log('Inventory List Refreshed')}
      </Box>
      <div style={{ height: 400, width: '100%' }}>
        <DataGrid rows={rows} columns={columns} pageSize={10} />
      </div>
      <Pagination
        className="justify-content-center"
        size="lg"
        page={currentPage}
        count={10}
        onChange={handlePageChange}
      />
    </Container>
  );
}