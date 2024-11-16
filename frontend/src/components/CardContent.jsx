const CardContent = (title, abstract, status, category) => {
  return (
    <div>
      <h2>{title}</h2>
      <p>{abstract}</p>
      <div>
        <p>{status}</p>
        <p>{category}</p>
      </div>
    </div>
  );
};

export default CardContent;
