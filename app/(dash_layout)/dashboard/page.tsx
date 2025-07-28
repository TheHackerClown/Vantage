import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import MainContent from "@/components/MainContent";

export default function DashboardPage() {
  return (<>
    <Navbar />
    <div className="flex flex-row h-full w-full">
      <Sidebar />
      <MainContent />
    </div>
  </>);
}
