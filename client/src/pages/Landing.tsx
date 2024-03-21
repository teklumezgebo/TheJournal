import React from "react";
import Button from "../components/Button";
import "../assets/scss/App.css";

export default function Landing(){
    return (
            <body className="landing-container">
                <header>
                    <span>The Journal: A web application dedicated to giving people a space to document their thoughts and emotinons.</span>
                </header>
                <main>
                    <p>Find solace in your words.</p>
                    <p>This journaling application offers a comforting sanctuary to pour out your thoughts and feelings, providing solace and understanding every step of the way.</p>
                    <div className="button-container">
                        <Button text="Make an account"/>
                        <Button text="Login"/>
                    </div>
                </main>
                <footer>
                    <span>Created by: Teklu Mezgebo</span>
                    <span>Souce Code</span>
                </footer>
            </body>
    )
}