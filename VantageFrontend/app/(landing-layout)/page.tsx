
import AButton from "@/components/ui/AButton";


//Main Landing Page
export default function Home() {

  return (<>
    <h2 className="text-white text-2xl">It is a Payroll Software as a Service,</h2>
    <h2 className="text-white text-2xl">Made using Next.js and Django</h2>
    <AButton href="/login" text="Continue"/>
    </>);
}