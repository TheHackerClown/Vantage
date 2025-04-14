import Logo from "@/components/ui/logo";

const page = () => {

  return (
    <div className="rounded-xl p-10 w-1.5xl bg-neutral-800">
    
    <div className="column center mb-4">

    <Logo/> <h1 className="text-white text-4xl font-bold">Vantage Login</h1>
    
    </div>
    <hr className="mb-4"/>
    <form action="/" className="column">
    <h2 className="text-white p-1 text-2xl center">Enter Your Access Token</h2>
    <input type="password" name="password" className="border-2 h-10 mt-2 rounded-xl text-white text-center" placeholder="Enter Here" required={true}/>
    <button type="submit" className="center bg-neutral-900 mt-4 text-white rounded-xl p-2 hover:shadow-2xl">Login</button>
    </form>
    <hr className="mt-5"/>
    <div className="center row w-full"> <a className="center bg-neutral-900 mt-4 text-white rounded-xl p-2 hover:shadow-2xl m-2" >Forget Token?</a> <a className="center m-2 bg-neutral-900 mt-4 text-white rounded-xl p-2 hover:shadow-2xl" >Register Yourself</a></div>
    
    </div>
  )
}

export default page