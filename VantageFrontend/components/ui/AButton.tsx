
interface AButtonProp {
    text: string;
    href: string;
    classes?: string;
    danger?:boolean;
}


export default function AButton({text, href, classes="", danger=false}: AButtonProp) {
  return (
    <a href={href} className={`center mt-2 text-white rounded-xl p-2 hover:shadow-2xl m-2 ${classes} ${danger ? "bg-red-500" : "bg-neutral-900"}`} >{text}</a>
  )
}
