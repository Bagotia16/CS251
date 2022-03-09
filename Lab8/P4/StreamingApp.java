/*
DO NOT MODIFY THE CODE STUB
NO NEED TO DEFINE main()
*/

import java.util.*;

class StreamingApp
{
	public static String findGenre(Map<String,ArrayList<String>>movieGenres,String movie)
	{
		for(String Genre: movieGenres.keySet())
		{
			if(movieGenres.get(Genre).contains(movie))
			{
				return Genre;
			}
		}
		return null;
	}

	public static Map<String, ArrayList<String> > getFavouriteGenres(Map<String, ArrayList<String> > userMovies, Map<String, ArrayList<String> > movieGenres)
	{
		
		// WRITE YOUR CODE HERE
		if(userMovies==null||movieGenres==null)return null;
		Map<String, Map<String,Integer>> genreCount = new HashMap<>();
//		Integer k = movieGenres.keySet().size();
		for(String name: userMovies.keySet())
		{
			Map<String,Integer> temp = new HashMap<>();
			for(String genre: movieGenres.keySet())
			{
				temp.put(genre,0);
			}
			genreCount.put(name,temp);
		}
		for(String name: userMovies.keySet())
		{
			ArrayList<String> movies = userMovies.get(name);
			for(String movie: movies)
			{
				String genre = findGenre(movieGenres,movie);
				genreCount.get(name).put(genre,genreCount.get(name).get(genre)+1);

			}
		}
		Map<String, ArrayList<String>> result = new HashMap<>();
		for(String name: userMovies.keySet())
		{
			Map<String,Integer> temp_genre = genreCount.get(name);
			Integer max = 0;
			for(String genre: temp_genre.keySet())
			{
				if(temp_genre.get(genre) > max)
				{
					max = temp_genre.get(genre);
				}
			}
			ArrayList<String> buffer = new ArrayList<>();
			for(String genre: temp_genre.keySet())
			{
				if(temp_genre.get(genre).equals(max) && max > 0)
				{
					buffer.add(genre);
				}
			}
			result.put(name,buffer);
		}

		return result;
		
	}
}