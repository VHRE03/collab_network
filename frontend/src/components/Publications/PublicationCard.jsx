export function PublicationCard({ publication }) {
  return (
    <div>
      <div>
        <p>{publication.author.first_name}</p>
      </div>
      <h1>{publication.title}</h1>
      <p>{publication.abstract}</p>
    </div>
  );
}
