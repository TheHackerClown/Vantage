interface VTableProp {
    heading: string[];
    keys: string[];
    /* eslint-disable @typescript-eslint/no-explicit-any */
    data: any[];
    /* eslint-enable @typescript-eslint/no-explicit-any */
}

export default function VTable({heading, keys, data}: VTableProp) {
    return (<>
    <div className="max-w-5xl max-h-dvh overflow-auto">
    <table className="bg-neutral-600 text-center rounded-xs overflow-auto">
        <thead className="text-white">
            <tr>
                {heading.map((val)=>(<th key={Math.random().toString(3)} className="cursor-default p-2 text-2xl">
                    {val}
                </th>))}
            </tr>
        </thead>
        <tbody>
        {data.map((row) => (
            <tr key={Math.random().toString(3)} className="bg-blue-200" contentEditable suppressContentEditableWarning>
                {keys.map((val)=>(<td key={Math.random().toString(3)}  className="px-4 py-2 hover:bg-blue-300 text-xl border-b-2 border-black rounded-xl">{row[val]}</td>))}
            </tr>
          ))}
        </tbody>
    </table></div>
    </>);
}