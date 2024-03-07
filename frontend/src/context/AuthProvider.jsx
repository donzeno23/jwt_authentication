import { useState } from "react";
import AuthContext from "./auth-context";

export const AuthProvider = ({ children }) => {
    const [auth, setAuth] = useState({});
    console.log("AuthProvider.auth="+auth);
    console.log("AuthProvider.setAuth"+setAuth);

    const authCtx = {
        state: auth,
        onShowCart: setAuth,
      };
    

    // The created context is an object with two properties: 
    // Provider and Consumer, both of which are components

    // To pass our value down to every component in our App,
    // we wrap our Provider component around it (in this case, authentication).
    
    // we put the value that we want to pass down our entire component tree
    return (
        //<AuthContext.Provider value={{ auth, setAuth }}>
        <AuthContext.Provider value={authCtx}>
            {children}
        </AuthContext.Provider>
    )
}

export default AuthProvider;