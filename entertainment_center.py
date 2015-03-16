import media
import fresh_tomatoes

#Movie Instances
american_sniper = media.Movie('American Sniper', 'True Storu of Chris Kyle, the most lethal sniper in U.S. military history', 'http://upload.wikimedia.org/wikipedia/en/1/10/American_Sniper_poster.jpg', 'https://www.youtube.com/watch?v=NTya9A4O9Ws&spfreload=10')
finding_nemo = media.Movie('Finding Nemo', 'It tells the story of the overprotective clownfish named Marlin (Albert Brooks) who, along with a regal tang named Dory (Ellen DeGeneres), searches for his abducted son Nemo (Alexander Gould) all the way to Sydney Harbour', 'http://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg', 'https://www.youtube.com/watch?v=SPHfeNgogVs&spfreload=10')
frozen = media.Movie('Frozen', 'The film tells the story of a fearless princess who sets off on an epic journey alongside a rugged iceman, his loyal pet reindeer, and a naive snowman to find her estranged sister, whose icy powers have inadvertently trapped the kingdom in eternal winter', 'http://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg', 'https://www.youtube.com/watch?v=FLzfXQSPBOg&spfreload=10')
madagascar = media.Movie('Madagascar', 'The film tells the story of four Central Park Zoo animals who have spent their lives in blissful captivity and are unexpectedly shipped back to Africa, getting shipwrecked on the island of Madagascar', 'http://upload.wikimedia.org/wikipedia/en/3/36/Madagascar_Theatrical_Poster.jpg', 'https://www.youtube.com/watch?v=fq5zU9T_Hl4')
madagascar_2 = media.Movie('Madagascar \nEscape 2 Africa', 'The film starts as a prequel, showing a small part of Alex\'s early life, including his capture by hunters. It soon moves to shortly after the point where the original left off, with the animals deciding to return to New York', 'http://upload.wikimedia.org/wikipedia/en/7/7f/Madagascar2poster.jpg', 'https://www.youtube.com/watch?v=hLVjIhPYq7s&spfreload=10')
the_matrix = media.Movie('The Matrix', 'It\'s an awesome movie, with super kool stunts', 'http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg', 'https://www.youtube.com/watch?v=m8e-FF8MsqU&spfreload=10')

#Calling open_movies_page in fresh_tomatoes to render content in html
fresh_tomatoes.open_movies_page([american_sniper, finding_nemo, frozen, madagascar, madagascar_2, the_matrix])