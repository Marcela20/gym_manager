import { useEffect, useState} from 'react';
import axios from 'axios';

const useFetchData = () => {
  const [raw_data, setData] = useState();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const { data: response } = await axios.get('http://127.0.0.1:8000/api/calendar/?group=1');
        setData(response);
      } catch (error) {
        console.error(error)
      }
      setLoading(false);
    };

    fetchData();
  }, []);

  return {
    raw_data,
    loading,
  };
};

export default useFetchData;