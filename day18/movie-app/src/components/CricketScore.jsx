import React, { useState } from 'react' 
import '../styles/CricketScore.css' ;

const CricketScore = (props) => {
    console.log("props" ,props)
    console.log("targert = " , props.target)
    //states are created here inside the function
    const [runs , setRuns] = useState(0);
    const [wickets , setWickets] = useState(0);
    const [target , setTarget] = useState(props.target);
    const [overs , setOvers] = useState(0.0);
    const [dotballs,setdotballs]=useState(0);
    const [left,setleftOvers]=useState(props.totalOvers);
    let temp = props.totalOvers-  overs



    // const handleSix = () =>{
    //     setRuns(runs + 6);
    // }

    // const handleFour = () =>{
    //     setRuns(runs + 4);
    // }

    

    const handleOne = () =>{
        setRuns(runs + 1);
    }

    const handleRuns = (run) => {
        if(runs + run >= target)
            alert("Target Chased");
        setRuns(runs + run)
    };

    // overs done => "Failed to Chase Target"

    const handleWicket = () =>{

        if(wickets + 1 == 10)
            alert("All Out");

        setWickets(wickets + 1); // it will take some time to update
    }
    const handleovers=() => {
            setOvers(overs+0.1)
            setleftOvers(props.totalOvers-  overs)
    }


const handledotball=()=>{
    setdotballs(dotballs+1)

}


  return (
    <>  <div className='container'>
            <div className='content'>
            <h1>SCORE : {runs} / {wickets}</h1>
            <h2>CURRENT OVERS : {overs}</h2>

          
            <h2>OVERS LEFT :{temp} </h2>
            
            
            <h2>DOTBALLS : {dotballs} </h2>
            </div>
        
        {
            
            wickets < 10 && runs < target && temp > 0?
            <div className='button'>
                <button onClick={()=>handleRuns(6)} >Six</button>
                <button onClick={()=>handleRuns(4)} >Four</button>
                <button onClick={handleWicket} >Wicket</button>
                {
                    //Add 3 2 dotball also
                }
                <button onClick={()=>handleRuns(1)} >One</button>
                <button onClick={()=>handleRuns(2)} >two</button>
                <button onClick={()=>handleRuns(3)} >three</button>
                <button onClick={handledotball}>dotballs</button>
                <button onClick={handleovers}>currentOvers</button>
                
               
            </div>
            :
            <h2>Game Over</h2>

        }
        </div>


    </>
    
  )
}

export default CricketScore