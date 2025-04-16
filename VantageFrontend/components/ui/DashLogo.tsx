"use client";
import { useLayoutStore } from "@/app/services/heading";
import Logo from "./BaseLogo";
import AButton from "./AButton";

export default function DashLogo() {
    const heading = useLayoutStore((state) => state.heading);
    
    return (<>
    <div className="column row">
        <Logo classnames="aspect-square w-18 pixel p-1"/>
        <h1 className="text-white pt-1 pb-1 pl-2 pr-2 mt-auto mb-auto hover:border-b-2 text-2xl" >{heading}</h1>
        <AButton href="/" text="Logout" danger={true} classes="p-1 mt-0.5 mr-5 ml-auto"/>
    </div>
    <hr />
    </>)
}