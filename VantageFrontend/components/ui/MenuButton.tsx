
interface MenuButtonProp {
    href?: string;
    text: string;
}

const MenuButton = ({text, href="#"}: MenuButtonProp) => {
  return (<>
  <a href={href} className="text-white hover:border-b-2 ml-4">{text}</a>
  </>
  )
}

export default MenuButton