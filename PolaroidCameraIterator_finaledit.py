class PolaroidCameraIterator:
    def __init__(self, cameras):
        # Assigning a key and value relationship to our cameras dictionary
        # 'camera_name' will be the primary 'key' in our dictionary and 'details' the corresponding tuple 'values' (tuples aka dictionaries within dictionaries)
            # camera_name - will be the primary key of the parent dictionary
            # details - will include as list of nested dictionaries for camera attributes (flash, film, year established)
        self.polaroid_cameras = list(cameras.items())  # Without this function, the iterator will not be able to parse a complex dictionary
        self.position = 0  # Sets the default starting point of the iterator at the first row of the dictionary

    # The __iter__() function returning itself allows it to prepare objects passed through it for loops
    def __iter__(self):
        return self

    # Defines the conditions for when the loop should look for what's next in the dictionary
    def __next__(self):
        # Sets the condition to run while the position of the row looped is less than the total length or number of rows/cameras in the dictionary
        if self.position < len(self.polaroid_cameras):
            # Returns the camera details in the dictionary relative to the number of times the loop has run
            camera = self.polaroid_cameras[self.position]
            # Adds 1 to the position each time the loop runs so that it keeps returning the next camera each loop
            self.position += 1
            return camera  # Returns a tuple (camera_name, details)
        else:
            raise StopIteration  # Stops iteration when no more cameras are available

    # Resets the iterator position to 0 once complete so that it can loop the sequence in order if restarted
    def reset(self):
        self.position = 0

# Create a parent dictionary listing the camera names
# Create a nested set of dictionaries listing the attributes of the cameras
camera_data = {
    "SX70 Sonar": {"Film": "SX70 Film", "Flash Type": "No Flash", "Year": 1978},
    "SLR680": {"Film": "SX70 Film", "Flash Type": "Flash", "Year": 1982},
    "OneStep 600": {"Film": "600 Film", "Flash Type": "No Flash", "Year": 1983},
    "Sun 600": {"Film": "600 Film", "Flash Type": "Flash", "Year": 1984},
    "SuperColor 635": {"Film": "600 Film", "Flash Type": "Flash", "Year": 1985},
    "Impulse": {"Film": "600 Film", "Flash Type": "Flash", "Year": 1988},
    "OneStep+": {"Film": "i-type Film", "Flash Type": "Flash", "Year": 2018},
    "I-2": {"Film": "i-type Film", "Flash Type": "Flash", "Year": 2023}
}

# Initialize the iterator as a variable that uses the camera_data dictionary in preparation for the for-loop method below
camera_iterator = PolaroidCameraIterator(camera_data)

# Prompt the user for day or night
# strip function - removes extra spaces typed in error by the user
# lower function - converts all user entries to lowercase
time_of_day = input("Is it day or night time? ").strip().lower()

# Initial output based on the time of day
if time_of_day == "day":
    print("Cameras without Flash:")
    cameras_output = []  # Define to save outputs from the iterator based on user selection
    # For-loop that uses 'key' and 'value' pairs from dictionary to inform the iterator for loop conditions
    for camera_name, details in camera_iterator:
        if details["Flash Type"] == "No Flash":
            with_or_without = "without"
            print(f" {camera_name}")
            # append function saves the subset of cameras by adding each relevant camera iterated to the camera_outputs list
            cameras_output.append((camera_name, details))

# Handling "night" input, moved outside the "day" block to ensure it's checked independently
elif time_of_day == "night":
    print("Cameras with Flash:")
    cameras_output = []  # Reset the output list to store night cameras
    camera_iterator.reset()  # Reset the iterator to use it again for night cameras
    for camera_name, details in camera_iterator:
        if details["Flash Type"] == "Flash":
            with_or_without = "with"
            print(f" {camera_name}")
            cameras_output.append((camera_name, details))

# Error if the user does not enter day or night
else:
    print("Error: Did not enter day or night.")
    # Exit() terminates the session
    exit()  # cannot complete second condition without successfully completing the first

# Prompt the user for film type after displaying the cameras with or without flash
film_type = input("Do you have SX70, 600, or i-type film? ").strip().lower()

# Mapping of user input to corresponding film types in the dictionary to manage potential misentry
film_type_mapping = {
    "sx70": "SX70 Film",
    "600": "600 Film",
    "i-type": "i-type Film"
}

# Check if the film type input is valid
if film_type in film_type_mapping:

    # Subset film_type_mapping dictionary by user-entered film type
    selected_film = film_type_mapping[film_type]
    print(f"\nCameras {with_or_without} flash and {selected_film}:")
    # Use camera_outputs dictionary from first flash condition output for second filtering loop
    for camera_name, details in cameras_output:
        # Further subset camera_outputs by selected film values
        if details["Film"] == selected_film:
            print(f"{camera_name}")

# Error message if the user does not enter a corresponding type of film
else:
    print("Error: Invalid film type entered.")
