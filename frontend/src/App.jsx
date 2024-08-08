import './App.css';
import NavBarGlobal from './components/NavBarGlobal';
import DashboardLayout from './components/DashboardLayout';

/**
 * @summary renders the app entry point
 * @returns 
 */
function App() {
  return (
    <div>
      <NavBarGlobal/>
      <DashboardLayout/>
    </div>
  );
}


export default App;
