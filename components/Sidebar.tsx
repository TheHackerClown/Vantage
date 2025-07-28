import Link from "next/link";



export default function Sidebar() {
  return (
    <div className="w-64 h-full bg-gray-800 text-white p-4">
      <h2 className="text-xl font-bold mb-4">Total Employees: 12</h2>
      <ul>
        <li className="mb-2">
          <Link href="/dashboard" className="hover:text-gray-400">Export Data</Link>
        </li>
        <li className="mb-2">
          <Link href="/dashboard" className="hover:text-gray-400">Delete Employee</Link>
        </li>
        <li className="mb-2">
          <Link href="/dashboard" className="hover:text-gray-400">Bulk Edit Employee</Link>
        </li>
        <li className="mb-2">
          <Link href="/dashboard" className="hover:text-gray-400">Salary Calculate (Monthly)</Link>
        </li>
        <li className="mb-2">
          <Link href="/settings" className="hover:text-gray-400">Settings</Link>
        </li>
        <li className="mb-2">
          <Link href="/exports" className="hover:text-gray-400">Export PDF</Link>
        </li>
      </ul>
    </div>
  );
}