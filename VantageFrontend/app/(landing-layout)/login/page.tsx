"use client";

import AButton from "@/components/ui/AButton";
import VInput from "@/components/ui/VInput";
import { useState } from "react";
import { useLayoutStore } from "../../services/heading";


export default function Page(){
  const setHeading = useLayoutStore((state)=>state.setHeading);
  setHeading("Vantage Login")

  const [selectedcompname, setSelectedCompName] = useState<string>("");
  return (<>
    <hr className="mb-4"/>
    <form action="/" className="column">
    <h2 className="text-white p-1 text-2xl center">Enter Your Access Token</h2>
    <VInput type="password" name="password" placeholder="Enter Here" required={true} value={selectedcompname} onchangeval={setSelectedCompName}/>
    <AButton href="/dashboard" text="Login"/>
    </form>
    
    <hr className="mt-5"/>
    
    <div className="center row w-full">
      <AButton href="/forgetkey" text="Forget Token?"/>
      <AButton href="/register" text="Register Yourself" />
      </div>
      </>)
}
