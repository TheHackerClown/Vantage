interface VInputProps {
    type: string;
    placeholder: string;
    name: string;
    required?: boolean;
    classes?: string;
    disable?: boolean;
    value:string;
    onchangeval: (arg0:string)=>void;
}

export default function VInput({type, placeholder, name, required=false,classes="",value="", disable=false, onchangeval }:VInputProps){
  return (<>
  <input type={type} name={name} className={`border-2 h-10 mt-2 rounded-xl text-white text-center ${classes}`} disabled={disable} placeholder={placeholder} required={required} value={value} onChange={(e)=>onchangeval(e.target.value)} />
  </>
  )
}
