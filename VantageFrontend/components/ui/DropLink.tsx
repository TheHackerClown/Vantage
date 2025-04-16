interface DropLinkProp {
    href: string;
    text: string;
}

export default function DropLink({text, href}: DropLinkProp){
  return (<>
  <a href={href}>
  <li className="px-4 py-2 hover:bg-gray-500">{text}</li></a></>
  )
}
