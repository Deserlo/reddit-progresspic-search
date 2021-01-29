import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import Header from "./Header";

const getItems = () => fetch("/home").then((res) => res.json());

function Container({ fallback }) {
  const [title, setTitle] = useState("");
  const [src, setSrc] = useState("");
  const [items, setItems] = useState([]);

  const showViewer = (title, thumbnail_src) => {
    setTitle(title);
    setSrc(thumbnail_src);
  };

  useEffect(() => {
    getItems().then((data) => setItems(data));
  }, []);

  const { register, handleSubmit } = useForm();
  const onSubmit = (data) => {
    //alert(JSON.stringify(data));
    //alert(data.gender);
    //alert(data.type);
    let query = "/home"
    if (data.gender != "" ) {
      query = "/search/" + data.gender;
    }
    //alert(query);
    let items = fetch(query).then((res) => res.json().then((data)=>setItems(data)));
  }

/*
  const handleSubmit = (e)=> {
    e.preventDefault();
    console.log(e.target.gender.value);
    console.log(e.target.type.value);
    let query = "/search/" + e.target.gender.value;
    let items = fetch(query).then((res) => res.json().then((data)=>setItems(data)));
  }
*/

  function FilterNav() {

      return (
        <div>
            <h1>Show Me</h1>
          <form onSubmit = {handleSubmit(onSubmit)}>
        <select name="gender" ref={register}>
          <option value="">Select..</option>
          <option value="F">F</option>
          <option value="M">M</option>
          <option value="Cat">Cat</option>
        </select>
  
        <select name="type" ref={register}>
          <option value="">Select..</option>
          <option value="L">Loss</option>
          <option value="G">Gain</option>
        </select>
            <input type="submit"/>
          </form>
        </div>
      );
  }

  function List({ items, fallback }) {
    if (!items || items.length === 0) {
      return fallback;
    } else {
      return items.map((item) => {
        return (
          <article>
            <div
              className="thumbnail"
              name={item.post_thumbnail}
              onClick={() => showViewer(item.post_title, item.post_url)}
              data-position="left center">
              <img src={item.post_thumbnail} alt="jj"/>
            </div>
            <h2>{item.post_title}</h2>
          </article>
        );
      });
    }
  }

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

  return (
    <div>
      <div id="main">
        <h1>Progress Pic Search</h1>
        <FilterNav/>
        <section id="thumbnails">
          <List items={items}  fallback={"Loading..."} />
        </section>
      </div>
      <First items={items} />
    </div>
  );
}

export default Container;
