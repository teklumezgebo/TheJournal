import React from "react";

export default function Button({ text }: { text:string }) {
    return (
        <button className="button">{text}</button>
    )
}