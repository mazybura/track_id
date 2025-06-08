import React, { useState, useEffect } from "react";
import "./RotatingBackground.css";

function RotatingBackground() {
    const [rotationY, setRotationY] = useState(0);
    const [rotationX, setRotationX] = useState(0);

    useEffect(() => {
        const handleMouseMove = (e) => {
            const windowWidth = window.innerWidth;
            const windowHeight = window.innerHeight;
            const mouseX = e.clientX;
            const mouseY = e.clientY;

            const rotateY = ((mouseX - windowWidth / 2) / windowWidth) * 30;
            const rotateX = ((mouseY - windowHeight / 2) / windowHeight) * 30;

            setRotationY(rotateY);
            setRotationX(rotateX / 5);
        };

        window.addEventListener("mousemove", handleMouseMove);
        return () => {
            window.removeEventListener("mousemove", handleMouseMove);
        };
    }, []);

    return (
        <div className="background-container">
            <img
                src="/images/jump_logo.png"
                className="rotating-image"
                style={{ transform: `rotateY(${rotationY}deg) rotateX(${rotationX}deg)` }}
                alt="Rotating Background"
            />
        </div>
    );
}

export default RotatingBackground;
