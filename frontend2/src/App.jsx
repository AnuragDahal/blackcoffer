import { useState } from 'react'
import './App.css'
import Dashboard from './assets/charts/Chart'
import Filter from './assets/charts/Filter'
import { Route, Routes } from 'react-router-dom'
import Layout from './Layout'

function App() {
  const [openSidebarToggle, setOpenSidebarToggle] = useState(false)

  const OpenSidebar = () => {
    setOpenSidebarToggle(!openSidebarToggle)
  }

  return (

    <Routes>
      <Route path='/' element={
        <Layout>
          <Dashboard/>
        </Layout>
      }/>
      
      <Route path='/filters' element={
        <Layout>
          <Filter/>
        </Layout>
      }/>
    </Routes>
  )
}

export default App