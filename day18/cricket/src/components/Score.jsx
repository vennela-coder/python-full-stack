import React, { useState } from 'react';
// import '../components./Score.css';

const Score = () =>{

const [runs,setruns]= useState(0);
const [wickets,setwickets]= useState(0);

// let six=()=>{
//     setruns(runs+6)

// }
// let four=()=>{
//     setruns(runs+4)
// }
    
// let one=()=>{
//     setruns(runs+1)
//}

const handleRuns=(run)=>{
    setruns(runs+run)
}


let wicket=()=>{

    if(wickets +1 == 10)

        alert("game over")

    setwickets(wickets+1)
    
}


  return (
    <>
    <div>score
        <h1>Socore : {runs}/{wickets}</h1>

       
    
    
    

    {/* <div className='button'> */}

        <button onClick={()=>handleRuns(6)}>six</button>
        <button onClick={()=>handleRuns(4)}>four</button>
        <button onClick={()=>handleRuns(1)}>one</button>
        <button onClick={wicket}>wicket</button>
    </div>
     {/* </div>  */}

   
    
    </>
  )
}

export default Score