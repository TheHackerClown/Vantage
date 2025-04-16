"use client";

import { useState } from "react"
import VInput from "./ui/VInput"
import AButton from "./ui/AButton"


const SelectCompany = () => {
    const iter = [
        {
          "id": 1,
          "username": "jdoe Corp",
          "address": "123 Maple Street, Springfield, IL 62704",
          "phoneno": "555-123-4567"
        },
        {
          "id": 2,
          "username": "asmith LLC",
          "address": "456 Oak Avenue, Portland, OR 97205",
          "phoneno": "555-987-6543"
        },
        {
          "id": 3,
          "username": "mlee PVT. LTD.",
          "address": "789 Pine Road, Austin, TX 73301",
          "phoneno": "555-246-8101"
        },
        {
          "id": 4,
          "username": "kpatel INFRA",
          "address": "321 Birch Blvd, Miami, FL 33101",
          "phoneno": "555-369-1470"
        },
        {
          "id": 5,
          "username": "lwilliams Contractors",
          "address": "654 Cedar Lane, Denver, CO 80202",
          "phoneno": "555-789-0123"
        }
      ]
      
      const [activeRow, setActiveRow] = useState<number | undefined>(undefined);
      const [selectedcompname, setSelectedCompName] = useState<string>("");

  return (<>
  <div className="w-full h-dvh column center pb-40 ">
    <h1 className="text-3xl text-white p-2 text-center" >Select Company</h1>
    <table className="bg-neutral-600 rounded-2xl">
        <thead className="text-white">
            <tr>
                <th>
                    Company Name
                </th>
                <th>
                    Address
                </th>
                <th>
                    Contact Number
                </th>
            </tr>
        </thead>
        <tbody>
        {iter.map((row) => (
            <tr
              key={row.id}
              onClick={() => {
                setActiveRow(row.id);
                setSelectedCompName(row.username);
              }}
              className={`cursor-pointer ${
                activeRow === row.id ? "bg-blue-100 rounded-2xl" : "hover:bg-gray-50 bg-slate-400"
              }`}
            >
              <td className="px-4 py-2 border-b">{row.username}</td>
              <td className="px-4 py-2 border-b">{row.address}</td>
              <td className="px-4 py-2 border-b">{row.phoneno}</td>
            </tr>
          ))}
        </tbody>
    </table>
    <VInput name="comp-name" type="text" disable={true} placeholder="Company Name" value={selectedcompname} onchangeval={setSelectedCompName}/>
    <AButton href={`/${selectedcompname}`} text="Open Company"/>
    </div></>
  )
}

export default SelectCompany