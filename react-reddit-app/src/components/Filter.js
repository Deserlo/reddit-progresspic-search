import React, { useState, useEffect } from "react";
import List from './List';

const getItems = () => fetch("/home").then((res) => res.json());

function Filter() {
    const [items, setItems] = useState([]);

    function handleSubmit(e) {
      e.preventDefault();
      console.log("submit");
      fetch('/search').then(res => res.json()).then(res => console.log(res));
    }

    useEffect(() => {
        getItems().then((data) => setItems(data));
      }, []);


    function parentFunction(data_from_child){
        console.log(data_from_child);
    }



    return (
      <div id="Header">
          <h1>Show Me</h1>
        <form action="" onSubmit={handleSubmit}>
          <label>
            Weight Gains
            <input type="checkbox" query="gain" /*onChange={handleValue}*/ />
          </label>
          <label>Weight Loss
              <input type="checkbox" query="loss" /*onChange={handleValue}*/ />
          </label>
          <input type="submit"  method="get" value="Submit"/>
        </form>
      <List functionCallFromParent={this.parentFunction.bind(this)}/>
      </div>
    );
  }

export default Filter;