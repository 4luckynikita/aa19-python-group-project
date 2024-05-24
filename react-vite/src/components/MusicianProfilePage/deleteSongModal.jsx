import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { fetchCurrentMusician } from "../../redux/musicians";
import { deleteAlbum, fetchAlbums } from "../../redux/albums";


const DeleteSongModal = ({album})=>{
const {closeModal} = useModal()
const currentUser = useSelector((state)=> state.session.user)
const id = album && album.id
const dispatch = useDispatch()

const handleClick = async(e) =>{
    e.preventDefault()

    await dispatch(deleteAlbum(id))
    .then (closeModal)
    dispatch(fetchAlbums(currentUser.id))
}


const close = (e) => {
    e.preventDefault()
    return closeModal()
}

return (
    <div>
        <h1>Confirm Delete</h1>
        <p>Are you sure you want to delete this album?</p>
        <button onClick={handleClick}>Yes</button>
        <button onClick={close}>No</button>
    </div>
)
}

export default DeleteSongModal
