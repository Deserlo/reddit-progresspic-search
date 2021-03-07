import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import Modal from './Modal';


const getItems = () => fetch("/home").then((res) => res.json());

function Container({ fallback }) {
  const [title, setTitle] = useState('');
  const [src, setSrc] = useState('');
  const [link, setLink] = useState("");
  const [items, setItems] = useState([]);
  const [status, setStatus] = useState(false);
  const [query, setQuery] = useState("");

  const showViewer = (title, thumbnail_src, link, status) => {
    setTitle(title);
    setSrc(thumbnail_src);
    setLink(link);
    setStatus(status);
  };

  useEffect(() => {
    getItems().then((data) => setItems(data));
  }, []);
  
  



  const { register, handleSubmit } = useForm();
  const onSubmit = (data) => {
    //alert(JSON.stringify(data));
    let args = ""
    for (const property in data){
      args+= "prop" + property + "="+ data[property];
    }
    for (const property in data){
      if (data[property] == "all" || data[property].startsWith("0-") ){
        delete data[property];
      }
    }
    setQuery(JSON.stringify(data));
    let query = "/search/" + args;
    let items = fetch(query).then((res) => res.json().then((data)=>setItems(data)));
  }

  function FilterNav() {

      return (
      <div>
          <h1>Options:</h1>
          <form onSubmit = {handleSubmit(onSubmit)}>
        <select name="gender" ref={register}>
          <option value="all">Gender</option>
          <option value="F">F</option>
          <option value="M">M</option>
        </select>
        <select name="age" ref={register}>
          <option value="0-150">Age</option>
          <option value="1-17">Under 18</option>
          <option value="18-30">18-30</option>
          <option value="31-45">31-45</option>
          <option value="46-150">46+</option>
        </select>
        <select name="height" ref={register}>
          <option value="0-240">Height</option>
          <option value="1-47">Under 4'0</option>
          <option value="48">4'0</option>
          <option value="49">4'1</option>
          <option value="50">4'2</option>
          <option value="51">4'3</option>
          <option value="52">4'4</option>
          <option value="53">4'5</option>
          <option value="54">4'6</option>
          <option value="55">4'7</option>
          <option value="56">4'8</option>
          <option value="57">4'9</option>
          <option value="58">4'10</option>
          <option value="59">4'11</option>
          <option value="60">5'0</option>
          <option value="61">5'1</option>
          <option value="62">5'2</option>
          <option value="63">5'3</option>
          <option value="64">5'4</option>
          <option value="65">5'5</option>
          <option value="66">5'6</option>
          <option value="67">5'7</option>
          <option value="68">5'8</option>
          <option value="69">5'9</option>
          <option value="70">5'10</option>
          <option value="71">5'11</option>
          <option value="72">6'0</option>
          <option value="73">6'1</option>
          <option value="74">6'2</option>
          <option value="75">6'3</option>
          <option value="76">6'4</option>
          <option value="77">6'5</option>
          <option value="78">6'6</option>
          <option value="79">6'7</option>
          <option value="80">6'8</option>
          <option value="81">6'9</option>
          <option value="82">6'10</option>
          <option value="83">6'11</option>
          <option value="84">7'0</option>
          <option value="85">7'1</option>
          <option value="86">7'2</option>
          <option value="87">7'3</option>
          <option value="88">7'4</option>
          <option value="89">7'5</option>
          <option value="90">7'6</option>
          <option value="91">7'7</option>
          <option value="92">7'8</option>
          <option value="93">7'9</option>
          <option value="94">7'10</option>
          <option value="95">7'11</option>
        </select>
        <select name="type" ref={register}>
          <option value="all">Progress Type</option>
          <option value="1">Loss</option>
          <option value="2">Gain</option>
        </select>
        <select name="starting" ref={register}>
          <option value="0-2000">Starting Weight</option>
          <option value="1-99">0-99</option>
          <option value="100-119">100-119</option>
          <option value="120-139">120-139</option>
          <option value="140-159">140-159</option>
          <option value="160-179">160-179</option>
          <option value="180-199">180-199</option>
          <option value="200-219">200-219</option>
          <option value="220-279">220-279</option>
          <option value="280-339">280-339</option>
          <option value="340-419">340-419</option>
          <option value="420-499">420-499</option>
          <option value="500-800">500-800</option>
        </select>
        <select name="current" ref={register}>
          <option value="0-2000">Goal Weight</option>
          <option value="1-99">0-99</option>
          <option value="100-119">100-119</option>
          <option value="120-139">120-139</option>
          <option value="140-159">140-159</option>
          <option value="160-179">160-179</option>
          <option value="180-199">180-199</option>
          <option value="200-219">200-219</option>
          <option value="220-279">220-279</option>
          <option value="280-339">280-339</option>
          <option value="340-419">340-419</option>
          <option value="420-499">420-499</option>
          <option value="500-800">500-800</option>
        </select>
        {/*}
        <select name="pounds" ref={register}>
          <option value="0-2000">Pounds Lost/Gained</option>
          <option value="0-20">0-20</option>
          <option value="20-40">20-40</option>
          <option value="41-80">41-80</option>
          <option value="81-120">81-120</option>
          <option value="121-300">121-300</option>
        </select>
      */}
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




  function First({ items, fallback }) {
    return (
      <div id="viewer">
        <div className="inner">
          <div className="nav-next"></div>
          <div className="nav-previous"></div>
          <div className="toggle"></div>
        </div>
        <div className="slide active">
        <a href={"https://reddit.com"+ link} target="_blank"><div className="caption">{title}</div></a>
        <div className="image">
        {/*<a href={"https://reddit.com"+ link} target="_blank">*/}<img className="view" src={src}/>{/*</a> */}
        </div>
        </div>
      </div>
    );
  }

function FilterQuery({query}){
  return (
    <p>{query}</p>
  )

}


  return (
    <div>
      <div id="main">
        <h1>Find Me Progress Photos</h1>
        <FilterNav/>
        <FilterQuery query={query} />
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
