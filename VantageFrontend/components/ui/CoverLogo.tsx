"use client";
import { useLayoutStore } from "@/app/services/heading";
import Logo from "./BaseLogo"

export default function CoverLogo(){
  const heading = useLayoutStore((state) => state.heading);
    return (
    <>
    <div className="column center mb-4">

    <Logo classnames="aspect-square w-25 pixel p-1"/> <h1 className="text-white text-4xl font-bold">{heading}</h1>

</div></>
  )
}