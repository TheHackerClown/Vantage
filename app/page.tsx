
import Image from "next/image";
import Link from "next/link";


export default function Home() {
  return (
    <div className='text-center bg-gray-800 text-white p-10 items-center flex h-fit w-fit flex-col rounded-2xl animate__animated animate__fadeIn'>
      <Image src={"/favicon.ico"} alt='Vantage' className="p-2 self-center" width={80} height={80}/>
      <h1 className="text-4xl font-bold mt-4">Welcome to Vantage</h1>
      <p className="text-lg mt-2">A Payroll Software Exclusively for Compliance Related Salary Preparation</p>
      <br />
      <Link href="/dashboard" className="bg-red-400 p-5 text-2xl rounded-2xl hover:bg-red-300 hover:scale-110 transition-all ">Start Vantage</Link>
    </div>
      );
}

