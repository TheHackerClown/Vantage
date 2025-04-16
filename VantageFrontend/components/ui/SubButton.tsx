interface SubButtonProp {
    text: string;
}


const SubButton = ({text}: SubButtonProp) => {
  return (
    <input type="submit" className="center bg-neutral-900 mt-4 text-white rounded-xl p-2 hover:shadow-2xl m-2" >{text}</input>
  )
}

export default SubButton