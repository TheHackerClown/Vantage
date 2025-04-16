import Image from "next/image";
import logoimg from "@/app/favicon.ico"

interface LogoProp {
  classnames: string;
}



export default function Logo ({classnames}: LogoProp){
  return (<>
  <Image className={classnames} src={logoimg} alt="Vantage" draggable={false}/></>
  )
}
