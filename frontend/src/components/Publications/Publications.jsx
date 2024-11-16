import { useEffect, useState } from "react";
import { PublicationCard } from "./PublicationCard";
import { getPublications } from "../../services/ResearchPublicationAPI";

export function Publications() {
  const [publications, setPublications] = useState([]);

  useEffect(() => {
    async function loadPublications() {
      const response = await getPublications();
      setPublications(response.data);
    }

    loadPublications();
  }, []);

  return (
    <div>
      {publications.map((publication) => (
        <div key={publication.id}>
          <PublicationCard publication={publication} />
        </div>
      ))}
    </div>
  );
}
