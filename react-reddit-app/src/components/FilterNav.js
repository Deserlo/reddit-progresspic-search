import React, { useState, useEffect } from "react";

const getItems = () => fetch("/home").then((res) => res.json());

function FilterNav() {

  const [items, setItems] = useState([]);

  useEffect(() => {
    getItems().then((data) => setItems(data));
  }, []);

    function handleSubmit(e) {
      e.preventDefault();
      console.log("submit");
      let items = fetch('/search').then(res => res.json()).then(res => console.log(res));
      setItems(items);
    }
    return (
      <div>
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
        <div items={items}></div>
      </div>
    );
}

export default FilterNav;
