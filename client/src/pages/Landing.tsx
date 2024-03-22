import React from "react";
import Button from "../components/Button";
import "../assets/scss/App.css";

export default function Landing(){
    return (
            <body className="landing">
                <header>
                    <span>The Journal</span>
                </header>
                <main>
                    <article>
                        <p>Let your mind be a peaceful haven in turbulent times.</p>
                        <p>Experience calmness through introspection.</p>
                        <p>Discover peace within your inner reflections.</p>
                    </article>
                    <div>
                        <Button text="Make an account"/>
                        <Button text="Login"/>
                    </div>
                    <article>
                        <p>Writing about one's thoughts has been proven to be therapeutic and beneficial, offering individuals an outlet for self-expression, reflection, and personal growth, ultimately fostering a deeper understanding of oneself and promoting emotional well-being.</p>
                    </article>
                </main>
                <footer>
                    <a href="https://www.linkedin.com/in/teklumezgebo/">Created by Teklu Mezgebo</a>
                    <a href="https://github.com/teklumezgebo/TheJournal">Source Code</a>
                </footer>
            </body>
    )
}