

import type { Metadata } from "next";
import "../globals.css";
import DashLogo from "@/components/ui/DashLogo";

export const metadata: Metadata = {
  title: "Vantage",
  description: "Payroll Saas by Dhruv",
};

export default function DashboardLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`sakura center column h-dvh overflow-hidden w-dvw`}
      >
        <div className="rounded-xl w-12/13 h-12/13 bg-neutral-800 overflow-hidden">
    
        <DashLogo/>
        
        {children}
    </div>
        
      </body>
    </html>
  );
}
