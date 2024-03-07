import { createContext } from "react";

const AuthContext = createContext({
    state: false,
    onShowCart: () => {},
});

export default AuthContext;