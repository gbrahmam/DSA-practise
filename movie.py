class Movie:
    
    def __init__(self):
        pass
        
    def run(self,movie_name,num_chars,length):
        self.language = movie_name
        self.num_characters = num_chars
        self.length_in_minutes = length
        return('This is a ' + self.language + ' movie with ' + str(self.num_characters) + ' characters and is ' + str(self.length_in_minutes) + ' minutes long.')


#inputs
movie_name = input()
num_chars = int(input())
length = int(input())
movie = Movie()
print(movie.run(movie_name,num_chars,length))