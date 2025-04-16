"use client";
import { useLayoutStore } from "@/app/services/heading";
import DropLink from "@/components/ui/DropLink";
import MenuButton from "@/components/ui/MenuButton";
import VDropdown from "@/components/ui/VDropdown";
import { useParams } from "next/navigation";



export default function Page() {
    const setHeading = useLayoutStore((state)=> state.setHeading);
    
    /* eslint-disable @typescript-eslint/no-explicit-any */
    const params:any = useParams();
    /* eslint-enable @typescript-eslint/no-explicit-any */
    setHeading(decodeURIComponent(params.compname));
    
    return (<>
  
        <div className="row m-1">
          <VDropdown title="Employer">
            <DropLink text="Employee Creation" href={`/${decodeURIComponent(params.compname)}/emp_create`}/>
          </VDropdown>
          <MenuButton text="Files" />

          <MenuButton text="Muster-Roll" />
          <MenuButton text="Setup" />
          <MenuButton text="Company Edit" />
          </div>
    <hr />  
    </>)
  }