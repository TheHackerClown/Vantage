import type { Metadata } from "next";
import "./globals.css";

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
        {children}
      </body>
    </html>
  );
}
