import React,{useState,useEffect} from 'react';
import './App.css';

function App() {
  const [data,setData]=useState([]);
  const getData=()=>{
    fetch('/home'
    ,{
      headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
    }
    )
      .then(function(response){
        console.log(response);
        return response.json();
      })
      .then(function(myJson) {
        console.log(myJson);
        setData(myJson)
      });
  }
  useEffect(()=>{
    getData()
  },[])
  return (
    <div className="App">
     {data.title}
    </div>
  );
}


export default App;
