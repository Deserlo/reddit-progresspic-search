import React,{useState,useEffect} from 'react';
import Header from './Header';


function List({ items, fallback }) {
    if (!items || items.length === 0) {
      return fallback;
    } else {
      console.log("first item:", items[0]);
      return items.map(item => {
        return <article><a className="thumbnail" href={item.post_thumbnail} data-position="left center"><img src={item.post_thumbnail} alt="jj"/></a>
        <h2>{item.post_title}</h2>
        <p>{item.progress}</p>
        </article>
      });
    }
  }



function First({ items, fallback }) {
    if (!items || items.length === 0) {
        return fallback;
    } else {
        console.log("First items ", items[0]);
        return <div id="viewer">
            <div className="inner">
                <div className="nav-next"></div>
                <div className="nav-previous"></div>
                <div className="toggle"></div>
            </div>
            <div className="caption">{items[0].post_title}</div>
            <div className="image"><img src={items[0].post_thumbnail} alt="jj"/></div>
        </div> 
    }
}


const getItems = () => fetch('/home').then(res => res.json());

function Container() {
    const [items, setItems] = useState([]);

    useEffect(() => {
        getItems().then(data => setItems(data));
    }, []);


    return (
        <div>
            <div id="main">
                <h1>Progress Pic Search</h1>
                <Header/>
                <section id="thumbnails">
                    <List items={items} fallback={"Loading..."}/>
                </section>
            </div>
            <First items={items} fallback={"Loading..."}/>
        </div>
    );
}

export default Container
