"use client";

import VTable from "@/components/ui/VTable";
import { useState } from "react";


export default function Page() {
    const [data, setData] = useState([
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
      ]);
      const heading = ["Company Name", "Address", "Contact Number"]
      const keys = ["username", "address", "phoneno"]

    return (<>
    <div className="center row">
    
        <VTable heading={heading} keys={keys} data={data}/>
        
        <button className="text-white bg-black text-2xl p-2 rounded-xl ml-32 z-50" onClick={()=>{setData([...data, {
          "id": 5,
          "username": "lwilliams Contractors",
          "address": "654 Cedar Lane, Denver, CO 80202",
          "phoneno": "555-789-0123"
        }])}}>Hehe</button>
    </div></>);
}