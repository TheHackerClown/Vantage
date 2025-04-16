"use client";

import { useState } from "react";
import AButton from "./ui/AButton"
import VInput from "./ui/VInput"



const CreateCompany = () => {

    const [selectedcompname, setSelectedCompName] = useState<string>("");
  return (<><form action="#" className="w-full h-dvh column center pb-40">
    <h1 className="text-3xl text-white text-center m-1" >Create Company</h1>
    <VInput type="text" name="comp-name" classes="w-fit" placeholder="Company Name" value={selectedcompname} onchangeval={setSelectedCompName}/>
    <VInput type="text" name="comp-name" classes="w-fit" placeholder="Company Name" value={selectedcompname} onchangeval={setSelectedCompName}/>
    <VInput type="text" name="comp-name" classes="w-fit" placeholder="Company Name" value={selectedcompname} onchangeval={setSelectedCompName}/>
    <VInput type="text" name="comp-name" classes="w-fit" placeholder="Company Name" value={selectedcompname} onchangeval={setSelectedCompName}/>
    <VInput type="text" name="comp-name" classes="w-fit" placeholder="Company Name" value={selectedcompname} onchangeval={setSelectedCompName}/>
    <AButton text="Create" href="/dashboard" classes="w-xs"/>
  </form></>
  )
}

export default CreateCompany