import type { Metadata } from "next";
import "../globals.css";
import CoverLogo from "@/components/ui/CoverLogo";

export const metadata: Metadata = {
  title: "Vantage",
  description: "Payroll Saas by Dhruv",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`sakura center column h-dvh overflow-hidden w-dvw`}
      >
        <div className="rounded-xl p-20 w-1.5xl bg-zinc-700">
          <CoverLogo/>
          {children}
        </div>
      </body>
    </html>
  );
}
