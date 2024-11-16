import { useState } from "react";
import { useEffect } from "react";
import { getPublications } from "../services/ResearchPublicationAPI";

function name(publicationId) {
  const [publications, setPublications] = useState([]);

  useEffect(() => {
    async function loadPublications() {
      const response = await getPublications();
      setPublications(response.data);
      console.log(response);
    }

    loadPublications();
  }, []);

  return <div></div>;
}
