import React, { useState } from 'react';
import { Grid, Paper, Avatar, TextField, Button, Typography, Link } from '@mui/material';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Хэрэглэгчийн нэр эсвэл нууц үгээ шалгана уу');
        }
      })
      .then(data => {
        localStorage.setItem('token', data.token);
        
      })
      .catch(error => {
        setError(error.message);
      });
  };

  const paperStyle = { padding: 20, height: '70vh', width: 280, margin: '20px auto' };
  const avatarStyle = { backgroundColor: '#1bbd7e' };
  const btnstyle = { margin: '8px 0' };

  return (
    <Grid>
      <Paper elevation={10} style={paperStyle}>
        <Grid align="center">
          <Avatar style={avatarStyle}>
            <LockOutlinedIcon />
          </Avatar>
          <h2>ETax Нэвтрэх</h2>
        </Grid>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Хэрэглэгч"
            placeholder="Enter username"
            fullWidth
            required
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <TextField
            label="Нууц үг"
            placeholder="Enter password"
            type="password"
            fullWidth
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <FormControlLabel
            control={
              <Checkbox name="checkedB" color="primary" />
            }
            label="Хэрэглэгчийг сануулах"
          />
          <Button type="submit" color="primary" variant="contained" style={btnstyle} fullWidth>
            Нэвтрэх
          </Button>
          {error && <Typography color="error">{error}</Typography>}
        </form>
        <Typography>
          <Link href="#">Нууц үг мартсан ?</Link>
        </Typography>
      </Paper>
    </Grid>
  );
}

export default Login;