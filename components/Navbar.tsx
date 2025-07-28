import Image from 'next/image';
import Link from 'next/link';


export default function Navbar() {

    return (<>
    <nav className="w-full border-b-2 h-1/13 flex flex-row justify-between items-center bg-gray-800 text-white p-5 mt-1">
      <div className="flex flex-row items-center" draggable="false" >
        <Image src="/favicon.ico" alt="Vantage" width={40} height={40} />
        <h2 className="text-2xl font-bold">Vantage</h2>
      </div>
      <div className="flex items-center self-center">
        <h2>Working on: <strong>Generic Pharma Company</strong> | Selected Month: <strong>{new Date().toLocaleString('default', { month: 'long' })} {new Date().getFullYear()}</strong></h2>

      </div>
      <div className="flex float-right items-center self-center">
        <Link href="/" className="p-2 bg-red-500 border-b-2 hover:bg-red-400 hover:border-b-0 rounded-2xl">
          Logout
        </Link>
      </div>
    </nav></>);
}