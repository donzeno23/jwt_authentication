import { useContext, useDebugValue } from "react";
import AuthContext from "../context/AuthProvider";

const useAuth = () => {
    console.log("hooks.useAuth called...");
    const { auth } = useContext(AuthContext);
    console.log("hooks.useAuth.auth="+auth)
    useDebugValue(auth, auth => auth?.user ? "Logged In" : "Logged Out")
    return useContext(AuthContext);
}

export default useAuth;