import React from "react";
import { useState, ChangeEvent, FormEvent } from "react";

export default function SignUpForm() {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    function handleUsernameChange(event: ChangeEvent<HTMLInputElement>) {
        setUsername(event.target.value)
    }

    function handlePasswordChange(event: ChangeEvent<HTMLInputElement>) {
        setPassword(event.target.value)
    }

    function handleFormSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()
        console.log({
            "username": username,
            "password": password
        })
    }

    return (
        <form onSubmit={handleFormSubmit}>
            <input type="username" value={username} onChange={handleUsernameChange} />
            <input type="password" value={password} onChange={handlePasswordChange} />
            <input type="submit" />
        </form>
    )
}