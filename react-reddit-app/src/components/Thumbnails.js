import React,{useState,useEffect} from 'react';



function List({ items, fallback }) {
    if (!items || items.length === 0) {
      return fallback;
    } else {
      //console.log("type of ", typeof(items.data[0]));
      //console.log(items.data[0]);
      return items.map(item => {
        /*return <div key={item.post_id}><img src={item.post_thumbnail}/>{item.post_title}</div>;*/
        /*return <img src={item.post_thumbnail} alt={item.post_title}/>;*/
        return <article><a className="thumbnail" href={item.post_thumbnail} data-position="left center"><img src={item.post_thumbnail} alt="jj"/></a>
        <h2>{item.post_title}</h2>
        <p>{item.progress}</p>
        </article>
      });
    }
  }

const getItems = () => fetch('/home').then(res => res.json());

function Thumbnails() {
const [items, setItems] = useState([]);

useEffect(() => {
    getItems().then(data => setItems(data));
}, []);


return (
    <section id="thumbnails">
    <List items={items} fallback={"Loading..."} />
    </section>
);
}


export default Thumbnails