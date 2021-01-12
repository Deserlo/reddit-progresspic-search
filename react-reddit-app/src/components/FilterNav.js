import React, { useState, useEffect } from "react";

function FilterNav() {

    function handleSubmit(e) {
      e.preventDefault();
      console.log("submit");
      fetch('/search').then(res => res.json()).then(res => console.log(res));
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
      </div>
    );
  }

export default FilterNav;
