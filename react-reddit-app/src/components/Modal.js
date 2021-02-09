import React from 'react';
import './modal.css';



const Modal = (props) => {
  const { closeModal } = props;

  const closeicon = () => (
    <div
    name="times"
    onClick={closeModal}
    style={{
      color: 'white',
      padding: '10px',
      cursor: 'pointer',
      backgroundColor: 'transparent',
      border: 0,
      position: 'absolute',
      top: '-2.5rem',
      right: '0.3rem',
    }}
    >X</div>
  );

  return (
    <div className="overlay">
      <div className="content">
        { closeicon() }
        {props.children}
      </div>
    </div>
  );
};


export default Modal;