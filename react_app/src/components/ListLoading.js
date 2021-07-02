import React from "react";

function ListLoading(Component) {
    return function ListLoadingComponent({isLoading, ...props}) {
        if (!isLoading) return <Component {...props} />;
        return (
            <p>Fetching data</p>
        );
    }
}

export default ListLoading;