import type { Metadata } from "next";
import "./globals.css";
import "animate.css"


export const metadata: Metadata = {
  title: "Vantage",
  description: "A Payroll Software Exclusively for G.P.Singh & Associates",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`antialiased sakura flex flex-col items-center h-dvh justify-center overflow-hidden`}
      >
        <main className="h-dvh w-dvw items-center flex justify-center">{children}</main>
        <footer className="text-center p-4 animate__animated animate__fadeIn">
          <p className="text-gray-500">© {new Date().getFullYear()} Vantage. All rights reserved.</p>
        </footer>
      </body>
    </html>
  );
}
