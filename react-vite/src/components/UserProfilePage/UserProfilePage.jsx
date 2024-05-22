import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import { getUser } from "../../redux/users";

const UserProfilePage = () => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.users.users[id]);
  const loading = useSelector((state) => state.users.loading);
  const error = useSelector((state) => state.users.error);

  useEffect(() => {
    dispatch(getUser(id));
  }, [dispatch, id]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  if (!user) return <div>User not found</div>;

  return (
    <div>
      <div>
        <img src={user.image_url} alt={user.image_url} />
        <div>
          <div>
            <h1>{`${user.first_name} ${user.last_name}`}</h1>
            <p>Joined on {user.created_at}</p>
          </div>
          <div>
            <p>{user.description}</p>
          </div>
          <div>
            <button onClick={() => navigate(`/users/${id}/edit`)}>
              Edit Profile
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserProfilePage;
