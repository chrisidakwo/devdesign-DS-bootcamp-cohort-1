# Task 3: Music Playlist 🎵

# You are managing a music app and need to handle a user's playlist.

# Instructions:

# Create a list called playlist containing five song titles.
# A user wants to add two new songs at once. Use an appropriate method to extend the list with these songs.
# The user decides to remove a song they no longer like. Remove the third song from the playlist.
# Print the updated playlist and display the total number of songs in it.
# Retrieve and print the first three songs in the playlist using slicing.

playlist = ["Danger", "Rendevouz", "Cry", "First Time", "Barcelona"]

# Use extend() to add multiple list items at once
playlist.extend(["Love", "Hate"])

# Use concatenation to add multiple list items at once
# playlist = playlist + ["Love", "Hate"]

# Delete the 3rd song from the playlist
del playlist[2]

print(f"Updated playlist: {playlist}")
print(f"Total number of songs: {len(playlist)}")

first3Songs = playlist[:3]
print(f"The first 3 songs are: {first3Songs}")
