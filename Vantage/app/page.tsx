
import Logo from "@/components/ui/logo";


export default function Home() {

  return (<><div className="rounded-xl p-20 w-1.5xl bg-zinc-700">
    
    <div className="column center mb-4">

    <Logo/> <h1 className="text-white text-4xl font-bold">Vantage</h1>
    
    </div>
    
    <h2 className="text-white text-2xl">It is a Payroll Software as a Service,</h2>
    <h2 className="text-white text-2xl">Made using Next.js and Django</h2>
    <a href="/login" className="center bg-neutral-900 mt-5 text-white rounded-xl p-2 hover:shadow-2xl">Continue</a>
    </div>
    </>);
}