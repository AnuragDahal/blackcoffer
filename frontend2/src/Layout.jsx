import { Children, useState } from 'react'
import React from 'react'
import './App.css'
import Header from './Header'
import Sidebar from './Sidebar'

function Layout({children}) {
  const [openSidebarToggle, setOpenSidebarToggle] = useState(false)

  const OpenSidebar = () => {
    setOpenSidebarToggle(!openSidebarToggle)
  }

  return (

    <div style={{
      display: "flex",
      flexDirection: "row",
      height:"100vh"
    }}>
      <Sidebar openSidebarToggle={openSidebarToggle} OpenSidebar={OpenSidebar}/>
      <div
      style={{
        display:"flex",
        flexDirection: "column",
        gap:"40px",
        height:"100vh",
        overflowY:"scroll",
        width:"calc(100vw - 200px)",
      }}
      >

      <Header OpenSidebar={OpenSidebar}/>
    {children}
      </div>
    </div>
  )
}
export default Layout