"use client";
import { useLayoutStore } from "@/app/services/heading";
import CreateCompany from "@/components/CreateCompany";
import SelectCompany from "@/components/SelectCompany";


export default function Page (){
  const setHeading = useLayoutStore((state)=> state.setHeading)

  setHeading("Company Manager")
  
  return (<>
        <div className="row ">
          <CreateCompany/>
          <div className="bg-white w-0.5 ml-2 mr-2 h-dvh"></div>
          <SelectCompany/>

          </div>
          </>)
}