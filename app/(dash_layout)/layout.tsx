import "@/app/globals.css";
import "animate.css"
import React from "react";



export default function DashboardLayout({
  children
} : {children: React.ReactNode}) {
  return (
    <div className='text-center bg-gray-800 text-white items-center flex flex-col rounded-2xl h-11/12 w-11/12 overflow-hidden animate__animated animate__fadeIn'>
      {children}
    </div>
        
  );
}
