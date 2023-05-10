class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # Get the starting pixel color
        startColor = image[sr][sc]
        
        # Check if the color needs to be changed
        if startColor == newColor:
            return image
        
        # Call the recursive flood fill function
        self.flood_fill_helper(image, sr, sc, startColor, newColor)
        
        # Return the modified image
        return image
    
    def flood_fill_helper(self, image, i, j, startColor, newColor):
        # Check if the pixel is within the image and of the starting color
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != startColor:
            return
        
        # Change the color of the current pixel
        image[i][j] = newColor
        
        # Recursively call the function on all 4-directionally connected pixels
        self.flood_fill_helper(image, i+1, j, startColor, newColor)
        self.flood_fill_helper(image, i-1, j, startColor, newColor)
        self.flood_fill_helper(image, i, j+1, startColor, newColor)
        self.flood_fill_helper(image, i, j-1, startColor, newColor)
