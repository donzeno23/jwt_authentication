import { Routes, Route } from "react-router-dom";
import { RequireToken } from "./context/Auth";

// import Login from './components/Login';
import Login from './components/LoginButton';
import Register from './components/Register';
import Admin from './components/Admin';
import Profile from './components/Profile';
import Client from './components/Client';
import Vendor from './components/Vendor';

function App() {
  return (
    <div className ="App">
      <Routes>
        <Route path="/" element = {<Login/>}/>
        <Route path="/register" element = {<Register/>}/>
        <Route
          path="/profile"
          element={
            <RequireToken>
              <Profile />
            </RequireToken>
          }
        />
        <Route 
          path="/admin" 
          element = {
            <RequireToken>
              <Admin />
            </RequireToken>
          }
        />
        <Route 
          path="/client" 
          element = {
            <RequireToken>
              <Client />
            </RequireToken>
          }
        />
        <Route 
          path="/vendor" 
          element = {
            <RequireToken>
              <Vendor />
            </RequireToken>
          }
        />
      </Routes>
    </div>
  );
}

export default App;
