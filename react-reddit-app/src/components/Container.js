import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import Modal from './Modal';






const getItems = () => fetch("/home").then((res) => res.json());

function Container({ fallback }) {
  const [title, setTitle] = useState("");
  const [src, setSrc] = useState("");
  const [link, setLink] = useState("");
  const [items, setItems] = useState([]);
  const [status, setStatus] = useState(false);

  const showViewer = (title, thumbnail_src, link, status) => {
    setTitle(title);
    setSrc(thumbnail_src);
    setLink(link);
    setStatus(status);
    //console.log(link);
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
      query = "/search/" + data.gender + "/" + data.type;
    }
    //alert(query);
    let items = fetch(query).then((res) => res.json().then((data)=>setItems(data)));
  }


  function FilterNav() {

      return (
        <div>
            <h1>Show Me</h1>
          <form onSubmit = {handleSubmit(onSubmit)}>
        <select name="gender" ref={register}>
          <option value="">Select..</option>
          <option value="F">F</option>
          <option value="M">M</option>
        </select>
  
        <select name="type" ref={register}>
          <option value="">Select..</option>
          <option value="1">Loss</option>
          <option value="2">Gain</option>
        </select>
            <input type="submit" value="Search"/>
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
            <a
              className="thumbnail"
              name={item.post_thumbnail}
              onClick={() => showViewer(item.post_title, item.post_url, item.post_permalink, true)}
              data-position="left center">
              <img src={item.post_thumbnail} alt={item.post_title}/>
            </a>
            <h2>{item.post_title}</h2>
 
          </article>
        );
      });
    }
  }




/*
  function First({ items, fallback }) {
    return (
      <div id="viewer">
        { status && (<Modal closeModal={() => setStatus(false)}>
        <div className="inner">
          <div className="nav-next"></div>
          <div className="nav-previous"></div>
          <div className="toggle"></div>
        </div>
        <div className="slide active">
        <div className="caption">{title}</div>
        <div className="image">
        <a href={"https://reddit.com"+ link} target="_blank"><img className="view" src={src}/></a> 
        </div>
        </div>
        </Modal>)}
      </div>
    );
  }
  */

  function First({ items, fallback }) {
    return (
      <div id="viewer">
        <div className="inner">
          <div className="nav-next"></div>
          <div className="nav-previous"></div>
          <div className="toggle"></div>
        </div>
        <div className="slide active">
        <div className="caption">{title}</div>
        <div className="image">
        {/*<a href={"https://reddit.com"+ link} target="_blank">*/}<img className="view" src={src}/>{/*</a> */}
        </div>
        </div>
      </div>
    );
  }





  return (
    <div>
      <div id="main">
        <h1>Progress Pic Search</h1>
        <FilterNav/>
        <div className="modal-modal">
          { status && (<Modal closeModal={() => setStatus(false)}><First items={items} /></Modal>)}
        </div>
        <section id="thumbnails">
          <List items={items}  fallback={"Loading..."} />
        </section>
      </div>
      <First items={items} />
    </div>
  );
}

export default Container;
