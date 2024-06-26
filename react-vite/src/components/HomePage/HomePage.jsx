import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import { getAllAlbums } from "../../redux/albums";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner";
import "./HomePage.css";
import { NavLink } from "react-router-dom";

const HomePage = () => {
  const dispatch = useDispatch();
  const [isLoading, setIsLoading] = useState(true);
  //let sortedAlbums = [...albumState.albums].sort((a, b) => new Date(b.release_date) - new Date(a.release_date));

  useEffect(() => {
    const fetchData = async () => {
      await dispatch(getAllAlbums());
      setIsLoading(false);
    };
    fetchData();
  }, [dispatch]);

  let albumState = useSelector((state) => state.albums);
  let randInt = 4;
  //   //console.log(albumState?.albums);

  // albumState &&
  //   albumState?.albums?.length &&
  //   (randInt = Math.floor(Math.random() * albumState?.albums?.length));

  //   //console.log(randInt);
  ////console.log([...albumState?.albums].sort((a, b) => new Date(b.release_date) - new Date(a.release_date)))

  return (
    <>
      {isLoading ? (
        <LoadingSpinner />
      ) : (
        <div className="homepage-container">
          {/* <h1 className="homepage-home-text">HOME</h1> */}
          <div className="homepage-featured-container">
            <div className="homepage-featured-container-inner">
              <h1 className="homepage-featured-container-title">Recommended</h1>
              {albumState?.albums && (
                <NavLink
                  className={"navlinkhome"}
                  to={`/musicians/${albumState?.albums[randInt]?.user_id}`}
                >
                  <div className="homepage-featured-image-container">
                    <img
                      src={albumState?.albums[randInt]?.image_url}
                      alt={albumState?.albums[randInt]?.title}
                      className="homepage-featured-image"
                    />
                    <div className="homepage-featured-leftmost-container">
                      <h1 className="homepage-featured-title">
                        {albumState?.albums[randInt]?.title}
                      </h1>
                      <h2 className="homepage-featured-title">
                        {albumState?.albums[randInt]?.musician[0].name}
                      </h2>
                      <p className="homepage-featured-description">
                        {albumState?.albums[randInt]?.description}
                      </p>
                    </div>
                  </div>
                </NavLink>
              )}
            </div>
            <div className="very-cool-line" />
            <div className="homepage-featured-container-inner">
              <h1 className="homepage-featured-container-title">
                Well Received Albums
              </h1>
              <div className="homepage-featured-image-container">
                {albumState?.albums &&
                  albumState?.albums?.slice(0, 5).map((album) => (
                    <div
                      className="homepage-featured-container-image"
                      key={album?.id}
                    >
                      <NavLink to={`/musicians/${album?.user_id}`}>
                        <img
                          src={album?.image_url}
                          alt={album?.title}
                          className="homepage-featured-image"
                        />
                        <p className="homepage-featured-album-name">
                          {album?.title}
                        </p>
                      </NavLink>
                    </div>
                  ))}
              </div>
            </div>
            <div className="very-cool-line" />
            <div className="homepage-featured-container-inner">
              <h1 className="homepage-featured-container-title">
                New Releases
              </h1>
              <div className="homepage-featured-image-container">
                {albumState?.albums &&
                  [...albumState.albums]
                    .sort(
                      (a, b) =>
                        new Date(b.release_date) - new Date(a.release_date)
                    )
                    .slice(0, 5)
                    .map((album) => (
                      <div
                        className="homepage-featured-container-image"
                        key={album?.id}
                      >
                        <NavLink to={`/musicians/${album?.user_id}`}>
                          <img
                            src={album?.image_url}
                            alt={album?.title}
                            className="homepage-featured-image"
                          />
                          <p className="homepage-featured-album-name">
                            {album?.title}
                          </p>
                        </NavLink>
                      </div>
                    ))}
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default HomePage;
