import React, { useState, useEffect } from "react";

  function First({ items, fallback }) {
    return (
      <div id="viewer">
        <div className="inner">
          <div className="nav-next"></div>
          <div className="nav-previous"></div>
          <div className="toggle"></div>
        </div>
        <div className="caption">{title}</div>
        <div className="image">
          <img className="view" src={src} />
        </div>
      </div>
    );
  }

  export default First;