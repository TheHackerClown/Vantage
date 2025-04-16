
interface VDropdownProp {
  title:string;
  children: React.ReactNode
}

export default function VDropdown({title, children} : VDropdownProp){
  return (<>
  <li className="relative group">
          <button className="hover:border-b-2 ml-4 text-white cursor-pointer">{title}</button>

          <div className="absolute top-full left-0 mt-2
            w-48 bg-neutral-700 text-white rounded shadow-lg
            invisible opacity-0 scale-95
            group-hover:visible group-hover:opacity-100 group-hover:scale-100
            transition-all duration-200 z-50
            pointer-events-auto">
            <ul className="py-2">
              {children}
            </ul>
          </div>
        </li>
        </>
  )
}
